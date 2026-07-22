import pandas as pd


class PeerRanking:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def calculate_percentiles(self):

        metrics = [
            "ROE",
            "ROCE",
            "Net Profit Margin",
            "Revenue CAGR 5yr",
            "PAT CAGR 5yr"
        ]

        for metric in metrics:
            if metric in self.df.columns:
                self.df[f"{metric}_Percentile"] = (
                    self.df.groupby("broad_sector")[metric]
                    .rank(pct=True) * 100
                )

        return self.df

    def save_excel(self, output_path):

        self.df.to_excel(output_path, index=False)
        print(f"Peer comparison saved to {output_path}")