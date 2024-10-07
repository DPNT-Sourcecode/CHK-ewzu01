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


def apply_group_discount(
    sku_count: dict[str, list[dict[str, str | int]]],
    group_items: list[str],
    group_price: int,
    group_size: int,
):
    group_items_count = 0
    for item in group_items:
        group_items_count += sku_count.get(item, 0)

    discount_groups_count = group_items_count // group_size
    discounted_price = discount_groups_count * group_price

    items_to_remove_count = discount_groups_count * group_size
    for item in group_items:
        if items_to_remove_count <= 0:
            break
        if item in sku_count:
            if sku_count[item] <= items_to_remove_count:
                items_to_remove_count -= sku_count[item]
                sku_count[item] = 0
            else:
                sku_count[item] -= items_to_remove_count
                items_to_remove_count = 0

    return discounted_price
