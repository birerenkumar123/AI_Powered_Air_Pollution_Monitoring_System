# Gringotts AI Trading 🏦
create by Biren Kumar Nayak

An intelligent stock trading system powered by machine learning and advanced risk management. Built with Python, scikit-learn, XGBoost, and Streamlit.

## 🎯 Project Overview

Gringotts AI Trading is an end-to-end machine learning pipeline for algorithmic stock trading that includes:

- **Data Pipeline**: Fetch and process stock market data
- **Feature Engineering**: Technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands)
- **ML Models**: XGBoost, LightGBM classifiers for buy/sell predictions
- **Risk Management**: Stop-loss, position sizing, drawdown limits
- **Backtesting**: Simulate trading strategies on historical data
- **Interactive Dashboard**: Streamlit app for visualization and real-time predictions

## 📁 Project Structure

```
gringotts-ai-trading/
├── data/                          # Data storage
│   ├── raw/                       # Original market data
│   ├── processed/                 # Cleaned & feature-engineered data
│   └── external/                  # External datasets
├── notebooks/                     # Jupyter notebooks
│   ├── 01_eda.ipynb              # Exploratory data analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_backtesting_analysis.ipynb
├── src/                          # Source code
│   ├── data/                     # Data loading & preprocessing
│   ├── features/                 # Feature engineering
│   ├── models/                   # Model training & prediction
│   ├── strategy/                 # Trading strategy logic
│   ├── risk/                     # Risk management
│   ├── backtesting/              # Backtesting engine
│   └── utils/                    # Utility functions
├── app/                          # Streamlit dashboard
├── tests/                        # Unit tests
├── config/                       # Configuration files
├── models/                       # Trained models (.pkl)
├── reports/                      # Generated reports & figures
└── requirements.txt              # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd gringotts-ai-trading
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Run the full pipeline:
```bash
python main.py
```

#### Launch Streamlit dashboard:
```bash
streamlit run app/app.py
```

#### Run Jupyter notebooks:
```bash
jupyter notebook notebooks/
```

#### Run tests:
```bash
pytest tests/
```

## 📊 Pipeline Stages

1. **Data Collection** (`src/data/loader.py`)
   - Fetch stock data from Yahoo Finance
   - Handle multiple symbols and timeframes

2. **Data Preprocessing** (`src/data/preprocess.py`)
   - Clean missing values
   - Handle outliers
   - Data normalization

3. **Feature Engineering** (`src/features/build_features.py`)
   - Calculate technical indicators
   - Create lagged features
   - Feature scaling

4. **Model Training** (`src/models/train.py`)
   - Train classification models
   - Hyperparameter tuning
   - Cross-validation

5. **Strategy Development** (`src/strategy/strategy.py`)
   - Define buy/sell rules
   - Position management
   - Entry/exit signals

6. **Risk Management** (`src/risk/risk_manager.py`)
   - Stop-loss implementation
   - Position sizing
   - Drawdown monitoring

7. **Backtesting** (`src/backtesting/backtest.py`)
   - Simulate historical trading
   - Calculate performance metrics
   - Risk analysis

## ⚙️ Configuration

Edit `config/config.yaml` to customize:
- Stock symbols and date range
- Technical indicators
- Model parameters
- Risk management thresholds
- Trading strategy rules

## 📈 Key Metrics

- **Accuracy**: Model prediction accuracy
- **Sharpe Ratio**: Risk-adjusted returns
- **Max Drawdown**: Maximum peak-to-trough decline
- **Win Rate**: % of profitable trades
- **ROI**: Return on investment

## 🛡️ Risk Management Features

- **Stop Loss**: Automatic exit at loss threshold
- **Take Profit**: Lock in gains at target price
- **Position Sizing**: Limit capital per trade
- **Max Drawdown**: Maximum portfolio decline limit
- **Max Positions**: Limit concurrent open trades

## 🔧 Development

### Code Structure
- **Modular design**: Each component is independent
- **Configuration-driven**: Easy to adjust parameters
- **Type hints**: Better code documentation
- **Error handling**: Robust exception management

### Testing
```bash
pytest tests/ -v
```

## 📝 Documentation

See individual module docstrings for detailed API documentation.

## ⚠️ Disclaimer

This is an educational project. Algorithmic trading involves significant risk. Past performance does not guarantee future results. Always perform thorough backtesting and risk assessment before trading with real capital.

## 📄 License

MIT License - See LICENSE file for details

## 👨‍💻 Contributing

Contributions are welcome! Please follow PEP 8 style guide and add tests for new features.

## 📧 Contact

For questions or suggestions, please open an issue or contact the development team.

---

**Built with ❤️ for algorithmic traders**
