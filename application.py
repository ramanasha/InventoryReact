from flask import Flask, request, render_template, jsonify
from mongoengine import *
import json
from flask.ext.cors import CORS

application = Flask(__name__)
cors = CORS(application)

connect('inventory')

item_category = ('industrial','commercial','garments','electronics')

class Item(Document):
    item_name = StringField()
    item_description = StringField()
    item_sku = StringField()
    item_type = StringField(choices= item_category)
    item_stockable = BooleanField(default=False)
    item_price = FloatField()
    item_instock = BooleanField(default=False)
    item_units = IntField()

user_category = ('admin','user')
    
class User(Document):
    user_name = StringField()
    user_email = StringField()
    user_pswd = StringField()
    user_type = StringField(choices= user_category)

@application.route('/')
@application.route('/index.html')
@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/products')
def products():
    products = Item.objects.all()
    return products.to_json()

@application.route('/products/<item_id>')
def get_product(item_id):
    item = Item.objects.get(id=item_id)
    return item.to_json()

if __name__ == '__main__':
    application.debug = True
    application.run()
        
