import sqlite3
import pandas as pd

# Connect to SQLite (creates the database if it doesn't exist)
connection = sqlite3.connect("bikes.db")

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# List of your CSV file paths
csv_files = [
    "brands.csv",
    "categories.csv",
    "customers.csv",
    "order_items.csv",
    "orders.csv",
    "products.csv",
    "staffs.csv",
    "stocks.csv",
    "stores.csv"
]

def create_table_from_csv(cursor, table_name, df):
    # Create table query
    columns = df.columns
    column_types = []

    # Inferring column types (this can be customized further based on your actual data)
    for column in columns:
        if df[column].dtype == 'int64':
            column_types.append(f"{column} INTEGER")
        elif df[column].dtype == 'float64':
            column_types.append(f"{column} REAL")
        else:
            column_types.append(f"{column} TEXT")
    
    # Creating the SQL query for creating a table
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_types)});"
    
    cursor.execute(create_table_query)

# Function to insert CSV data into the table
def insert_csv_data(cursor, table_name, df):
    placeholders = ', '.join(['?'] * len(df.columns))
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    
    # Insert data row by row
    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))

# Loop through each CSV file
for csv_file in csv_files:
    # Extract table name from file name (without extension)
    table_name = csv_file.split('.')[0]
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Create a table based on CSV file structure
    create_table_from_csv(cursor, table_name, df)
    
    # Insert the CSV data into the table
    insert_csv_data(cursor, table_name, df)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database 'bikes.db' created and tables populated successfully.")
