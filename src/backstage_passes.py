from gilded_rose import Gilded_Rose
from stock_item import Stock_Item
from values import Value

class Backstage_Pass(Stock_Item):
    
    def update_quality(self):
        
        if self.get_sell_in() <= Value.TEN_DAYS.value and self.get_sell_in() > Value.FIVE.value:
            self.improve_quality(Value.TWO.value)
            
        elif self.get_sell_in() <= Value.FIVE.value and self.get_sell_in() >= Value.ONE.value:
            self.improve_quality(Value.THREE.value)
        
        elif self.get_sell_in() <= Value.ZERO.value:
            self.set_quality(Value.ZERO.value)
            
        else:
            self.improve_quality(Value.ONE.value)
        
        self.decrease_sell_in()

if __name__ == '__main__': 
    item = [Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
    gilded_rose = Gilded_Rose(item)
        
    print("Day 0", item)
    for day in range(1, 31):
        gilded_rose.update_quality()
        print("Day", day, item)
    