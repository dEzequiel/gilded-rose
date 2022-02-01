import pytest
from src.normal_item import Normal_Item
from src.gilded_rose import Gilded_Rose

@pytest.mark.test_normal_item
def test_normal_item():
    normal_item = Normal_Item("Elixir of the Mongoose", 5, 7)
    normal_item.update_quality()
    
    assert 4 == normal_item.sell_in
    assert 6 == normal_item.quality