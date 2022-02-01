from src.values import Value
from src.gilded_rose import Item

class Stock_Item(Item):
    
    def get_sell_in(self):
        return self.sell_in
    
    def get_quality(self):
        return self.quality
    
    def set_quality(self, amount):
        self.quality = amount
        self.quality_checker()

    def decrease_sell_in(self):
        self.sell_in -= Value.ONE.value

    def improve_quality(self, amount):
        self.quality += amount
        self.quality_checker()

    def reduce_quality(self, amount):
        self.quality -= amount
        self.quality_checker()
    
    def quality_checker(self):
        if self.get_quality() > Value.MAX_ITEM_QUALITY.value:
            self.quality = Value.MAX_ITEM_QUALITY.value