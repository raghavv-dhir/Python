class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    #string representation
    def __str__(self):
        if not self.items:
            return "ShoppingCart is empty"
        return f"Shopping Cart: \n{self.items}: {self.total_price()}"

    def __repr__(self):
        return f"ShoppingCart(items={self.items!r})"


    #Comparison
    def total_price(self):
        return sum(price for _, price in self.items)

    def __eq__(self, other):
        return self.total_price() == other.total_price()

    def __lt__(self, other):
        return self.total_price() < other.total_price()

    def __gt__(self, other):
        return self.total_price() > other.total_price()


    #Arithmetic
    def __add__(self, other):
        # Combine items of both carts
        return ShoppingCart(self.items + other.items)

    def __sub__(self, other):
        # Remove items that exist in other cart
        remaining_items = self.items.copy()
        for item in other.items:
            if item in remaining_items:
                remaining_items.remove(item)
        return ShoppingCart(remaining_items)

    def __mul__(self, quantity):
        # Repeat items
        return ShoppingCart(self.items * quantity)


    #Iteration
    def __iter__(self):
        return iter(self.items)


    #Indexing
    def __getitem__(self, index):
        return self.items[index]


if __name__ == "__main__":
    cart1 = ShoppingCart([
        ("Laptop", 60000),
        ("Mouse", 1500),
        ("Keyboard", 3000)
    ])

    cart2 = ShoppingCart([
        ("Headphones", 4000),
        ("Mouse", 1500)
    ])

    print("cart1:")
    print(cart1)

    print("\ncart2:")
    print(cart2)

    # Comparision
    print("\nComparison:")
    print("cart1 == cart2 :", cart1 == cart2)
    print("cart1 > cart2  :", cart1 > cart2)
    print("cart1 < cart2  :", cart1 < cart2)

    # Addition
    combined_cart = cart1 + cart2
    print("\nAfter Adding cart1 + cart2:")
    print(combined_cart)

    # Sub
    reduced_cart = combined_cart - ShoppingCart([("Mouse", 1500)])
    print("\nAfter Removing Mouse:")
    print(reduced_cart)

    # Mul
    bulk_cart = cart2 * 2
    print("\nBulk Order (cart2 * 2):")
    print(bulk_cart)

    # Indexing
    print("\nIndexing:")
    print("First item in cart1:", cart1[0])

    # Iteration
    print("\nIterating over cart1:")
    for item in cart1:
        print(item)

    # repr()
    print("\nrepr(cart1):")
    print(repr(cart1))
