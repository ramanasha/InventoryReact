from flask import Flask, request, render_template
from mongoengine import *

main_inventory= connect('inventory')

item_category = ('industrial','commercial','garments','electronics')

class Item(Document):
    
    item_name = StringField()
    item_sku = StringField()
    item_type = StringField(choices= item_category)
    item_stockable = BooleanField()
    item_price = FloatField()
    item_instock = BooleanField()
