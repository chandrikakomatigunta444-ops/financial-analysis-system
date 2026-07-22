import pandas as pd
from pathlib import Path

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data folder
DATA_FOLDER = PROJECT_ROOT / "data"

# File paths
FINANCIAL_DATA = DATA_FOLDER / "financial_ratios.csv"
PEER_GROUPS = DATA_FOLDER / "peer_groups.xlsx"


def load_financial_data():
    """Load financial ratios CSV file."""
    if not FINANCIAL_DATA.exists():
        raise FileNotFoundError(f"File not found: {FINANCIAL_DATA}")

    df = pd.read_csv(FINANCIAL_DATA)
    print("Financial data loaded successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return df


def load_peer_groups():
    """Load peer groups Excel file."""
    if not PEER_GROUPS.exists():
        raise FileNotFoundError(f"File not found: {PEER_GROUPS}")

    df = pd.read_excel(PEER_GROUPS)
    print("Peer groups loaded successfully.")
    print(f"Rows: {len(df)}")

    return df


if __name__ == "__main__":
    try:
        load_financial_data()
    except Exception as e:
        print(e)

    try:
        load_peer_groups()
    except Exception as e:
        print(e)