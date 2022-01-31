
from gilded_rose import Gilded_Rose
from normal_item import Normal_Item
from stock_item import Stock_Item
from values import Value


'''
Una "Entrada al Backstage", como el queso brie, incrementa su calidad a medida que la fecha de venta se aproxima

    si faltan 10 días o menos para el concierto, la calidad se incrementa en 2 unidades
    si faltan 5 días o menos, la calidad se incrementa en 3 unidades
    luego de la fecha de venta la calidad cae a 0
'''

class Backstage_Pass(Stock_Item):
    
    def update_quality(self):
        if self.sell_in <= Value.TEN_DAYS.value and self.sell_in > Value.FIVE.value:
            self.improve_quality(Value.TWO.value)
            self.decrease_sell_in()
        elif self.sell_in <= Value.FIVE.value:
            self.improve_quality(Value.THREE.value)
            self.decrease_sell_in()
        else:
            self.decrease_sell_in()
            self.improve_quality(Value.ONE.value)
        

if __name__ == '__main__': 
#Backstage passes to a TAFKAL80ETC concert, 14, 21
    item = [Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
    gilded_rose = Gilded_Rose(item)
        
    print("Day 0", item)
    for day in range(1, 30):
        gilded_rose.update_quality()
        print("Day", day, item)
    