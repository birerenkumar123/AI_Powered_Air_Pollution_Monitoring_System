"""
Trading Strategy Module

Handles trading logic and signal generation
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)


class TradingStrategy:
    """Define and execute trading strategy."""
    
    def __init__(self, config):
        """
        Initialize TradingStrategy.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.buy_threshold = config['strategy']['buy_threshold']
        self.sell_threshold = config['strategy']['sell_threshold']
        self.position_size = config['strategy']['position_size']
    
    def generate_signals(self, predictions):
        """
        Generate buy/sell signals from model predictions.
        
        Args:
            predictions (np.ndarray): Model prediction probabilities
            
        Returns:
            pd.Series: Trading signals (-1=sell, 0=hold, 1=buy)
        """
        signals = pd.Series(index=range(len(predictions)), data=0)
        
        # Buy signal
        signals[predictions >= self.buy_threshold] = 1
        
        # Sell signal
        signals[predictions <= self.sell_threshold] = -1
        
        return signals
    
    def calculate_position_size(self, portfolio_value):
        """
        Calculate position size based on portfolio value.
        
        Args:
            portfolio_value (float): Current portfolio value
            
        Returns:
            float: Position size
        """
        return portfolio_value * self.position_size
