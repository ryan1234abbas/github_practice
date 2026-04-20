import requests 
from flask import Flask
import jsonify

class ProductService:
    def __init__(self):
        self.products = [
            {"id": i, "name": f"product_{i}", 'price': i}
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
        return None
            
    def return_price(self, product):
        #returns the price of a product (input as product_i)
        for p in self.products:
            if p['name'] == product:
                return p['price']
        return None
    
    def add_product(self, id, name, price):
        self.products.append({'id': id, 'name': name, 'price': price})

    def delete_product(self, id):
        #delet by ID
        for i, p in enumerate(self.products):
            if p['id'] == id:
                del self.products[i]
    
    def product_exists(self, product):
        for p in self.products:
            if p["name"] == product: return True
        return False
    
    def products_in_priceRange(self, lower, upper):
        range = []
        for p in self.products:
            if p['price'] <= upper and p['price'] >= lower:
                range.append(p['name'])
            
        return range

app = Flask(__name__)
service = ProductService()

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    service.add_product(data['id'], data['name'], data['price'])
    return jsonify({'msg': 'successs'}), 201

@app.route('/products', methods=['GET'])
def return_all_products():
    products = service.return_all_products()
    return jsonify({'products': products}), 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    service.delete_product(id)
    return jsonify({"msg": 'deleted'}), 200

@app.route('/products/<string:name>/exists', methods=['GET'])
def product_exists(name):
    res = service.product_exists(name)
    return jsonify({"msg": res}), 200
