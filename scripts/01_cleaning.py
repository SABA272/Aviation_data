import pandas as pd
import numpy as np
import os

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
RAW_DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'raw', 'flight_data_2018_2024.csv')
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, 'data', 'processed', 'cleaned_data.csv')

df = pd.read_csv(RAW_DATA_PATH, low_memory=False)