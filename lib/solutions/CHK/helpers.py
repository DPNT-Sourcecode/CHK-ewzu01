def apply_free_item_offer(sku_count, sku, free_item_sku, quantity):
    free_items = sku_count[sku] // quantity
    sku_count[free_item_sku] -= free_items
