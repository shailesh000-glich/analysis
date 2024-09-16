# Data Analysis with Python

This project demonstrates a versatile data analysis and visualization workflow using Python libraries such as Pandas, Matplotlib, and Seaborn. It is designed to handle CSV datasets of various kinds and provide users with multiple types of visual insights, such as count plots, bar charts, and pie charts.

## Project Overview

The script analyzes datasets by generating visualizations based on user input. It supports a wide range of graphical representations, including gender-based analysis, age group distribution, state-wise trends, occupation breakdown, and product categories.

## Visualizations

The following visualizations are available in the script:

1. **Count plot for Gender**: Displays the distribution of data by gender.
2. **Bar chart for Gender vs Total Amount**: Compares total values (e.g., sales) by gender.
3. **Count plot for Age Group with Gender as hue**: Shows the distribution of age groups, split by gender.
4. **Total Amount vs Age Group**: Displays total values grouped by age range.
5. **Total number of orders from top 10 states**: Bar chart showing top 10 states by number of occurrences/orders.
6. **Total amount/sales from top 10 states**: Bar chart showing top 10 states by total amount.
7. **Count plot for Marital Status**: Distribution based on marital status.
8. **Total amount by Marital Status and Gender**: Displays total values by marital status, with gender breakdown.
9. **Count plot for Occupation**: Distribution by occupation.
10. **Total amount by Occupation**: Shows total values grouped by occupation.
11. **Count plot for Product Category**: Displays distribution by product category.
12. **Total amount by Product Category**: Shows total values by product category.
13. **Total orders for top 10 most sold products**: Bar chart of top 10 products by number of occurrences.
14. **Age Group Pie Chart**: Pie chart showing the distribution of age groups.
15. **State Pie Chart**: Pie chart showing the distribution of data by state.
16. **Occupation Pie Chart**: Pie chart showing the distribution by occupation.
17. **Product Category Pie Chart**: Pie chart showing distribution by product category.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Data_Analysis_Project.git
   ```

2. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset

This script is adaptable to various datasets in CSV format. You can replace the CSV file with any dataset of your choice, but ensure that the dataset has columns matching the visualizations (e.g., 'Gender', 'Amount', 'Age Group', 'Orders', etc.).

### Example Dataset Columns:
- `Gender`
- `Amount`
- `Age Group`
- `Orders`
- `State`
- `Marital Status`
- `Occupation`
- `Product Category`
- `Product_ID`

Place your dataset in the project directory and ensure the correct file path is provided in the script.

## Usage

1. Ensure the CSV file is in the correct location.
2. Run the script:
   ```bash
   python analysis.py
   ```
3. Enter the number corresponding to the graph you want to visualize (from 1 to 17). The script will generate the appropriate graph based on the dataset and display it.

## Requirements

The project requires the following Python libraries:

- Pandas
- Matplotlib
- Seaborn

You can install these libraries by running:
```bash
pip install pandas matplotlib seaborn
```

## Customization

To adapt the script to different datasets, modify the columns used in the visualizations in the `display_graph()` function. For example, you can change column names like 'Gender', 'Amount', and 'Orders' to match your dataset's specific column structure.

## Contributing

Contributions are welcome! Feel free to fork the project, open an issue, or submit a pull request if you want to improve or expand the functionality.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
