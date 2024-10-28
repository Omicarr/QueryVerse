from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import pandas as pd
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the SQL database

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        df = pd.read_sql_query(sql, conn)
        return df
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None  # Return None in case of error
    finally:
        conn.close()

# Define your prompt
prompt = [
    """
    You are an expert SQL query generator for a bike database named BIKES_DB. The database consists of the following tables:

    **Table: brands**
    - **Description:** This table stores information about bike brands.
    - **Columns:**
      - `brand_id`: Unique identifier for each brand (Primary Key)
      - `brand_name`: Name of the brand (Not Null)
    - **Example Query:** 
      - **Description:** List all brands available in the database.
      - **SQL Code:** 
        `SELECT * FROM brands;`

    **Table: categories**
    - **Description:** This table stores categories of bikes.
    - **Columns:**
      - `category_id`: Unique identifier for each category (Primary Key)
      - `category_name`: Name of the category (Not Null)
    - **Example Query:** 
      - **Description:** Retrieve the category name for children's bicycles.
      - **SQL Code:** 
        `SELECT * FROM categories WHERE category_name = 'children bicycles';`

    **Table: customers**
    - **Description:** This table stores customer information.
    - **Columns:**
      - `customer_id`: Unique identifier for each customer (Primary Key)
      - `first_name`: Customer's first name (Not Null)
      - `last_name`: Customer's last name (Not Null)
      - `phone`: Customer's phone number
      - `email`: Customer's email address
    - **Example Query:** 
      - **Description:** Find the first and last names of customers with a specific email address.
      - **SQL Code:** 
        `SELECT first_name, last_name FROM customers WHERE email = 'customer@example.com';`

    **Table: orders**
    - **Description:** This table stores information about customer orders.
    - **Columns:**
      - `order_id`: Unique identifier for each order (Primary Key)
      - `customer_id`: Identifier of the customer who placed the order (Foreign Key)
      - `order_status`: Status of the order (Not Null)
      - `order_date`: Date when the order was placed (Not Null)
    - **Example Query:** 
      - **Description:** Retrieve all orders that are currently pending.
      - **SQL Code:** 
        `SELECT * FROM orders WHERE order_status = 1;`

    **Table: products**
    - **Description:** This table stores information about products.
    - **Columns:**
      - `product_id`: Unique identifier for each product (Primary Key)
      - `product_name`: Name of the product (Not Null)
      - `brand_id`: Identifier of the brand (Foreign Key)
      - `category_id`: Identifier of the category (Foreign Key)
      - `model_year`: Year of the model (Not Null)
      - `list_price`: Price of the product (Not Null)
    - **Example Query:** 
      - **Description:** List product names and prices for a specific brand.
      - **SQL Code:** 
        `SELECT product_name, list_price FROM products WHERE brand_id = 1;`

    **Table: staffs**
    - **Description:** This table stores information about staff members.
    - **Columns:**
      - `staff_id`: Unique identifier for each staff member (Primary Key)
      - `first_name`: Staff member's first name (Not Null)
      - `last_name`: Staff member's last name (Not Null)
      - `email`: Staff member's email (Not Null)
      - `phone`: Staff member's phone number
    - **Example Query:** 
      - **Description:** Retrieve names of active staff members.
      - **SQL Code:** 
        `SELECT first_name, last_name FROM staffs WHERE active = 1;`

    **Table: stocks**
    - **Description:** This table stores inventory information for products in each store.
    - **Columns:**
      - `store_id`: Identifier of the store (Foreign Key)
      - `product_id`: Identifier of the product (Foreign Key)
      - `quantity`: Quantity of the product in stock (Not Null)
    - **Example Query:** 
      - **Description:** Check the quantity of a specific product in a particular store.
      - **SQL Code:** 
        `SELECT product_id, quantity FROM stocks WHERE store_id = 1;`

    **Table: order_items**
    - **Description:** This table stores details of the items in each order.
    - **Columns:**
      - `order_id`: Identifier of the associated order (Foreign Key)
      - `item_id`: Unique identifier for each line item (Primary Key)
      - `product_id`: Identifier of the product (Foreign Key)
      - `quantity`: Quantity of the product ordered (Not Null)
      - `list_price`: Price of the product at the time of order (Not Null)
      - `discount`: Discount applied to the product (Default is 0)
    - **Example Query:** 
      - **Description:** Retrieve product IDs and quantities for a specific order.
      - **SQL Code:** 
        `SELECT product_id, quantity FROM order_items WHERE order_id = 1;`

    Make sure that the generated SQL queries are syntactically correct and do not include any unnecessary characters.
    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

# Input for SQL query
question = st.text_input("Input your SQL query: ", key="input")

# Submit button
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    if response:
        # Strip unnecessary characters from the response
        cleaned_response = response.replace("```sql", "").replace("```", "").strip()
        st.write("Generated SQL Query:")
        st.code(cleaned_response)  # Display the SQL query nicely formatted

        # Check if the SQL query is valid
        if cleaned_response:
            try:
                data = read_sql_query(cleaned_response, "bikes.db")
                st.subheader("The Response is:")
                if data is not None and not data.empty:
                    st.write(data)  # Display the DataFrame nicely
                else:
                    st.write("No data found or invalid query.")
            except Exception as e:
                st.error(f"An error occurred while executing the query: {e}")
        else:
            st.write("Generated query is empty.")
    else:
        st.write("No response generated.")
