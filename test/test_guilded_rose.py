import pytest
from src.gilded_rose import Item

@pytest.mark.test_item_constructor
def test_item_constructor():
    item = Item("Help me!", 9, 9)
    assert "Help me!" == item.name
    assert 9 == item.quality
    assert 9 == item.sell_in

@pytest.mark.test_item_representation
def test_item_representation():
    item = Item("Help me!", 9, 9)
    assert item.__repr__() == "Help me!, 9, 9" 