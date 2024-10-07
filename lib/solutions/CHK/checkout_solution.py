# noinspection PyUnusedLocal
from .constants import item_prices, special_offers, group_items
from .helpers import apply_free_item_offers, apply_group_discount


# skus = unicode string
def checkout(skus: str):
    sku_count = {}
    for sku in skus:
        if sku in item_prices:
            sku_count[sku] = sku_count.get(sku, 0) + 1
        else:
            return -1

    apply_free_item_offers(sku_count)

    group_discount = apply_group_discount(sku_count, group_items, group_size=3, group_price=45)

    total_checkout += group_discount
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
