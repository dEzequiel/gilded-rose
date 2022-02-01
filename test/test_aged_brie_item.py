import pytest
from src.aged_brie import Aged_Brie

@pytest.mark.test_aged_brie_item_IF
def test_aged_brie_item_IF():
    aged_brie_item = Aged_Brie("Aged Brie", 0, 0)
    aged_brie_item.update_quality()

    assert 2 == aged_brie_item.quality
    assert -1 == aged_brie_item.sell_in

@pytest.mark.test_aged_brie_item_ELSE
def test_aged_brie_item_ELSE():
    aged_brie_item = Aged_Brie("Aged Brie", 1, 0)
    aged_brie_item.update_quality()

    assert 1 == aged_brie_item.quality
    assert 0 == aged_brie_item.sell_in



