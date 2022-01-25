from src.gilded_rose import Normal_Item, Stock_Item, Gilded_Rose

if __name__ == '__main__': 

    item = Normal_Item("Elixir of the Mongoose", 5, 7)

    print(item)

    for dia in range(1, 10):
        print('Day ', dia), item.update_quality(), 
        print(item), "\n"
       