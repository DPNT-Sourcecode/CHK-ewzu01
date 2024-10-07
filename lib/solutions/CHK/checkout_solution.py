

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    special_offers = {"A": {"quantity": 3, "price": 130}, "B": {"quantity": 2, "price": 45}}

    if any(char not in skus for char in skus):
        return -1
    




