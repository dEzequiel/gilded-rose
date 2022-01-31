from cmath import exp
import pytest
from src.gilded_rose import Normal_Item, Gilded_Rose

@pytest.mark.test_normal_item
def test_normal_item():
    item = [Normal_Item("Elixir of the Mongoose", 5, 7)]
    gilded_rose = Gilded_Rose(item)
    gilded_rose.update_quality()
    
    expected = ['Elixir of the Mongoose', 4, 6]
    
    assert item.__repr__() == expected

       