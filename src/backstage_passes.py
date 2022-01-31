
from gilded_rose import Gilded_Rose, Backstage_Pass

if __name__ == '__main__': 
#Backstage passes to a TAFKAL80ETC concert, 14, 21
    item = [Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
    gilded_rose = Gilded_Rose(item)
        
    print("Day 0", item)
    for day in range(1, 30):
        gilded_rose.update_quality()
        print("Day", day, item)
    