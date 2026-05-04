"""
Risk Management Module

Handles risk management and position management
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)


class RiskManager:
    """Manage trading risks and positions."""
    
    def __init__(self, config):
        """
        Initialize RiskManager.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.stop_loss_pct = config['risk']['stop_loss_pct']
        self.take_profit_pct = config['risk']['take_profit_pct']
        self.max_drawdown_pct = config['risk']['max_drawdown_pct']
        self.max_positions = config['risk']['max_positions']
    
    def calculate_stop_loss(self, entry_price):
        """
        Calculate stop-loss price.
        
        Args:
            entry_price (float): Entry price
            
        Returns:
            float: Stop-loss price
        """
        return entry_price * (1 - self.stop_loss_pct)
    
    def calculate_take_profit(self, entry_price):
        """
        Calculate take-profit price.
        
        Args:
            entry_price (float): Entry price
            
        Returns:
            float: Take-profit price
        """
        return entry_price * (1 + self.take_profit_pct)
    
    def check_max_drawdown(self, current_value, peak_value):
        """
        Check if maximum drawdown limit is exceeded.
        
        Args:
            current_value (float): Current portfolio value
            peak_value (float): Peak portfolio value
            
        Returns:
            bool: True if drawdown exceeded, False otherwise
        """
        drawdown = (peak_value - current_value) / peak_value
        return drawdown > self.max_drawdown_pct
    
    def can_open_position(self, open_positions):
        """
        Check if new position can be opened.
        
        Args:
            open_positions (int): Number of open positions
            
        Returns:
            bool: True if position can be opened, False otherwise
        """
        return open_positions < self.max_positions
