# Sales Data Analysis Using Python

## 1. Project Overview

Sales Data Analysis is a beginner-friendly Python project developed using the Pandas library.

The main purpose of this project is to analyze sales data, calculate total revenue, identify the best-selling product, and generate a formatted sales report.

## 2. Objectives

- Analyze sales data using Python.
- Load CSV files using Pandas.
- Handle missing values.
- Remove duplicate records.
- Calculate total sales and revenue.
- Identify the best-selling product.
- Generate a sales analysis report.

## 3. Technologies Used

- Python 3.14.0
- Pandas Library
- CSV Dataset
- Visual Studio Code
- Markdown

## 4. Project Structure

```text
Sales_Analysis_Project/
│
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
├── cleaned_sales_data.csv
├── requirements.txt
└── README.md
```

## 5. Dataset Description

The project uses a CSV file named `sales_data.csv`.

Dataset columns:

| Column Name | Description |
|---|---|
| OrderID | Unique order identification |
| OrderDate | Date of order |
| Product | Product name |
| Category | Product category |
| Quantity | Number of products sold |
| Price | Product price |
| Customer | Customer name |

## 6. Installation Requirements

Install Python on your computer.

Install the Pandas library using:

```bash
py -m pip install pandas
```

## 7. How to Run the Project

**Step 1:** Download or clone the project repository.

**Step 2:** Open the project folder in VS Code.

**Step 3:** Open the terminal.

**Step 4:** Install required libraries.

```bash
py -m pip install -r requirements.txt
```

**Step 5:** Run the Python program.

```bash
py sales_analysis.py
```

## 8. Data Cleaning

The project performs the following data-cleaning operations:

- Removes duplicate records.
- Removes extra spaces from text columns.
- Handles missing customer names.
- Handles missing category values.
- Converts quantity and price into numeric values.
- Converts order dates into date format.
- Removes rows with invalid essential data.

## 9. Analysis Metrics

The project calculates the following metrics:

1. Total Revenue
2. Total Orders
3. Total Quantity Sold
4. Average Order Value
5. Best-Selling Product
6. Highest Revenue Product

## 10. Expected Results

| Metric | Result |
|---|---:|
| Total Revenue | ₹158,000 |
| Total Orders | 5 |
| Total Quantity Sold | 13 |
| Average Order Value | ₹31,600 |
| Best-Selling Product | Mouse |
| Quantity Sold | 7 |
| Highest Revenue Product | Laptop |

## 11. Output Files

After successful execution, the program generates:

- `analysis_report.md` – Formatted sales analysis report.
- `cleaned_sales_data.csv` – Cleaned sales dataset.

## 12. Key Features

- CSV data loading.
- Data exploration.
- Data cleaning.
- Sales calculations.
- Product-wise analysis.
- Automatic report generation.
- Clean and readable output.

## 13. Conclusion

This project demonstrates how Python and Pandas can be used for basic sales data analysis.

It helps identify total revenue, sales performance, best-selling products, and important business insights.

The project also provides practical experience in data loading, data cleaning, data manipulation, and report generation.

## 14. Author

**Project Name:** Sales Data Analysis Using Python

**Language:** Python

**Library:** Pandas

**Project Level:** Beginner

**Purpose:** Python Data Analysis Practice and Academic Submission
