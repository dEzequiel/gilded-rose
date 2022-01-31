from values import Value

class Stock_Item(Item):

    def set_quality(self, value):
        
        if value > Value.MAX_ITEM_QUALITY:
            self.quality = Value.MAX_ITEM_QUALITY
        else:
            self.quality = self.value
        
    def expired_sell_in(self):

        if self.sell_in == Value.ZERO:
            self.sell_in = Value.ZERO
        else:
            self.sell_in -= Value.ONE
            self.reduce_quality(Value.ONE)
        
    def decrease_sell_in(self):
        self.sell_in -= Value.ONE

    def improve_quality(self, value):
        self.quality += value
    
    def reduce_quality(self, value):
        self.quality -= value
        
        if self.quality < Value.ZERO:
            self.quality = Value.MIN_ITEM_QUALITY

    # def update_quality(self):
    #     self.reduce_quality(Value.TWO) if self.expired_sell_in() else self.reduce_quality(Value.ONE)