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

    def expired_sell_in(self):
        
        # if self.sell_in <= 0:
        #     self.set_quality(ZERO)
        
        if self.sell_in == ZERO:
            self.set_quality(ZERO)
            self.sell_in -= ONE

        # elif self.sell_in > ZERO:
        #     self.sell_in -= ONE
        #     self.reduce_quality(ONE)
        else:
            self.sell_in -= ONE
            self.reduce_quality(ONE)
            
    def expired_counter(self):
        self.sell_in -= ONE
        # self.update_quality()
        
    def decrease_sell_in(self):
        self.sell_in -= ONE
    
    def set_quality(self, value):
        if value < 0:
            self.quality = MIN_ITEM_QUALITY
        
        self.quality = value

    def improve_quality(self, value):
        self.quality += value

        # if self.quality > MAX_ITEM_QUALITY:
        #     self.quality = MAX_ITEM_QUALITY
    
    def reduce_quality(self, value):
        self.quality -= value
        
        if self.quality < 0:
            self.quality = MIN_ITEM_QUALITY

    def update_quality(self):
        self.reduce_quality(TWO) if self.expired_sell_in() else self.reduce_quality(ONE)

class Normal_Item(Stock_Item):

    def expired_counter(self):
        self.sell_in -= ONE
    
    def update_quality(self):   
        
        self.expired_sell_in()
        
        # if self.sell_in < 0:
        #     self.decrease_sell_in
        #     self.set_quality(ZERO)
        # else:
        #     self.decrease_sell_in()
        #     self.reduce_quality(ONE)
        

class Aged_Brie(Stock_Item):

    def expired_sell_in(self):
        if self.sell_in <= ZERO:
            self.improve_quality(TWO)
            self.sell_in -= ONE
        else:
            self.decrease_sell_in()
            self.quality += 1
        
    def update_quality(self):
        # self.improve_quality(2) if self.expired_sell_in() else self.improve_quality(1)
        self.expired_sell_in()
        
        
class Sulfuras(Stock_Item):
    
    def update_quality(self):
        self.quality = LEGENDARY_ITEM_QUALITY

class Backstage_Pass(Stock_Item):

    def expired_sell_in(self):
        if self.sell_in <= ZERO:
            self.quality = ZERO
    
    def ten_days_or_less(self):
        if self.sell_in > 5 and self.sell_in <= 10:
            self.quality += 2
            self.sell_in -= 1
    
    def five_days_or_less(self):
        if self.sell_in <= 5:
            self.improve_quality(THREE)
            self.sell_in -= 1
        
    def update_quality(self):
        if self.sell_in > 10:
            self.improve_quality(1)
            self.sell_in -= 1
        
        self.ten_days_or_less()
        self.five_days_or_less()
        
        if not self.ten_days_or_less and not self.five_days_or_less():
            self.expired_sell_in()
        
        

class Conjured_Item(Stock_Item):
    
    def update_quality(self):
        if self.sell_in >= ZERO:
            self.reduce_quality(TWO)
        else:
            self.reduce_quality(FOUR)