# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    item_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    special_offers = {
        "A": [{"quantity": 5, "price": 200}, {"quantity": 3, "price": 130}],
        "B": [{"quantity": 2, "price": 45}],
        "E": [{"quantity": 2, "free_item": "B"}]
    }

    if any(char not in item_prices for char in skus):
        return -1

    sku_count = {}
    for sku in skus:
        if sku in item_prices:
            sku_count[sku] = sku_count.get(sku, 0) + 1
    
    # Handle special case
    if "E" in sku_count and "B" in sku_count:
        free_items = sku_count["E"] // 2
        sku_count["B"] -= free_items

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


