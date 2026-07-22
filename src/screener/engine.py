import pandas as pd
import yaml


class ScreenerEngine:

    def __init__(self, data_file, config_file):
        self.data_file = data_file
        self.config_file = config_file
        self.df = None
        self.config = None

    def load_data(self):
        """Load financial ratios CSV."""
        self.df = pd.read_csv(self.data_file)

    def load_config(self):
        """Load YAML configuration."""
        with open(self.config_file, "r") as file:
            self.config = yaml.safe_load(file)

    def apply_filters(self):
        """Apply filters from YAML configuration."""

        filters = self.config["custom_filters"]

        filtered = self.df.copy()

        # ROE Filter
        if filters.get("roe_min") is not None:
            filtered = filtered[
                filtered["ROE"] >= filters["roe_min"]
            ]

        # Debt to Equity Filter
        if filters.get("de_max") is not None:
            filtered = filtered[
                (filtered["Debt_to_Equity"] <= filters["de_max"])
                | (filtered["broad_sector"] == "Financials")
            ]

        # Free Cash Flow Filter
        if filters.get("fcf_min") is not None:
            filtered = filtered[
                filtered["FCF"] >= filters["fcf_min"]
            ]

        return filtered

    def run(self):
        self.load_data()
        self.load_config()

        filtered = self.apply_filters()

        return filtered