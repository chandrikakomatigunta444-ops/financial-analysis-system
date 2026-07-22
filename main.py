from src.screener.engine import ScreenerEngine
from src.analytics.peer import PeerRanking


def main():
    print("=" * 50)
    print("Financial Analysis System")
    print("=" * 50)

    engine = ScreenerEngine(
        "data/financial_ratios.csv",
        "config/screener_config.yaml"
    )

    engine.run()

    engine.save_results("output/screener_output.xlsx")

    print("Screener report generated.")

    peer = PeerRanking(engine.filtered_data)

    peer.calculate_percentiles()

    peer.save_excel("output/peer_comparison.xlsx")

    print("Peer comparison generated.")

    print("Project completed successfully!")


if __name__ == "__main__":
    main()