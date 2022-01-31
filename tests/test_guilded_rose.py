import unittest


from src.gilded_rose import Stock_Item, Gilded_Rose

class GildedRoseTest(unittest.main):
    def test_item_decreases_quality_by_one(self):
        items = [Stock_Item("Elixir of the Mongoose,", 5, 5)]
        gilded_rose = Gilded_Rose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

if __name__ == '__main__':
    unittest.main()