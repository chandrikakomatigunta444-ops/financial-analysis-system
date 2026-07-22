from src.screener.engine import ScreenerEngine


def main():
    print("=" * 50)
    print("Financial Analysis System")
    print("=" * 50)

    engine = ScreenerEngine(
        "data/financial_ratios.csv",
        "config/screener_config.yaml"
    )

    result = engine.run()

    print("\nFiltered Companies:\n")

    if result.empty:
        print("No companies matched the filters.")
    else:
        print(result)


if __name__ == "__main__":
    main()