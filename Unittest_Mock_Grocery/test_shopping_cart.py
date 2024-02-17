from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import MagicMock
import pytest


@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_item()


def test_if_cart_is_not_full(cart):
    with pytest.raises(OverflowError):
        for i in range(6):
            cart.add("apple")


def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0

    item_database.get = MagicMock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0
