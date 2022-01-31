from gilded_rose import Gilded_Rose, Sulfuras

if __name__ == '__main__': 

    item = [Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)]
    gilded_rose = Gilded_Rose(item)
        
    print("Day 0", item)
    for day in range(1, 30):
        gilded_rose.update_quality()
        print("Day", day, item)
    