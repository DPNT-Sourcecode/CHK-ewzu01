# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    special_offers = {
        "A": {"quantity": 3, "price": 130},
        "B": {"quantity": 2, "price": 45},
    }

    if any(char not in item_prices for char in skus):
        return -1

    sku_count = {}
    for sku in skus:
        if sku in item_prices:
            sku_count[sku] = sku_count.get(sku, 0) + 1

    total_checkout = 0
    for sku, count in sku_count.items():
        if sku in special_offers:
            price = special_offers[sku]["price"]
            quantity = special_offers[sku]["quantity"]
            if count == quantity:
                total_checkout += count * price
            elif count % quantity == 0:
                total_checkout += (count / quantity) * price
            elif count < quantity:
                total_checkout += count * item_prices[sku]
            else:
                sku_groups = count // quantity
                remaining_skus = count - (sku_groups * quantity)
                total_checkout += (sku_groups * price) + (remaining_skus * item_prices[sku])
        else:
            total_checkout += count * item_prices[sku]

    return total_checkout



