"""
Utility Helper Functions

Common utility functions used throughout the project
"""

import logging
import pandas as pd
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def get_date_range(start_date, end_date):
    """
    Generate date range.
    
    Args:
        start_date (str): Start date (YYYY-MM-DD)
        end_date (str): End date (YYYY-MM-DD)
        
    Returns:
        list: List of dates
    """
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    return pd.date_range(start=start, end=end, freq='D').tolist()


def format_currency(value):
    """
    Format value as currency.
    
    Args:
        value (float): Value to format
        
    Returns:
        str: Formatted currency string
    """
    return f"${value:,.2f}"


def calculate_percentage_change(start, end):
    """
    Calculate percentage change.
    
    Args:
        start (float): Starting value
        end (float): Ending value
        
    Returns:
        float: Percentage change
    """
    if start == 0:
        return 0
    return ((end - start) / start) * 100
