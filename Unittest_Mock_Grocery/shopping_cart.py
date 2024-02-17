# Can add item to cart
# Can throw the error if cart is full
# Can caclulate total price of items


from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("Cannot add one more item")
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def get_item(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0.0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price
