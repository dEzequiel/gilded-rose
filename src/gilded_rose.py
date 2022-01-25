from random import expovariate
from src.item import Item

# Constants

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
TEN_DAYS = 10
FIVE_DAYS = 5
MAX_ITEM_QUALITY = 50
MIN_ITEM_QUALITY = 0
LEGENDARY_ITEM_QUALITY = 80    

class Gilded_Rose(object):
    
    # So items can be any type of data structure.
    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
            item.update_quality()

class Item:
    # This is just a normal item, no logic, just attributes.
    def __init__(self, name, sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Interface(Item):
    def update_quality():
        pass

class Stock_Item(Item):

    def expired_item(self):
        return self.sell_in < 0
    
    def expired_counter(self):
        self.sell_in -= 1
        self.update_quality()
    
    def improve_quality(self, value):
        self.quality += value
        self.quality = MAX_ITEM_QUALITY if self.quality >= MAX_ITEM_QUALITY else 0
    
    def reduce_quality(self, value):
        self.quality -= value
        self.quality = MIN_ITEM_QUALITY if self.quality < MIN_ITEM_QUALITY else 0

    def update_quality(self):
        self.reduce_quality(2) if self.expired_item() else self.reduce_quality(1)

class Aged_Brie(Stock_Item):

    def update_quality(self):
        self.improve_quality(2) if self.expired_item() else self.improve_quality(1)