import os
import pandas as pd
import yaml


class ScreenerEngine:
    def __init__(self, data_path, config_path):
        self.data_path = data_path
        self.config_path = config_path
        self.data = None
        self.filtered_data = None
        self.config = {}

        self.load_data()
        self.load_config()

    def load_data(self):
        """Load financial data from CSV."""
        self.data = pd.read_csv(self.data_path)

    def load_config(self):
        """Load YAML configuration if available."""
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as file:
                self.config = yaml.safe_load(file) or {}
        else:
            self.config = {}

    def calculate_quality_score(self):
        """Calculate a composite quality score."""
        score = pd.Series(0, index=self.data.index)

        metrics = [
            "ROE",
            "ROCE",
            "Net Profit Margin",
            "Revenue CAGR 5yr",
            "PAT CAGR 5yr",
            "Dividend Yield",
            "Interest Coverage"
        ]

        for metric in metrics:
            if metric in self.data.columns:
                score += self.data[metric].rank(pct=True) * 100

        self.data["Quality Score"] = score / len(metrics)

    def apply_filters(self):
        """Apply basic financial filters."""
        df = self.data.copy()

        if "ROE" in df.columns:
            df = df[df["ROE"] >= 15]

        if "ROCE" in df.columns:
            df = df[df["ROCE"] >= 15]

        if "Debt_to_Equity" in df.columns:
            df = df[df["Debt_to_Equity"] <= 1]

        self.filtered_data = df.sort_values(
            by="Quality Score",
            ascending=False
        )

    def run(self):
        """Run complete screener."""
        self.calculate_quality_score()
        self.apply_filters()

    def save_results(self, output_path):
        """Save screener results."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if self.filtered_data is None:
            self.run()

        self.filtered_data.to_excel(output_path, index=False)

        print(f"Results saved to {output_path}")