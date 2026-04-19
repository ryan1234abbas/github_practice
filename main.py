import requests 
from flask import Flask

class ProductService:
    def __init__(self):
        self.products = [
            {"id": i, "name": f"product_{i}", 'price': f'${i}'}
            for i in range(1, 101)
        ]
    def return_all_products(self):
        product_names = []
        for product in self.products:
            product_names.append(product['name'])
        return product_names
        
    def search_prod(self, id):
        #should return prod given id
        for product in self.products:
            if product['id'] == id:
                return product['name']
            
    def return_price(self, product):
        #returns the price of a product (input as product_i)
        for p in self.products:
            if p['name'] == product:
                return p['price']
        return None