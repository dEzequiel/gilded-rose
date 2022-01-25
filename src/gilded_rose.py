# Constants

TEN_DAYS = 10
FIVE_DAYS = 5
MAX_ITEM_QUALITY = 50
MIN_ITEM_QUALITY = 0
LEGENDARY_ITEM_QUALITY = 80    

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
FOUR = 4

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


class Stock_Item(Item):

    def expired_item(self):
        return self.sell_in < ZERO
    
    def expired_counter(self):
        self.sell_in -= ONE
        self.update_quality()
    
    def set_quality(self, value):
        self.quality = value

    def improve_quality(self, value):
        self.quality += value
        self.quality = MAX_ITEM_QUALITY if self.quality >= MAX_ITEM_QUALITY else 0
    
    def reduce_quality(self, value):
        self.quality -= value
        self.quality = MIN_ITEM_QUALITY if self.quality < MIN_ITEM_QUALITY else 0

    def update_quality(self):
        self.reduce_quality(TWO) if self.expired_item() else self.reduce_quality(ONE)

class Normal_Item(Stock_Item):

    def expired_counter(self):
        self.sell_in -= ONE

    def update_quality(self):
        if self.expired_item():
            self.set_quality(MIN_ITEM_QUALITY) 
        else:
            self.expired_counter()
            self.reduce_quality(ONE)

class Aged_Brie(Stock_Item):

    def update_quality(self):
        self.improve_quality(2) if self.expired_item() else self.improve_quality(1)

class Sulfuras(Stock_Item):
    
    def update_quality(self):
       self.quality = LEGENDARY_ITEM_QUALITY

class Backstage_Pass(Stock_Item):

    def update_quality(self):
        if self.expired_item():
            self.quality = MIN_ITEM_QUALITY
        elif self.sell_in < FIVE_DAYS:
            self.improve_quality(THREE)
        elif self.sell_in < TEN_DAYS:
            self.improve_quality(TWO)
        else:
            self.improve_quality(ONE)

class Conjured_Item(Stock_Item):
    
    def update_quality(self):
        if self.sell_in >= ZERO:
            self.reduce_quality(TWO)
        else:
            self.reduce_quality(FOUR)