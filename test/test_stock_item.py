from re import S
import pytest
from src.stock_item import Stock_Item

stock_item = Stock_Item('Unnecesary test', 5, 5)

@pytest.mark.test_get_sell_in
def test_get_sell_in():
    assert 5 == stock_item.get_sell_in()

@pytest.mark.test_get_quality
def test_get_quality():
    assert 5 == stock_item.get_quality()

@pytest.mark.test_set_quality
def test_set_quality():
    stock_item.set_quality(6)
    assert 6 == stock_item.get_quality()

@pytest.mark.test_decrease_sell_in
def test_decrease_sell_in():
    stock_item.decrease_sell_in()
    assert 4 == stock_item.get_sell_in()

@pytest.mark.test_improve_quality
def test_improve_quality():
    stock_item.improve_quality(2)
    assert 8 == stock_item.get_quality()

@pytest.mark.test_reduce_quality
def test_reduce_quality():
    stock_item.reduce_quality(1)
    assert 7 == stock_item.get_quality()

@pytest.mark.test_quality_checker
def test_quality_checker():
    stock_item.improve_quality(51)
    assert 50 == stock_item.get_quality()

