from flask import Flask, request, render_template, jsonify
from mongoengine import *
import json

app = Flask(__name__)

connect('inventory')

item_category = ('industrial','commercial','garments','electronics')

class Item(Document):
    item_name = StringField()
    item_sku = StringField()
    item_type = StringField(choices= item_category)
    item_stockable = BooleanField()
    item_price = FloatField()
    item_instock = BooleanField()

user_category = ('admin','user')
    
class User(Document):
    user_name = StringField()
    user_email = StringField()
    user_pswd = StringField()
    user_type = StringField(choices= user_category)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = Item.objects.all()
    return products.to_json()

@app.route('/products/<item_id>')
def get_product(item_id):
    item = Item.objects.get(id=item_id)
    return item.to_json()

if __name__ == '__main__':
    app.run(debug=True)
        
