# Sales Dashboard

A Python-based data analysis and visualization tool that transforms supermarket sales data into actionable business insights through an interactive 2x2 dashboard.

## Overview

This project loads sales data from a CSV file, performs data cleaning and preprocessing, calculates key business metrics, and generates a professional dashboard with four complementary visualizations:

- **Monthly Sales Trend**: Line chart showing sales performance over time
- **Sales by Category**: Bar chart comparing revenue across product categories
- **Regional Sales Distribution**: Donut chart displaying market share by region
- **Top 5 Sub-Categories**: Horizontal bar chart highlighting best-performing product lines

## Tech Stack

- **Language**: Python 3.x
- **Key Libraries**:
  - `pandas` — Data loading, cleaning, and aggregation
  - `matplotlib` — Dashboard visualization and chart generation
  - `numpy` — Numerical operations for color mapping

## Project Structure

```
Sales-Dashboard/
├── main.py                 # Core data pipeline and visualization logic
├── Superstore.csv          # Sales dataset (2.2 MB)
├── dashboard_output.png    # Generated dashboard visualization
└── README.md               # This file
```

## How It Works

1. **Data Loading** (`load_and_prepare_data`):
   - Reads the Superstore CSV file with Latin-1 encoding
   - Removes duplicate rows for data integrity
   - Parses dates and derives time-based features (Year, Month)
   - Handles missing values across numeric and text columns

2. **Metrics Calculation** (`print_key_metrics`):
   - Computes total sales, profit, order count, and average discount
   - Displays KPIs to console for quick reference

3. **Visualization** (`create_dashboard`):
   - Aggregates sales by time period, category, region, and sub-category
   - Renders a 2x2 subplot grid (15×10 inches, 300 DPI)
   - Saves high-quality PNG output for reports or presentations

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Badr-Rafik/Sales-Dashboard.git
   cd Sales-Dashboard
   ```

2. Install dependencies:
   ```bash
   pip install pandas matplotlib numpy
   ```

3. Verify the data file exists:
   ```bash
   ls -lh Superstore.csv
   ```

## Usage

Run the complete pipeline:

```bash
python main.py
```

### Output

The script will:
1. Print KPIs to the console:
   ```
   Sales Data Analysis KPIs
   ----------------------------
   Total Sales: $2,297,200.86
   Total Profit: $286,397.02
   Total Unique Orders: 5,009
   Average Discount: 0.1563
   ```

2. Generate `dashboard_output.png` — a high-resolution visualization dashboard

## Data Format

The `Superstore.csv` file contains the following columns:
- **Order ID, Customer ID, Customer Name**: Customer and order identifiers
- **Order Date, Ship Date**: Temporal data
- **Ship Mode**: Shipping method (e.g., Standard, Express)
- **Region, State, City, Country**: Geographic information
- **Segment**: Customer segment (e.g., Consumer, Corporate)
- **Category, Sub-Category**: Product classifications
- **Product Name**: Item description
- **Sales, Quantity, Discount, Profit**: Financial metrics

## Customization

You can extend this project by:

- **Modifying the top N sub-categories** — Edit line 93 in `main.py`:
  ```python
  .head(10)  # Instead of .head(5)
  ```

- **Changing the output format** — Modify line 133:
  ```python
  fig.savefig(output_path, format='pdf', dpi=300)  # Save as PDF
  ```

- **Adding filters** — Filter by region, time period, or segment before aggregation:
  ```python
  df_filtered = df[df["Region"] == "West"]
  ```

- **Creating additional charts** — Extend the dashboard to 3×3 or more subplots by adjusting `fig, axes = plt.subplots(3, 3, ...)`

## Sample Output

The generated dashboard includes:
- Color-coded visualizations for easy interpretation
- Grid lines and labels for precise data reading
- Responsive layout that adapts to different screen sizes

See `dashboard_output.png` for a sample output.

## Requirements

- **Python 3.7+**
- **pandas 1.0+**
- **matplotlib 3.0+**
- **numpy 1.18+**

Install all requirements at once:
```bash
pip install -r requirements.txt
```

(If a `requirements.txt` doesn't exist, create one with the versions above.)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError: Could not find data file` | Ensure `Superstore.csv` is in the same directory as `main.py` |
| `UnicodeDecodeError` | The script uses `latin1` encoding; this is already configured |
| `ModuleNotFoundError: No module named 'pandas'` | Run `pip install pandas matplotlib numpy` |
| Dashboard appears blank or misaligned | Check that your display supports matplotlib; try increasing `figsize` |

## Contributing

Contributions are welcome! Feel free to:
- Report issues or bugs
- Suggest new visualizations or metrics
- Optimize data processing performance
- Add support for different data formats

## License

This project is open source and available under the MIT License.

## Contact

For questions or feedback, reach out to [Badr-Rafik](https://github.com/Badr-Rafik).

---

**Last Updated**: July 2026
