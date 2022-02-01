import pytest
from src.backstage_passes import Backstage_Pass

@pytest.mark.test_backstage_passes_item_IF
def test_backstage_passes_item_IF():
    backstage_passses_item = Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 10, 20)
    backstage_passses_item.update_quality()

    assert 22 == backstage_passses_item.quality
    assert 19 == backstage_passses_item.sell_in

@pytest.mark.test_backstage_passes_item_FIRST_ELIF
def test_backstage_passes_item_IF():
    backstage_passses_item = Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    backstage_passses_item.update_quality()

    assert 23 == backstage_passses_item.quality
    assert 19 == backstage_passses_item.sell_in


@pytest.mark.test_backstage_passes_item_SECOND_ELIF
def test_backstage_passes_item_IF():
    backstage_passses_item = Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    backstage_passses_item.update_quality()

    assert 0 == backstage_passses_item.quality
    assert 19 == backstage_passses_item.sell_in

@pytest.mark.test_backstage_passes_item_ELSE
def test_backstage_passes_item_IF():
    backstage_passses_item = Backstage_Pass("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    backstage_passses_item.update_quality()

    assert 21 == backstage_passses_item.quality
    assert 19 == backstage_passses_item.sell_in
