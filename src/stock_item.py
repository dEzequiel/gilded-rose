from values import Value
from gilded_rose import Item

class Stock_Item(Item):

    def set_quality(self, amount):
        
        if amount > Value.MAX_ITEM_QUALITY.value:
            self.quality = Value.MAX_ITEM_QUALITY.value
        else:
            self.quality = amount

    def decrease_sell_in(self):
        if self.sell_in <= Value.ZERO.value:
            self.set_quality(Value.ZERO.value)

        self.sell_in -= Value.ONE.value

    def improve_quality(self, amount):
        self.quality += amount

    def reduce_quality(self, amount):
        self.quality -= amount
        if self.quality < Value.ZERO.value:
            self.quality = Value.MIN_ITEM_QUALITY.value

    # def update_quality(self):
    #     self.reduce_quality(Value.TWO) if self.expired_sell_in() else self.reduce_quality(Value.ONE)