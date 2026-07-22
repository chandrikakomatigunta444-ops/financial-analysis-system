# Financial Analysis System

A Python-based financial analysis and stock screening system that filters companies based on financial ratios, ranks companies against peers, and exports the results to Excel.

---

## Features

- Financial data loading from CSV
- Configurable stock screener
- Multiple screening filters
- Peer comparison and percentile ranking
- Excel report generation
- Modular project structure
- Easy to extend with new financial metrics

---

## Project Structure

```
Financial-Analysis-System/
│
├── config/
│   └── screener_config.yaml
│
├── data/
│   └── financial_ratios.csv
│
├── output/
│   ├── screener_output.xlsx
│   └── peer_comparison.xlsx
│
├── src/
│   ├── analytics/
│   │   └── peer.py
│   │
│   ├── database/
│   │   └── db.py
│   │
│   ├── screener/
│   │   └── engine.py
│   │
│   ├── utils/
│   │   ├── loader.py
│   │   ├── excel.py
│   │   └── charts.py
│   │
│   └── __init__.py
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python 3.x
- Pandas
- NumPy
- OpenPyXL
- Matplotlib
- PyYAML

---

## Installation

Clone the repository.

```bash
git clone https://github.com/chandrikakomatigunta444-ops/financial-analysis-system.git
```

Move into the project.

```bash
cd financial-analysis-system
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run

```bash
python main.py
```

If everything executes successfully, Excel reports will be created inside the **output/** folder.

---

## Input Dataset

The application reads financial data from

```
data/financial_ratios.csv
```

Example columns:

- Company ID
- Company Name
- Sector
- ROE
- ROCE
- Net Profit Margin
- Debt to Equity
- Revenue CAGR
- PAT CAGR
- PE Ratio
- PB Ratio
- Dividend Yield
- Market Cap
- Interest Coverage
- Asset Turnover

---

## Configuration

Screening conditions can be modified inside

```
config/screener_config.yaml
```

Example:

```yaml
filters:
  ROE: 15
  ROCE: 20
  Debt_to_Equity: 1
```

---

## Output

The system generates:

### Screener Report

```
output/screener_output.xlsx
```

Contains companies that satisfy the screening conditions.

### Peer Comparison Report

```
output/peer_comparison.xlsx
```

Contains peer rankings and percentile analysis.

---

## Future Improvements

- SQLite database integration
- Interactive dashboard
- Radar charts
- Sector-wise comparison
- Stock price integration
- Web application using Streamlit

---

## Author

**Chandrika Komatigunta**

GitHub:

https://github.com/chandrikakomatigunta444-ops

---

## License

This project is developed for educational and portfolio purposes.