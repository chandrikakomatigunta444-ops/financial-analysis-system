import pandas as pd
import yaml


class ScreenerEngine:

    def __init__(self, data_file, config_file):
        self.data_file = data_file
        self.config_file = config_file
        self.df = None
        self.config = None

    def load_data(self):
        self.df = pd.read_csv(self.data_file)

    def load_config(self):
        with open(self.config_file, "r") as file:
            self.config = yaml.safe_load(file)

    def apply_filters(self):

        df = self.df.copy()

        filters = self.config["custom_filters"]

        if filters["roe_min"] is not None:
            df = df[df["ROE"] >= filters["roe_min"]]

        if filters["roce_min"] is not None:
            df = df[df["ROCE"] >= filters["roce_min"]]

        if filters["fcf_min"] is not None:
            df = df[df["FCF"] >= filters["fcf_min"]]

        if filters["revenue_cagr_5yr_min"] is not None:
            df = df[df["Revenue_CAGR_5yr"] >= filters["revenue_cagr_5yr_min"]]

        if filters["pat_cagr_5yr_min"] is not None:
            df = df[df["PAT_CAGR_5yr"] >= filters["pat_cagr_5yr_min"]]

        if filters["pe_max"] is not None:
            df = df[df["PE"] <= filters["pe_max"]]

        if filters["pb_max"] is not None:
            df = df[df["PB"] <= filters["pb_max"]]

        if filters["dividend_yield_min"] is not None:
            df = df[df["Dividend_Yield"] >= filters["dividend_yield_min"]]

        if filters["market_cap_min"] is not None:
            df = df[df["Market_Cap"] >= filters["market_cap_min"]]

        if filters["net_profit_min"] is not None:
            df = df[df["Net_Profit"] >= filters["net_profit_min"]]

        if filters["eps_cagr_min"] is not None:
            df = df[df["EPS_CAGR"] >= filters["eps_cagr_min"]]

        if filters["asset_turnover_min"] is not None:
            df = df[df["Asset_Turnover"] >= filters["asset_turnover_min"]]

        if filters["sales_min"] is not None:
            df = df[df["Sales"] >= filters["sales_min"]]

        return df

    def run(self):

        self.load_data()

        self.load_config()

        return self.apply_filters()