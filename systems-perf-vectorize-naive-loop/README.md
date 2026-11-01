# Vectorize a Naive Python Loop into NumPy Ops, Before/After Speed Comparison

Beginner | mlops | acceleration

### The problem, from first principles

Every operation in this curriculum's classical-ML and deep-learning tracks was implemented as a single vectorized NumPy expression, deliberately avoiding Python-level loops over individual elements — this question makes the reason for that convention explicit and measurable, rather than assumed.

### From theory to code

Implement `naive_dot_product(a, b)` (a plain Python loop over two lists), `vectorized_dot_product(a, b)` (the identical computation as one NumPy call), and `compare_speed(a, b)`, which runs both on the same data and reports both the results and the actual measured timings.

### Constraints

- `naive_dot_product`: takes plain Python lists, returns a `float`.
- `vectorized_dot_product`: takes NumPy arrays, returns a `float`.
- `compare_speed`: takes NumPy arrays, returns a dict with `naive_result`, `vectorized_result`, `naive_time`, `vectorized_time`, `speedup` (`naive_time / vectorized_time`).
- `compare_speed` internally converts its array inputs to lists for `naive_dot_product` — it doesn't change what's being measured, only which representation each implementation actually expects.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`naive_dot_product` is the dot product exactly as anyone would first write it without knowing NumPy exists: a loop, one multiplication and one addition per pair of elements.

</details>

<details>
<summary>Hint 2</summary>

`np.dot(a, b)` does the _entire_ dot product in one call, dispatching to a highly-optimized (often BLAS-backed) routine — there's no loop for Python to interpret one instruction at a time.

</details>
