from src import Normal_Item, Stock_Item, Gilded_Rose

if __name__ == '__main__': 

    item = [Normal_Item("Elixir of the Mongoose", 5, 7)]
    gilded_rose = Gilded_Rose(item)
    print(type(item))

    for dia in range(1, 10):
        gilded_rose.update_quality()
        print('Day', dia, item)
       