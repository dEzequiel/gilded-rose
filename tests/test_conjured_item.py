import pytest
from src.conjured_item import Conjured_Item

@pytest.mark.test_conjured_item_IF
def test_conjured_item_IF():
    conjured_item = Conjured_Item("Conjured Mana Cake", 3, 6)
    conjured_item.update_quality()

    assert 4 == conjured_item.quality
    assert 2 == conjured_item.sell_in

@pytest.mark.test_conjured_item_ELSE
def test_conjured_item_ELSE():
    conjured_item = Conjured_Item("Conjured Mana Cake", 0, 6)
    conjured_item.update_quality()

    assert 2 == conjured_item.quality
    assert -1 == conjured_item.sell_in
