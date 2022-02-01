from src.gilded_rose import Gilded_Rose
from src.stock_item import Stock_Item
from src.values import Value

class Aged_Brie(Stock_Item):
    
    def update_quality(self):

        if self.get_sell_in() <= Value.ZERO.value:
            self.improve_quality(Value.TWO.value)
        else:
            self.improve_quality(Value.ONE.value)

        self.decrease_sell_in()


# if __name__ == '__main__': 
#     item = [Aged_Brie("Aged Brie", 2, 0)]
#     gilded_rose = Gilded_Rose(item)

#     print("Day 0", item)
#     for day in range(1, 31):
#         gilded_rose.update_quality()
#         print("Day", day, item)
    
    