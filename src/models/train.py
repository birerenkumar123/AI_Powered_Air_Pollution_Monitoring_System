"""
Model Training Module

Handles training of machine learning models
"""

import logging
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

logger = logging.getLogger(__name__)


class ModelTrainer:
    """Train machine learning models for trading predictions."""
    
    def __init__(self, config):
        """
        Initialize ModelTrainer.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.model_type = config['model']['type']
        self.model = None
    
    def train(self, data, target_col='target'):
        """
        Train the machine learning model.
        
        Args:
            data (pd.DataFrame): Training data with features and target
            target_col (str): Name of target column
            
        Returns:
            model: Trained model object
        """
        try:
            logger.info("Starting model training...")
            
            # Check if target column exists
            if target_col not in data.columns:
                logger.warning(f"Target column '{target_col}' not found. Creating binary classification target.")
                # Create target based on price movement (example)
                data[target_col] = (data[data.columns[0]].pct_change() > 0).astype(int)
            
            # Separate features and target
            X = data.drop(columns=[target_col, 'Symbol'] if 'Symbol' in data.columns else [target_col])
            y = data[target_col]
            
            logger.info(f"Features shape: {X.shape}, Target shape: {y.shape}")
            
            # Split data
            test_size = self.config['model'].get('test_size', 0.2)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y,
                test_size=test_size,
                random_state=self.config['model'].get('random_state', 42)
            )
            
            logger.info(f"Training set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")
            
            # Build and train model
            self._build_model()
            logger.info(f"Training {self.model_type} model...")
            self.model.fit(X_train, y_train)
            
            # Evaluate
            train_score = self.model.score(X_train, y_train)
            test_score = self.model.score(X_test, y_test)
            
            logger.info(f"Training score: {train_score:.4f}")
            logger.info(f"Test score: {test_score:.4f}")
            
            return self.model
            
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
    
    def _build_model(self):
        """Build model based on configuration."""
        if self.model_type == 'xgboost':
            params = self.config['model']['xgboost']
            self.model = xgb.XGBClassifier(**params)
        elif self.model_type == 'lightgbm':
            # TODO: Implement LightGBM model
            raise NotImplementedError("LightGBM not yet implemented")
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")
    
    def save_model(self, filepath):
        """
        Save trained model to disk.
        
        Args:
            filepath (str): Path to save model
        """
        if self.model is None:
            raise ValueError("No model to save. Train model first.")
        
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
        logger.info(f"Model saved to {filepath}")
    
    def load_model(self, filepath):
        """
        Load pre-trained model from disk.
        
        Args:
            filepath (str): Path to saved model
        """
        with open(filepath, 'rb') as f:
            self.model = pickle.load(f)
        logger.info(f"Model loaded from {filepath}")
