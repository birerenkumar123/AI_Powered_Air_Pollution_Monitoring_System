"""
Data Preprocessing Module

Handles data cleaning, missing value imputation, and data normalization
"""

import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)


class Preprocessor:
    """Handle data preprocessing tasks."""
    
    def __init__(self, config):
        """
        Initialize Preprocessor.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.scaler = StandardScaler()
    
    def fit_transform(self, data):
        """
        Fit preprocessor and transform data.
        
        Args:
            data (pd.DataFrame): Raw input data
            
        Returns:
            pd.DataFrame: Preprocessed data
        """
        logger.info("Starting data preprocessing pipeline...")
        
        try:
            # Step 1: Handle missing values
            logger.info("Step 1: Handling missing values...")
            data = self.handle_missing_values(data, strategy='forward_fill')
            
            # Step 2: Remove duplicates
            logger.info("Step 2: Removing duplicates...")
            data = data.drop_duplicates()
            
            # Step 3: Handle outliers (optional, based on config)
            logger.info("Step 3: Handling outliers...")
            data = self.remove_outliers(data)
            
            # Step 4: Normalize features
            logger.info("Step 4: Normalizing features...")
            data = self.normalize_features(data)
            
            logger.info(f"Preprocessing completed. Output shape: {data.shape}")
            return data
            
        except Exception as e:
            logger.error(f"Error in preprocessing pipeline: {str(e)}")
            raise
    
    def handle_missing_values(self, data, strategy='forward_fill'):
        """
        Handle missing values in data.
        
        Args:
            data (pd.DataFrame): Input data
            strategy (str): Strategy for handling missing values
            
        Returns:
            pd.DataFrame: Data with missing values handled
        """
        if strategy == 'forward_fill':
            return data.ffill()
        elif strategy == 'backward_fill':
            return data.bfill()
        elif strategy == 'drop':
            return data.dropna()
        elif strategy == 'mean':
            numerical_cols = data.select_dtypes(include=[np.number]).columns
            for col in numerical_cols:
                data[col].fillna(data[col].mean(), inplace=True)
            return data
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
    
    def normalize_features(self, data):
        """
        Normalize numerical features.
        
        Args:
            data (pd.DataFrame): Input data
            
        Returns:
            pd.DataFrame: Normalized data
        """
        numerical_cols = data.select_dtypes(include=[np.number]).columns
        data[numerical_cols] = self.scaler.fit_transform(data[numerical_cols])
        return data
    
    def remove_outliers(self, data, method='iqr', threshold=1.5):
        """
        Remove outliers from numerical data.
        
        Args:
            data (pd.DataFrame): Input data
            method (str): Method to detect outliers ('iqr' or 'zscore')
            threshold (float): Threshold for outlier detection
            
        Returns:
            pd.DataFrame: Data with outliers removed
        """
        numerical_cols = data.select_dtypes(include=[np.number]).columns
        
        if method == 'iqr':
            for col in numerical_cols:
                Q1 = data[col].quantile(0.25)
                Q3 = data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
        
        elif method == 'zscore':
            from scipy import stats
            z_scores = np.abs(stats.zscore(data[numerical_cols]))
            data = data[(z_scores < threshold).all(axis=1)]
        
        logger.info(f"Outliers removed. New shape: {data.shape}")
        return data
