"""
Data Loader Module

Handles loading stock market data from various sources (Yahoo Finance, APIs, etc.)
"""

import logging
import pandas as pd
import yfinance as yf
import requests
from datetime import datetime

logger = logging.getLogger(__name__)


class DataLoader:
    """Load stock market data from external sources."""
    
    def __init__(self, config):
        """
        Initialize DataLoader.
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.symbols = config['stock']['symbols']
        self.start_date = config['stock']['start_date']
        self.end_date = config['stock']['end_date']
    
    def fetch_data(self):
        """
        Fetch stock data from Yahoo Finance API.
        
        Returns:
            pd.DataFrame: Combined stock data for all symbols
        """
        try:
            all_data = []
            
            for symbol in self.symbols:
                logger.info(f"Fetching data for {symbol} from {self.start_date} to {self.end_date}")
                
                # Download data using yfinance API
                data = yf.download(
                    symbol,
                    start=self.start_date,
                    end=self.end_date,
                    interval=self.config['stock'].get('interval', '1d'),
                    progress=False
                )
                
                # Reset index and add symbol column
                data.reset_index(inplace=True)
                data['Symbol'] = symbol
                all_data.append(data)
            
            # Combine all data
            combined_df = pd.concat(all_data, ignore_index=True)
            logger.info(f"Successfully fetched data for {len(self.symbols)} symbols. Shape: {combined_df.shape}")
            
            return combined_df
            
        except Exception as e:
            logger.error(f"Error fetching data from Yahoo Finance API: {str(e)}")
            raise
    
    def fetch_from_rest_api(self):
        """
        Fetch stock quotes from Yahoo Finance REST API.
        Direct API endpoint: https://query1.finance.yahoo.com/v7/finance/quote
        
        Returns:
            pd.DataFrame: Stock quote data for all symbols
        """
        try:
            api_url = "https://query1.finance.yahoo.com/v7/finance/quote"
            
            # Format symbols as comma-separated string
            symbols_str = ",".join(self.symbols)
            
            params = {
                "symbols": symbols_str
            }
            
            logger.info(f"Fetching quotes for symbols: {symbols_str} from REST API")
            
            # Make API request
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Parse response
            quotes = data.get('quoteResponse', {}).get('result', [])
            
            if not quotes:
                logger.warning("No quote data returned from API")
                return pd.DataFrame()
            
            # Convert to DataFrame
            df = pd.DataFrame(quotes)
            
            # Select relevant columns
            relevant_columns = ['symbol', 'regularMarketPrice', 'regularMarketChange', 
                              'regularMarketChangePercent', 'marketCap', 'trailingPE', 
                              'epsTrailingTwelveMonths', 'regularMarketDayHigh', 
                              'regularMarketDayLow', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow']
            
            # Filter columns that exist
            existing_columns = [col for col in relevant_columns if col in df.columns]
            df = df[['symbol'] + existing_columns]
            
            # Rename columns
            df.rename(columns={'symbol': 'Symbol', 'regularMarketPrice': 'Price'}, inplace=True)
            
            logger.info(f"Successfully fetched quote data for {len(df)} symbols")
            logger.info(f"Data shape: {df.shape}")
            
            return df
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching data from REST API: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error parsing API response: {str(e)}")
            raise
    
    def load_from_csv(self, filepath):
        """
        Load data from CSV file.
        
        Args:
            filepath (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Loaded data
        """
        return pd.read_csv(filepath)
    
    def save_to_csv(self, data, filepath):
        """
        Save fetched data to CSV file for caching.
        
        Args:
            data (pd.DataFrame): Data to save
            filepath (str): Path where to save the CSV
        """
        try:
            data.to_csv(filepath, index=False)
            logger.info(f"Data saved to {filepath}")
        except Exception as e:
            logger.error(f"Error saving data to CSV: {str(e)}")
            raise
