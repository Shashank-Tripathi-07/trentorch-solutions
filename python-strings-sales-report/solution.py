def build_sales_report(raw: str) -> str:
    """
    Parse messy sales data and produce an aligned sales report.
    """
    rows = []
    grand_total = 0.0
    bytes_total = 0

    # Process each line separately
    for line in raw.splitlines():

        # Step 1: Remove whitespace and skip empty/comment lines
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        # Step 2: Split into exactly three fields
        fields = line.split(",")

        if len(fields) != 3:
            continue

        # Step 3: Clean individual fields
        item, quantity, price = [field.strip() for field in fields]

        # Validate quantity
        if not quantity.isdigit():
            continue

        # Convert numeric fields
        qty = int(quantity)
        price = float(price)

        # Step 4: Format item name
        item = item.title()[:12]

        # Step 5: Calculate line total
        line_total = qty * price

        grand_total += line_total
        bytes_total += len(item.encode("utf-8"))

        # Build formatted row
        row = (
            f"{item:<12}"
            f"{qty:>4}"
            f"{price:>10.2f}"
            f"{line_total:>12,.2f}"
        )

        rows.append(row)

    # Build report
    header = f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}"

    separator = "-" * 38

    grand_total_line = f"{'TOTAL':<26}{grand_total:>12,.2f}"

    summary = f"Rows: {len(rows)} | UTF-8 bytes in items: {bytes_total}"

    return "\n".join([
        header,
        *rows,
        separator,
        grand_total_line,
        summary
    ])
