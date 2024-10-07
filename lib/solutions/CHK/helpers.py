def apply_free_item_offer(sku_count, sku, free_item_sku, quantity, condition=None):
    if sku == "F" or sku != free_item_sku or sku_count[sku] > quantity:
        free_items = sku_count[sku] // quantity
    else:
        free_items = 0
    sku_count[free_item_sku] -= free_items
