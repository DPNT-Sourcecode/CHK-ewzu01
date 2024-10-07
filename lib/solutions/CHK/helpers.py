def apply_free_item_offer(sku_count, sku, free_item_sku, quantity, condition=None):
    if sku == "F" and condition and sku_count[sku] >= condition:
        free_items = sku_count[sku] // condition
    else:
        free_items = sku_count[sku] // quantity
    sku_count[free_item_sku] -= free_items