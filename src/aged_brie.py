from gilded_rose import Gilded_Rose
from stock_item import Stock_Item
from values import Value

class Aged_Brie(Stock_Item):
    
    def decrease_sell_in(self):

        if self.sell_in <= Value.ZERO.value:
            self.improve_quality(Value.TWO.value)
        else:
            self.improve_quality(Value.ONE.value)

        self.sell_in -= Value.ONE.value    

    def update_quality(self):
        self.decrease_sell_in()


if __name__ == '__main__': 

    item = [Aged_Brie("Aged Brie", 2, 0)]
    gilded_rose = Gilded_Rose(item)

    print("Day 0", item)
    for day in range(1, 31):
        gilded_rose.update_quality()
        print("Day", day, item)
    
    