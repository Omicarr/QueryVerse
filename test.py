import unittest
from unittest.mock import patch, MagicMock
from app import get_gemini_response

class TestNaturalLanguageToSQL(unittest.TestCase):

    @patch('app.genai.GenerativeModel')
    def test_list_all_brands(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT * FROM brands;"
        question = "List all brands"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT * FROM brands;")

    @patch('app.genai.GenerativeModel')
    def test_list_all_categories(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT * FROM categories;"
        question = "Show all categories"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT * FROM categories;")

    @patch('app.genai.GenerativeModel')
    def test_find_customer_by_email(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT first_name, last_name FROM customers WHERE email = 'customer@example.com';"
        question = "Find customer with email customer@example.com"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT first_name, last_name FROM customers WHERE email = 'customer@example.com';")

    @patch('app.genai.GenerativeModel')
    def test_pending_orders(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT * FROM orders WHERE order_status = 1;"
        question = "Get all pending orders"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT * FROM orders WHERE order_status = 1;")

    @patch('app.genai.GenerativeModel')
    def test_products_by_brand(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT product_name, list_price FROM products WHERE brand_id = 1;"
        question = "List products and prices for brand 1"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT product_name, list_price FROM products WHERE brand_id = 1;")

    @patch('app.genai.GenerativeModel')
    def test_active_staff_members(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT first_name, last_name FROM staffs WHERE active = 1;"
        question = "Who are the active staff members?"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT first_name, last_name FROM staffs WHERE active = 1;")

    @patch('app.genai.GenerativeModel')
    def test_stock_quantity(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT product_id, quantity FROM stocks WHERE store_id = 1;"
        question = "Check stock quantity for store 1"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT product_id, quantity FROM stocks WHERE store_id = 1;")

    @patch('app.genai.GenerativeModel')
    def test_order_items_for_order(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT product_id, quantity FROM order_items WHERE order_id = 1;"
        question = "Get items for order 1"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT product_id, quantity FROM order_items WHERE order_id = 1;")

    @patch('app.genai.GenerativeModel')
    def test_products_by_year(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT product_name FROM products WHERE model_year = 2023;"
        question = "Show products from the year 2023"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT product_name FROM products WHERE model_year = 2023;")

    @patch('app.genai.GenerativeModel')
    def test_discounted_order_items(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT * FROM order_items WHERE discount > 0;"
        question = "Find all discounted order items"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT * FROM order_items WHERE discount > 0;")

    @patch('app.genai.GenerativeModel')
    def test_customers_with_phone(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT first_name, last_name FROM customers WHERE phone IS NOT NULL;"
        question = "List customers with phone numbers"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT first_name, last_name FROM customers WHERE phone IS NOT NULL;")

    @patch('app.genai.GenerativeModel')
    def test_products_above_price(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT product_name FROM products WHERE list_price > 1000;"
        question = "Show products priced above 1000"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT product_name FROM products WHERE list_price > 1000;")

    @patch('app.genai.GenerativeModel')
    def test_orders_by_customer(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT * FROM orders WHERE customer_id = 1;"
        question = "Get orders for customer 1"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT * FROM orders WHERE customer_id = 1;")

    @patch('app.genai.GenerativeModel')
    def test_staff_email_list(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = "SELECT email FROM staffs;"
        question = "List all staff emails"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "SELECT email FROM staffs;")

    @patch('app.genai.GenerativeModel')
    def test_empty_response_for_invalid_input(self, MockGenerativeModel):
        mock_model = MockGenerativeModel.return_value
        mock_model.generate_content.return_value.text = ""
        question = "Blah blah blah"
        response = get_gemini_response(question, ["Prompt"])
        self.assertEqual(response, "")

if __name__ == '__main__':
    unittest.main()