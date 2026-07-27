# Sales Dashboard

A Python tool that analyzes supermarket sales data and generates an interactive 2x2 dashboard with key business insights.

## Overview

This project loads CSV sales data, performs cleaning and preprocessing, and generates a professional dashboard with four complementary visualizations:

- **Monthly Sales Trend** — Line chart of sales over time
- **Sales by Category** — Bar chart comparing revenue by product category
- **Regional Distribution** — Donut chart showing market share by region
- **Top 5 Sub-Categories** — Horizontal bar chart of best-performing products

## Tech Stack

- **Python 3.7+**
- **Libraries**: pandas, matplotlib, numpy

## Project Structure

```
Sales-Dashboard/
├── main.py                 # Core pipeline and visualization logic
├── Superstore.csv          # Sales dataset (2.2 MB)
├── dashboard_output.png    # Generated visualization
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Badr-Rafik/Sales-Dashboard.git
   cd Sales-Dashboard
   ```

2. Install dependencies:
   ```bash
   pip install pandas matplotlib numpy
   ```

## Usage

```bash
python main.py
```

This will print KPIs to the console and generate `dashboard_output.png`.

## Data Format

The `Superstore.csv` file includes columns for:
- Customer info: Order ID, Customer ID, Customer Name
- Dates: Order Date, Ship Date
- Location: Region, State, City, Country
- Product: Category, Sub-Category, Product Name
- Metrics: Sales, Quantity, Discount, Profit

## Customization

- Change top N sub-categories: Edit `.head(5)` on line 93
- Modify output format: Change `savefig()` parameters on line 133
- Filter data: Add `df = df[df["Region"] == "West"]` before aggregation
- Extend dashboard: Change `plt.subplots(2, 2)` to larger grid

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError` | Ensure `Superstore.csv` is in the project directory |
| `ModuleNotFoundError` | Run `pip install pandas matplotlib numpy` |
| Blank dashboard | Check display support; try increasing `figsize` |

## Contributing

Contributions welcome! Feel free to report issues, suggest visualizations, or optimize performance.

## License

MIT License — See LICENSE file for details.

## Contact

Questions? Reach out to [Badr-Rafik](https://github.com/Badr-Rafik).
