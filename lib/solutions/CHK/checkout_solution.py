# noinspection PyUnusedLocal
# skus = unicode string
def apply_free_item_offer(sku_count, sku, free_item_sku, quantity):
    free_items = sku_count[sku] // quantity
    sku_count[free_item_sku] -= free_items


def checkout(skus):
    item_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    special_offers = {
        "A": [{"quantity": 5, "price": 200}, {"quantity": 3, "price": 130}],
        "B": [{"quantity": 2, "price": 45}],
        "E": [{"quantity": 2, "free_item": "B"}],
        "F": [{"quantity": 3, "free_item": "F"}],
    }

    if any(char not in item_prices for char in skus):
        return -1

    sku_count = {}
    for sku in skus:
        if sku in item_prices:
            sku_count[sku] = sku_count.get(sku, 0) + 1

    if "E" in sku_count and "B" in sku_count:
        apply_free_item_offer(sku_count, "E", "B", 2)

    if "F" in sku_count and sku_count["F"] >= 3:
        apply_free_item_offer(sku_count, "F", "F", 3)

    total_checkout = 0
    for sku, count in sku_count.items():
        if sku in special_offers and count > 0:
            for special_offer in special_offers[sku]:
                if "price" in special_offer:
                    price = special_offer["price"]
                    quantity = special_offer["quantity"]
                    offer_count = count // quantity
                    total_checkout += offer_count * price
                    count = count % quantity

        total_checkout += count * item_prices[sku]

    return total_checkout

