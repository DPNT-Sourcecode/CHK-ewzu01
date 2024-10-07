# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    special_offers = {
        "A": [{"quantity": 5, "price": 200}, {"quantity": 3, "price": 130}],
        "B": [{"quantity": 2, "price": 45}],
        "E": [{"quantity": 2, "free_item": "B"}],
    }

    if any(char not in item_prices for char in skus):
        return -1

    sku_count = {}
    for sku in skus:
        if sku in item_prices:
            sku_count[sku] = sku_count.get(sku, 0) + 1

    total_checkout = 0
    for sku, count in sku_count.items():
        if sku in special_offers and count > 0:
            for special_offer in special_offers[sku]:
                quantity = special_offer["quantity"]
                if "price" in special_offer:
                    price = special_offer["price"]
                    offer_count = count // quantity
                    total_checkout += offer_count * price
                    count = count % quantity
                elif "free_item" in special_offer:
                    free_item = special_offer["free_item"]
                    if sku in sku_count and free_item in sku_count:
                        free_items_count = count // quantity
                        sku_count[free_item] -= free_items_count

        total_checkout += count * item_prices[sku]

    return total_checkout


