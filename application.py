from flask import Flask, request, render_template, jsonify
from mongoengine import *
import json
from flask.ext.cors import CORS

application = Flask(__name__)
cors = CORS(application)

connect('inventory', host='ds045054.mongolab.com', port=45054, username='', password='')

item_category = ('industrial', 'commercial', 'garments', 'electronics')


class Item(Document):
    item_name = StringField()
    item_description = StringField()
    item_sku = StringField()
    item_type = StringField(choices=item_category)
    item_stockable = BooleanField(default=False)
    item_price = FloatField()
    item_instock = BooleanField(default=False)
    item_units = IntField()

user_category = ('admin', 'user')


class User(Document):
    user_name = StringField()
    user_email = StringField()
    user_pswd = StringField()
    user_type = StringField(choices=user_category)


@application.route('/')
@application.route('/index.html')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/products', methods=['GET'])
def products():
    products = Item.objects.all()
    return products.to_json()


@application.route('/products/<item_id>', methods=['GET'])
def get_product(item_id):
    item = Item.objects.get(id=item_id)
    return item.to_json()

@application.route('/products/new', methods=['POST'])
def new_product():
    new_item = Item(item_name=request.json['product']['item_name'], \
                    item_description=request.json['product']['item_description'], \
                    item_sku=request.json['product']['item_sku'], \
                    item_type=request.json['product']['item_type'], \
                    item_stockable=request.json['product']['item_stockable'], \
                    item_price=request.json['product']['item_price'], \
                    item_instock=request.json['product']['item_instock'], \
                    item_units=request.json['product']['item_units'])

    new_item.save()
    return new_item.to_json(), 201
                    


if __name__ == '__main__':
    application.debug = True
    application.run()
