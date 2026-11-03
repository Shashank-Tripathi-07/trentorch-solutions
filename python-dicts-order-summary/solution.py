def summarize_orders(orders: list) -> dict:
    """
    Summarize nested order records without modifying the input.
    """

    units_by_customer = {}
    units_by_sku = {}

    customers_by_sku = {}
    customers_by_initial = {}

    # Step 1: Aggregate quantities and collect customer groups
    for order in orders:
        customer = order["customer"]
        items = order["items"]

        # Include customers even if their orders are empty
        units_by_customer.setdefault(customer, 0)

        for sku, quantity in items.items():

            # Total units per customer
            units_by_customer[customer] += quantity

            # Total units per SKU
            units_by_sku[sku] = units_by_sku.get(sku, 0) + quantity

            # Distinct customers per SKU
            customers_by_sku.setdefault(sku, set()).add(customer)

        # Group non-empty customer names by initial
        if customer:
            initial = customer[0].upper()
            customers_by_initial.setdefault(initial, set()).add(customer)

    # Step 2: Find the SKU with the largest quantity.
    # Alphabetically first SKU wins ties.
    if units_by_sku:
        top_sku = min(
            units_by_sku,
            key=lambda sku: (-units_by_sku[sku], sku)
        )
    else:
        top_sku = None

    # Step 3: Convert sets into independent sorted lists
    customers_by_sku = {
        sku: sorted(customers)
        for sku, customers in customers_by_sku.items()
    }

    customers_by_initial = {
        initial: sorted(customers)
        for initial, customers in customers_by_initial.items()
    }

    # Step 4: Return exactly the requested five keys
    return {
        "units_by_customer": units_by_customer,
        "units_by_sku": units_by_sku,
        "top_sku": top_sku,
        "customers_by_sku": customers_by_sku,
        "customers_by_initial": customers_by_initial
    }
