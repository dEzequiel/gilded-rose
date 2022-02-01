
from src import aged_brie, backstage_passes, conjured_item, normal_item, stock_item, sulfuras
from src.gilded_rose import Gilded_Rose

items = [
    conjured_item.Conjured_Item("+5 Dexterity Vest", 10, 20),
    aged_brie.Aged_Brie("Aged Brie", 2, 0),
    normal_item.Normal_Item("Elixir of the Mongoose", 5, 7),
    sulfuras.Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
    sulfuras.Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
    backstage_passes.Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 15, 20),
    backstage_passes.Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 10, 49),
    backstage_passes.Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 5, 49),
    conjured_item.Conjured_Item("Conjured Mana Cake", 3, 6)
]

gilded_rose_shop = Gilded_Rose(items)
print("-------- day 0 --------")
print(items)
for day in range(1, 31):
    print("-------- day", day, " --------")
    gilded_rose_shop.update_quality()
    print(*items, sep="\n")