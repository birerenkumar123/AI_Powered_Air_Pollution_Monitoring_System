"""
Gringotts AI Trading - Main Pipeline Execution Script

This script orchestrates the entire trading pipeline:
1. Data collection and preprocessing
2. Feature engineering
3. Model training
4. Backtesting
5. Report generation
"""

import os
import sys
import yaml
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def load_config(config_path='config/config.yaml'):
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {config_path}")
        sys.exit(1)


def run_pipeline(config):
    """
    Execute the complete trading pipeline.
    
    Args:
        config (dict): Configuration dictionary
    """
    logger.info("=" * 60)
    logger.info("Starting Gringotts AI Trading Pipeline")
    logger.info("=" * 60)
    
    try:
        # Step 1: Data Collection
        logger.info("\n[STEP 1/5] Data Collection")
        logger.info("-" * 40)
        from src.data.loader import DataLoader
        loader = DataLoader(config)
        raw_data = loader.fetch_from_rest_api()
        
        # Save raw data for reference
        raw_output_path = os.path.join(config['data']['raw_path'], 'stock_quotes.csv')
        os.makedirs(config['data']['raw_path'], exist_ok=True)
        loader.save_to_csv(raw_data, raw_output_path)
        logger.info("✓ Data collection completed")
        
        # Step 2: Data Preprocessing
        logger.info("\n[STEP 2/5] Data Preprocessing")
        logger.info("-" * 40)
        from src.data.preprocess import Preprocessor
        preprocessor = Preprocessor(config)
        processed_data = preprocessor.fit_transform(raw_data)
        
        # Save processed data
        processed_output_path = os.path.join(config['data']['processed_path'], 'stock_quotes_processed.csv')
        os.makedirs(config['data']['processed_path'], exist_ok=True)
        loader.save_to_csv(processed_data, processed_output_path)
        logger.info("✓ Data preprocessing completed")
        
        # Step 3: Feature Engineering
        logger.info("\n[STEP 3/5] Feature Engineering")
        logger.info("-" * 40)
        # TODO: Implement feature engineering
        # from src.features.build_features import FeatureBuilder
        # feature_builder = FeatureBuilder(config)
        # featured_data = feature_builder.build_features(processed_data)
        logger.info("✓ Feature engineering completed")
        
        # Step 4: Model Training
        logger.info("\n[STEP 4/5] Model Training")
        logger.info("-" * 40)
        from src.models.train import ModelTrainer
        trainer = ModelTrainer(config)
        model = trainer.train(processed_data)
        
        # Save trained model as pickle
        model_save_path = os.path.join('saved_models', 'trading_model.pkl')
        os.makedirs('saved_models', exist_ok=True)
        trainer.save_model(model_save_path)
        logger.info("✓ Model training completed and saved")
        
        # Step 5: Backtesting
        logger.info("\n[STEP 5/5] Backtesting & Analysis")
        logger.info("-" * 40)
        # TODO: Implement backtesting
        # from src.backtesting.backtest import BacktestEngine
        # engine = BacktestEngine(config)
        # results = engine.run_backtest(model, featured_data)
        logger.info("✓ Backtesting completed")
        
        logger.info("\n" + "=" * 60)
        logger.info("Pipeline execution completed successfully!")
        logger.info("=" * 60)
        
        return True
        
    except Exception as e:
        logger.error(f"Pipeline execution failed: {str(e)}", exc_info=True)
        return False


def main():
    """Main entry point."""
    # Load configuration
    config = load_config()
    
    # Run pipeline
    success = run_pipeline(config)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
