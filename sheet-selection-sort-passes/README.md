# Selection Sort, Pass by Pass

Beginner | dsa-sheet | sorting | sorting-by-hand

**Selection sort** builds the sorted part of a list from the left. On pass `i` it finds the smallest value in `nums[i:]`, swaps it into position `i`, and moves on.

Run selection sort on `nums` and return the list as it looks **after every pass**, in order. There is one pass for each position except the last, so a list of length `n` gives `n - 1` snapshots. A list with fewer than two items gives `[]`.

Two rules make the answer exact:

- If the smallest value appears more than once, take the leftmost one.
- Always swap, even when the smallest value is already at position `i`. Record the snapshot either way.

Do not change `nums`.

### Examples

**Example 1**

Input:

```python
selection_sort_passes([64, 25, 12, 22, 11])
```

Output:

```text
[[11, 25, 12, 22, 64], [11, 12, 25, 22, 64], [11, 12, 22, 25, 64], [11, 12, 22, 25, 64]]
```

After pass 0 the smallest value, 11, is first. The last pass swaps 25 with itself.

**Example 2**

Input:

```python
selection_sort_passes([3, 1, 3, 1])
```

Output:

```text
[[1, 3, 3, 1], [1, 1, 3, 3], [1, 1, 3, 3]]
```

Pass 0 takes the leftmost 1 (index 1). Pass 1 takes the other 1. Pass 2 swaps 3 with itself.

### Constraints

- `0 <= len(nums) <= 300`
- `-10**9 <= nums[i] <= 10**9`
