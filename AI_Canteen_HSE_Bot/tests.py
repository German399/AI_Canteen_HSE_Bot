import os.path
import unittest

from config import API_TOKEN, kb, kbi

class TestMethods(unittest.TestCase):
    def test_api_token(self):
        self.assertTrue(API_TOKEN)

    def test_exist_menu(self):
        self.assertTrue(os.path.exists('menu'))

    def test_exist_products(self):
        self.assertTrue(os.path.exists('products.json'))

    def test_exist_order_example(self):
        self.assertTrue(os.path.exists('order_example.jpg'))

    def test_kb(self):
        self.assertTrue(kb)

    def test_kbi(self):
        self.assertTrue(kbi)