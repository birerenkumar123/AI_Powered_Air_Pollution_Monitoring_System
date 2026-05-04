"""
Streamlit Dashboard Application

Interactive dashboard for the Gringotts AI Trading system
"""

import streamlit as st
import pandas as pd
import logging
import pickle
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logger = logging.getLogger(__name__)


def main():
    """Main Streamlit app."""
    
    # Configure page
    st.set_page_config(
        page_title="Gringotts AI Trading",
        page_icon="🏦",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Title
    st.title("🏦 Gringotts AI Trading Dashboard")
    st.markdown("*Intelligent algorithmic trading powered by machine learning*")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Stock selection
        symbol = st.selectbox(
            "Select Stock Symbol",
            ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
        )
        
        # Date range
        date_range = st.date_input(
            "Select Date Range",
            value=[pd.Timestamp("2023-01-01"), pd.Timestamp("2024-12-31")],
            max_value=pd.Timestamp.now()
        )
        
        # Model selection
        model_type = st.selectbox(
            "Model Type",
            ["XGBoost", "LightGBM", "Random Forest"]
        )
        
        # Load/Train Model section
        st.divider()
        st.subheader("🤖 Model Management")
        
        # Get correct model path
        app_dir = os.path.dirname(__file__)
        project_root = os.path.dirname(app_dir)
        model_path = os.path.join(project_root, "saved_models", "trading_model.pkl")
        model_exists = os.path.exists(model_path)
        
        if model_exists:
            st.info("✅ Trained model found")
            if st.button("Load Model"):
                try:
                    with open(model_path, 'rb') as f:
                        loaded_model = pickle.load(f)
                    st.success("Model loaded successfully!")
                    st.session_state.model = loaded_model
                except Exception as e:
                    st.error(f"Error loading model: {str(e)}")
        else:
            st.warning("❌ No trained model found")
            st.info("Run main.py to train and save the model first")
    
    # Main content
    tabs = st.tabs(["Dashboard", "Backtest Results", "Predictions", "Settings"])
    
    with tabs[0]:
        st.header("📊 Dashboard")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Portfolio Value", "$100,000", "+5.2%")
        with col2:
            st.metric("Sharpe Ratio", "1.45", "+0.15")
        with col3:
            st.metric("Win Rate", "62.5%", "+2.1%")
        with col4:
            st.metric("Max Drawdown", "-8.3%", "−1.2%")
        
        st.subheader("Portfolio Performance")
        # TODO: Add actual chart
        st.info("Portfolio performance chart will be displayed here")
    
    with tabs[1]:
        st.header("📈 Backtest Results")
        st.info("Backtest results will be displayed here")
    
    with tabs[2]:
        st.header("🔮 Current Predictions")
        st.info("Current predictions will be displayed here")
    
    with tabs[3]:
        st.header("⚙️ Settings")
        st.info("Configuration settings will be displayed here")


if __name__ == '__main__':
    main()
