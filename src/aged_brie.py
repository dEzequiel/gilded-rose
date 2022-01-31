from gilded_rose import Gilded_Rose, Aged_Brie

if __name__ == '__main__': 

    item = [Aged_Brie("Aged Brie", 2, 0)]
    gilded_rose = Gilded_Rose(item)

    print("Day 0", item)
    for day in range(1, 31):
        gilded_rose.update_quality()
        print("Day", day, item)
    
    