"""
Sales Data Analysis Dashboard

This script loads supermarket sales data from Superstore.csv, cleans and
preprocesses it, calculates key business metrics, and creates a 2x2 dashboard
with four visualizations: monthly sales trend, category performance, regional
sales distribution, and top sub-categories.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_and_prepare_data(data_path: Path) -> pd.DataFrame:
    """Load the sales dataset, clean it, and create derived time features."""
    df = pd.read_csv(data_path, encoding="latin1")

    # Remove duplicate rows to keep the analysis reliable.
    df = df.drop_duplicates().copy()

    # Parse the order date and derive useful time-based columns.
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").dt.strftime("%Y-%m")

    # Handle missing values in a clean, consistent way.
    numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)

    text_columns = [
        "Category",
        "Sub-Category",
        "Region",
        "Ship Mode",
        "Segment",
        "Customer ID",
        "Customer Name",
        "Product Name",
    ]
    for column in text_columns:
        if column in df.columns:
            df[column] = df[column].fillna("Unknown")

    # Fill any remaining missing values for other columns.
    df = df.fillna({
        "Order ID": "Unknown",
        "Country": "Unknown",
        "City": "Unknown",
        "State": "Unknown",
        "Postal Code": 0,
    })

    return df


def print_key_metrics(df: pd.DataFrame) -> None:
    """Print the main KPI values for the dataset."""
    total_sales = round(float(df["Sales"].sum()), 2)
    total_profit = round(float(df["Profit"].sum()), 2)
    total_unique_orders = int(df["Order ID"].nunique())
    average_discount = round(float(df["Discount"].mean()), 4)

    print("Sales Data Analysis KPIs")
    print("-" * 28)
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Total Unique Orders: {total_unique_orders}")
    print(f"Average Discount: {average_discount:.4f}")


def create_dashboard(df: pd.DataFrame, output_path: Path) -> None:
    """Create the requested 2x2 dashboard and save it to disk."""
    monthly_sales = (
        df.loc[df["Month"] != "Unknown"]
        .groupby("Month")["Sales"]
        .sum()
        .sort_index()
    )
    sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    top_subcategories = (
        df.groupby("Sub-Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Monthly sales trend.
    axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker="o", linewidth=2, color="#1f77b4")
    axes[0, 0].set_title("Monthly Sales Trend")
    axes[0, 0].set_xlabel("Month")
    axes[0, 0].set_ylabel("Sales")
    axes[0, 0].tick_params(axis="x", rotation=45)
    axes[0, 0].grid(True, alpha=0.3)

    # Sales by category.
    sales_by_category.plot(kind="bar", ax=axes[0, 1], color="#2ca02c")
    axes[0, 1].set_title("Sales by Category")
    axes[0, 1].set_xlabel("Category")
    axes[0, 1].set_ylabel("Sales")
    axes[0, 1].tick_params(axis="x", rotation=45)

    # Sales by region as a donut chart.
    axes[1, 0].pie(
        sales_by_region.values,
        labels=sales_by_region.index,
        autopct="%1.1f%%",
        startangle=90,
        wedgeprops={"width": 0.35, "edgecolor": "white"},
        colors=plt.cm.Set3(np.linspace(0, 1, len(sales_by_region))),
    )
    axes[1, 0].set_title("Sales Distribution by Region")
    axes[1, 0].axis("equal")

    # Top 5 sub-categories as a horizontal bar chart.
    top_subcategories.plot(kind="barh", ax=axes[1, 1], color="#ff7f0e")
    axes[1, 1].invert_yaxis()
    axes[1, 1].set_title("Top 5 Sub-Categories by Sales")
    axes[1, 1].set_xlabel("Sales")
    axes[1, 1].set_ylabel("Sub-Category")

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()


def main() -> None:
    """Run the full pipeline: load data, print KPIs, and create the dashboard."""
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "Superstore.csv"
    output_path = base_dir / "dashboard_output.png"

    if not data_path.exists():
        raise FileNotFoundError(f"Could not find data file at: {data_path}")

    df = load_and_prepare_data(data_path)
    print_key_metrics(df)
    create_dashboard(df, output_path)


if __name__ == "__main__":
    main()
