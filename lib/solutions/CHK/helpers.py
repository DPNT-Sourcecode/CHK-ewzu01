def apply_free_item_offer(sku_count, sku, free_item_sku, quantity, condition=None):
    if sku == "F" or sku != free_item_sku or sku_count[sku] > quantity:
        free_items = sku_count[sku] // quantity
    else:
        free_items = 0
    sku_count[free_item_sku] -= free_items


def apply_group_discount(sku_count, group_items, group_price, group_size):
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
