def apply_free_item_offer(sku_count, sku, free_item_sku, quantity, basket_condition=None):
    if sku_count[sku] == quantity and not basket_condition:
        free_items = 0
    else:
        free_items = sku_count[sku] // quantity
    sku_count[free_item_sku] -= free_items

