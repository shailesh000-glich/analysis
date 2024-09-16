import pandas as pd
import matplotlib.pyplot as plt
# visualizing data

import seaborn as sns
# import csv file
df = pd.read_csv('Python_Diwali_Sales_Analysis-main/Diwali Sales Data.csv', encoding='unicode_escape')
df.shape



df[['Age', 'Orders', 'Amount']].describe()
def display_graph(graph_number):
    if graph_number == 1:
        # Plotting count plot for Gender
        ax = sns.countplot(x='Gender', data=df)
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.show()
    elif graph_number == 2:
        # Plotting bar chart for Gender vs Total Amount
        sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
        sns.barplot(x='Gender', y='Amount', data=sales_gen)
        plt.show()
    elif graph_number == 3:
        # Plotting count plot for Age Group with Gender as hue
        ax = sns.countplot(data=df, x='Age Group', hue='Gender')
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.show()
    elif graph_number == 4:
        # Total Amount vs Age Group
        sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
        sns.barplot(x='Age Group', y='Amount', data=sales_age)
        plt.show()
    elif graph_number == 5:
        # Total number of orders from top 10 states
        sales_state_orders = df.groupby(['State'], as_index=False)['Orders'].sum().nlargest(10, 'Orders')
        sns.barplot(x='State', y='Orders', data=sales_state_orders)
        plt.show()
    elif graph_number == 6:
        # Total amount/sales from top 10 states
        sales_state_amount = df.groupby(['State'], as_index=False)['Amount'].sum().nlargest(10, 'Amount')
        sns.barplot(x='State', y='Amount', data=sales_state_amount)
        plt.show()
    elif graph_number == 7:
        # Count plot for Marital Status
        ax = sns.countplot(data=df, x='Marital_Status')
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.show()
    elif graph_number == 8:
        # Total amount by Marital Status and Gender
        sales_marital_gender = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum()
        sns.barplot(x='Marital_Status', y='Amount', hue='Gender', data=sales_marital_gender)
        plt.show()
    elif graph_number == 9:
        # Count plot for Occupation
        ax = sns.countplot(data=df, x='Occupation')
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.show()
    elif graph_number == 10:
        # Total amount by Occupation
        sales_occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum()
        sns.barplot(x='Occupation', y='Amount', data=sales_occupation)
        plt.show()
    elif graph_number == 11:
        # Count plot for Product Category
        ax = sns.countplot(data=df, x='Product_Category')
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.show()
    elif graph_number == 12:
        # Total amount by Product Category
        sales_product_category = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().nlargest(10, 'Amount')
        sns.barplot(x='Product_Category', y='Amount', data=sales_product_category)
        plt.show()
    elif graph_number == 13:
        # Total orders for top 10 most sold products
        fig, ax = plt.subplots(figsize=(12, 7))
        df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
        plt.show()
    elif graph_number == 14:
        # grouped_data = df.groupby(['Gender', 'Age Group']).size().reset_index(name='count')
        grouped_data = df.groupby('Age Group').size().reset_index(name='count')
        labels = grouped_data['Age Group']
        sizes = grouped_data['count']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')

        # Add this block to add a comment box
        comment = "Age Group"
        plt.text(0.5, 1.05, comment, ha='center', va='bottom', transform=plt.gca().transAxes)

        plt.show()
    elif graph_number == 15:
        # grouped_data = df.groupby(['Gender', 'Age Group']).size().reset_index(name='count')
        grouped_data = df.groupby('State').size().reset_index(name='count')
        labels = grouped_data['State']
        sizes = grouped_data['count']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')

        # Add this block to add a comment box
        comment = "State"
        plt.text(0.5, 1.05, comment, ha='center', va='bottom', transform=plt.gca().transAxes)

        plt.show()
    elif graph_number == 16:
        # grouped_data = df.groupby(['Gender', 'Age Group']).size().reset_index(name='count')
        grouped_data = df.groupby('Occupation').size().reset_index(name='count')
        labels = grouped_data['Occupation']
        sizes = grouped_data['count']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')

        # Add this block to add a comment box
        comment = "Occupation"
        plt.text(0.5, 1.05, comment, ha='center', va='bottom', transform=plt.gca().transAxes)

        plt.show()
    elif graph_number == 17:
        # grouped_data = df.groupby(['Gender', 'Age Group']).size().reset_index(name='count')
        grouped_data = df.groupby('Product_Category').size().reset_index(name='count')
        labels = grouped_data['Product_Category']
        sizes = grouped_data['count']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')

        # Add this block to add a comment box
        comment = "Product_Category"
        plt.text(0.5, 1.05, comment, ha='center', va='bottom', transform=plt.gca().transAxes)

        plt.show()
    else:
        print("Invalid input. Please enter a number between 1 and 2.")

    # Printing the corresponding graph for each number

while True:
    
    print("Graph Number -> Graph")
    print("1 -> Count plot for Gender")
    print("2 -> Bar chart for Gender vs Total Amount")
    print("3 -> Count plot for Age Group with Gender as hue")
    print("4 -> Total Amount vs Age Group")
    print("5 -> Total number of orders from top 10 states")
    print("6 -> Total amount/sales from top 10 states")
    print("7 -> Count plot for Marital Status")
    print("8 -> Total amount by Marital Status and Gender")
    print("9 -> Count plot for Occupation")
    print("10 -> Total amount by Occupation")
    print("11 -> Count plot for Product Category")
    print("12 -> Total amount by Product Category")
    print("13 -> Total orders for top 10 most sold products")
    print("14 -> Age Group  Pie Chart")
    print("15 -> State  Pie Chart")
    print("16 -> Occupation  Pie Chart")
    print("17 -> Product_Category  Pie Chart")



        # Taking user input
    graph_number = int(input("Enter the number of the graph you want to display (1-17): "))
    display_graph(graph_number)
