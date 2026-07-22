import pandas as pd
import yaml
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_FILE = PROJECT_ROOT / "config" / "screener_config.yaml"


class ScreenerEngine:

    def __init__(self):

        with open(CONFIG_FILE, "r") as file:
            self.config = yaml.safe_load(file)

    def show_presets(self):

        print("\nAvailable Screeners\n")

        for preset in self.config["presets"]:

            print("-", preset)


if __name__ == "__main__":

    engine = ScreenerEngine()

    engine.show_presets()