"""
Prediction Module

Handles making predictions using trained models
"""

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


class Predictor:
    """Make predictions using trained models."""
    
    def __init__(self, model):
        """
        Initialize Predictor.
        
        Args:
            model: Trained model object
        """
        self.model = model
    
    def predict(self, features):
        """
        Make predictions on new data.
        
        Args:
            features (pd.DataFrame or np.ndarray): Input features
            
        Returns:
            np.ndarray: Predicted values (0=sell, 1=buy)
        """
        return self.model.predict(features)
    
    def predict_proba(self, features):
        """
        Get prediction probabilities.
        
        Args:
            features (pd.DataFrame or np.ndarray): Input features
            
        Returns:
            np.ndarray: Prediction probabilities
        """
        if hasattr(self.model, 'predict_proba'):
            return self.model.predict_proba(features)
        else:
            raise NotImplementedError("Model does not support predict_proba")
