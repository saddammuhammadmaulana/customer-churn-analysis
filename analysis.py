import pandas as pd
def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)
print("Data loading function created.")
