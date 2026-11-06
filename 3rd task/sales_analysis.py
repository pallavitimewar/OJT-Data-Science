
# Sales Data Analysis Project
# Import pandas library
import pandas as pd

# Step 1: Load CSV dataset
df = pd.read_csv("sales_data.csv")

print("SALES DATA ANALYSIS")
print("=" * 40)

# Step 2: Explore the dataset
print("\nOriginal Dataset:")
print(df)

print("\nDataset Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)

# Step 3: Clean the data

# Remove duplicate records
df = df.drop_duplicates()

# Remove extra spaces from text columns
for column in ["Product", "Category", "Customer"]:
    df[column] = df[column].astype("string").str.strip()

# Convert numeric columns into numbers
df["Quantity"] = pd.to_numeric(
    df["Quantity"], errors="coerce"
)
df["Price"] = pd.to_numeric(
    df["Price"], errors="coerce"
)

# Remove rows with missing essential values
df = df.dropna(
    subset=["Product", "Quantity", "Price"]
)

# Handle missing values in other columns
df["Category"] = df["Category"].fillna("Unknown")
df["Customer"] = df["Customer"].fillna("Unknown")

# Convert OrderDate into date format
df["OrderDate"] = pd.to_datetime(
    df["OrderDate"], errors="coerce"
)

# Remove rows with invalid dates
df = df.dropna(subset=["OrderDate"])

# Step 4: Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Step 5: Calculate different metrics
total_revenue = df["Total_Sales"].sum()
total_orders = df["OrderID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_revenue / total_orders

# Step 6: Find best-selling product by quantity
product_sales = df.groupby("Product")["Quantity"].sum()

best_product = product_sales.idxmax()
best_quantity = product_sales.max()

# Find highest revenue product
product_revenue = df.groupby("Product")["Total_Sales"].sum()

top_revenue_product = product_revenue.idxmax()
top_revenue = product_revenue.max()

# Step 7: Display analysis results
print("\nSALES ANALYSIS RESULTS")
print("=" * 40)

print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Order Value: Rs. {average_order_value:,.2f}")

print(f"Best-Selling Product: {best_product}")
print(f"Quantity Sold: {best_quantity}")

print(f"Highest Revenue Product: {top_revenue_product}")
print(f"Product Revenue: Rs. {top_revenue:,.2f}")

# Step 8: Create a clean formatted report
report = f"""
# SALES DATA ANALYSIS REPORT

## 1. Project Overview
This project analyzes sales data using Python and Pandas.

## 2. Dataset Information
- Total Records After Cleaning: {len(df)}
- Total Unique Orders: {total_orders}
- Total Products: {df['Product'].nunique()}

## 3. Sales Metrics
- Total Revenue: Rs. {total_revenue:,.2f}
- Total Orders: {total_orders}
- Total Quantity Sold: {total_quantity}
- Average Order Value: Rs. {average_order_value:,.2f}

## 4. Best-Selling Product
- Product: {best_product}
- Quantity Sold: {best_quantity}

## 5. Highest Revenue Product
- Product: {top_revenue_product}
- Revenue: Rs. {top_revenue:,.2f}

## 6. Product-wise Sales

{product_sales.to_string()}

## 7. Product-wise Revenue

{product_revenue.to_string()}

## 8. Data Cleaning
- Removed duplicate records.
- Removed extra spaces.
- Handled missing values.
- Converted numeric columns.
- Converted dates into date format.

## 9. Conclusion
The total revenue generated was Rs. {total_revenue:,.2f}.
The best-selling product was {best_product}.
It sold {best_quantity} units.

The analysis helps understand sales performance
and identify important business insights.
"""

# Save report into Markdown file
with open("analysis_report.md", "w", encoding="utf-8") as file:
    file.write(report)

# Step 9: Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nReport generated successfully!")
print("File Name: analysis_report.md")
print("Cleaned data saved successfully!")
