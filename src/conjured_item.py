from src.gilded_rose import Gilded_Rose
from src.stock_item import Stock_Item
from src.values import Value

class Conjured_Item(Stock_Item):
    
    def update_quality(self):
        if self.get_sell_in() >= Value.ZERO.value:
            self.reduce_quality(Value.ONE.value)
        elif self.get_sell_in() < Value.ZERO.value:
            self.set_quality(Value.ZERO.value)
        else:
            self.reduce_quality(Value.FOUR.value)

        self.decrease_sell_in()

# if __name__ == '__main__': 

#     item = [Conjured_Item("Conjured Mana Cake", 3, 6)]
#     gilded_rose = Gilded_Rose(item)

#     print("Day 0", item)
#     for day in range(1, 31):
#         gilded_rose.update_quality()
#         print("Day", day, item)