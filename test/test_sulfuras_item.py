from src.sulfuras import Sulfuras
import pytest

@pytest.mark.test_sulfuras_item
def test_sulfuras_item():
    sulfuras_item = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)
    sulfuras_item.update_quality()

    assert -1 == sulfuras_item.sell_in
    assert 80 == sulfuras_item.quality
