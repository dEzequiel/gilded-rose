from src.normal_item import Normal_Item
import pytest

@pytest.mark.test_normal_item
def test_normal_item():
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    normal_item.update_quality()
    
    assert 4 == normal_item.sell_in
    assert 6 == normal_item.quality

@pytest.mark.test_normal_item_sell_in_zero
def test_normal_item_quality_zero():
    normal_item = Normal_Item("Elixir of the Mongoose", -1, 7)
    normal_item.update_quality()

    assert 0 == normal_item.quality