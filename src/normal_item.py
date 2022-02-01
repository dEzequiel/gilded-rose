from src.gilded_rose import Gilded_Rose
from src.stock_item import Stock_Item
from src.values import Value

class Normal_Item(Stock_Item):
    
    def update_quality(self):

        if self.get_sell_in() <= Value.ZERO.value:
            self.set_quality(Value.ZERO.value)
        else:
            self.reduce_quality(Value.ONE.value)
        
        self.decrease_sell_in()
        
# if __name__ == '__main__': 

#     item = [Normal_Item("Elixir of the Mongoose", 5, 7)]
#     gilded_rose = Gilded_Rose(item)
        
#     print("Day 0", item)
#     for day in range(1, 30):
#         gilded_rose.update_quality()
#         print("Day", day, item)
    
