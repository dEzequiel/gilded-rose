from gilded_rose import Gilded_Rose, Normal_Item

if __name__ == '__main__': 

    item = [Normal_Item("Elixir of the Mongoose", 5, 7)]
    gilded_rose = Gilded_Rose(item)
        
    print("Day 0", item)
    for day in range(1, 30):
        gilded_rose.update_quality()
        print("Day", day, item)
    
