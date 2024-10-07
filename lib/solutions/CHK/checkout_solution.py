# noinspection PyUnusedLocal

from .constants import item_prices, special_offers
from .helpers import apply_free_item_offer, apply_group_discount


# skus = unicode string
def checkout(skus):
    sku_count = {}
    for sku in skus:
        if sku in item_prices:
            sku_count[sku] = sku_count.get(sku, 0) + 1
        else:
            return -1

    if "E" in sku_count and "B" in sku_count:
        apply_free_item_offer(sku_count, sku="E", free_item_sku="B", quantity=2)

    if "F" in sku_count:
        apply_free_item_offer(sku_count, sku="F", free_item_sku="F", quantity=3)

    if "N" in sku_count and "M" in sku_count:
        apply_free_item_offer(sku_count, sku="N", free_item_sku="M", quantity=3)

    if "R" in sku_count and "Q" in sku_count:
        apply_free_item_offer(sku_count, sku="R", free_item_sku="Q", quantity=3)

    if "U" in sku_count:
        apply_free_item_offer(sku_count, sku="U", free_item_sku="U", quantity=3)

    group_items = ["S", "T", "X", "Y", "Z"]
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

