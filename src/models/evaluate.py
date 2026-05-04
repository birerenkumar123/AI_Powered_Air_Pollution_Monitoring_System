"""
Model Evaluation Module

Handles model evaluation and performance metrics
"""

import logging
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_auc_score, classification_report
)

logger = logging.getLogger(__name__)


class ModelEvaluator:
    """Evaluate model performance."""
    
    def __init__(self):
        """Initialize ModelEvaluator."""
        pass
    
    def evaluate(self, y_true, y_pred):
        """
        Evaluate model performance.
        
        Args:
            y_true (np.ndarray): True labels
            y_pred (np.ndarray): Predicted labels
            
        Returns:
            dict: Dictionary of evaluation metrics
        """
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted'),
            'recall': recall_score(y_true, y_pred, average='weighted'),
            'f1': f1_score(y_true, y_pred, average='weighted'),
        }
        
        logger.info(f"Model Evaluation Metrics:\n{metrics}")
        return metrics
    
    def get_classification_report(self, y_true, y_pred):
        """
        Get detailed classification report.
        
        Args:
            y_true (np.ndarray): True labels
            y_pred (np.ndarray): Predicted labels
            
        Returns:
            str: Classification report
        """
        return classification_report(y_true, y_pred)
