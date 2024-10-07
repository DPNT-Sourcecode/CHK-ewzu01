# noinspection PyUnusedLocal
from .constants import item_prices, special_offer_prices
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
    group_discount = apply_group_discount(sku_count)

    total_checkout = 0
    total_checkout += group_discount
    for sku, count in sku_count.items():
        if sku in special_offer_prices and count > 0:
            for special_offer in special_offer_prices[sku]:
                if "price" in special_offer:
                    offer_count = count // special_offer["quantity"]
                    total_checkout += offer_count * special_offer["price"]
                    count = count % special_offer["quantity"]

        total_checkout += count * item_prices[sku]

    return total_checkout

