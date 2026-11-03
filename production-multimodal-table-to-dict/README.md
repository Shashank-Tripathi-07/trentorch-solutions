# Extract a Parsed Table Into Structured Records

Beginner | production-systems | multimodal | data-processing

### The problem, from first principles

A table extracted from a PDF or an image (by an OCR pass or a table-detection model) usually comes out as a header row plus a list of data rows -- both just lists of strings. Reasoning about that table by column name ("what's the price column") is much easier once each row is a dict keyed by header name, rather than a positional list the caller has to remember the column order of.

### The task

Write `rows_to_records(header, rows)` that pairs each row with the header by position and returns one dict per row. A row shorter than the header simply omits its missing trailing columns; a row longer than the header drops its extra trailing cells.
