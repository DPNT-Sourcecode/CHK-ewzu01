from .constants import item_prices, special_offer_free_items


def apply_free_item_offer(
    sku_count: dict[str, list[dict[str, str | int]]],
    sku: str,
    free_item_sku: str,
    quantity: int,
):
    if sku == "F" or sku != free_item_sku or sku_count[sku] > quantity:
        free_items = sku_count[sku] // quantity
    else:
        free_items = 0
    sku_count[free_item_sku] -= free_items


def apply_free_item_offers(sku_count: dict[str, list[dict[str, str | int]]]):
    for sku, special_offer in special_offer_free_items.items():
        free_item_sku = special_offer["free_item"]
        quantity = special_offer["quantity"]
        if sku in sku_count and free_item_sku in sku_count:
            if sku == "F" or sku != free_item_sku or sku_count[sku] > quantity:
                free_items = sku_count[sku] // quantity
            else:
                free_items = 0
            sku_count[free_item_sku] -= free_items
            # apply_free_item_offer(sku_count, sku, free_item_sku, quantity=special_offer["quantity"])

def apply_group_discount(
    sku_count: dict[str, list[dict[str, str | int]]],
    group_items: list[str],
    group_price: int,
    group_size: int,
):
    group_items_count = 0
    group_items_prices = {}
    for item in group_items:
        group_items_count += sku_count.get(item, 0)
        if item in item_prices:
            group_items_prices[item] = item_prices[item]

    group_items_prices_sorted = {k: v for k, v in sorted(group_items_prices.items(), key=lambda item: item[1], reverse=True)}

    discount_groups_count = group_items_count // group_size
    discounted_price = discount_groups_count * group_price

    items_to_remove_count = discount_groups_count * group_size
    for item in group_items_prices_sorted:
        if items_to_remove_count <= 0:
            break
        if item in sku_count:
            while sku_count[item] > 0 and items_to_remove_count > 0:
                sku_count[item] -= 1
                items_to_remove_count -= 1

    return discounted_price






