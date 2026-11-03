# Note: Alignment Tax, the Capability Cost of Aligning a Model

Beginner | reinforcement-learning | nlp | metrics-and-evaluation

### The problem, from first principles

`12-reward-hacking-goodharts-law` showed that optimizing a proxy reward too hard can actively hurt what you truly care about. There's a related, equally real cost worth measuring directly: even a WELL-aligned model (genuinely more helpful, honest, and harmless) can lose some raw capability on standard benchmarks compared to its un-aligned base model: a real, quantifiable tradeoff the original InstructGPT paper explicitly measured and reported, rather than a purely hypothetical worry.

### From theory to code

Implement `alignment_tax` (the average capability regression across a suite of benchmarks), `per_benchmark_regression` (the same comparison, unaveraged), and `has_net_alignment_tax`.

### Constraints

- `alignment_tax(base_model_scores, aligned_model_scores)` returns `mean(base_model_scores - aligned_model_scores)`.
- `per_benchmark_regression(base_model_scores, aligned_model_scores)` returns the elementwise difference, one entry per benchmark.
- `has_net_alignment_tax(...)` returns `True` exactly when `alignment_tax(...) > 0`.
- A positive `alignment_tax` means the aligned model is, ON AVERAGE, less capable than the base model it came from; it's possible for `per_benchmark_regression` to show BOTH gains and losses across different benchmarks even when the net tax is exactly zero.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`alignment_tax` is nothing more than `per_benchmark_regression(...).mean()`: the whole exercise is really about getting the SIGN of the subtraction right (base minus aligned, so a positive number means capability was LOST).

</details>

<details>
<summary>Hint 2</summary>

A model can genuinely improve on some benchmarks (alignment sometimes helps instruction-following-style tasks) while regressing on others (raw completion-style tasks): `per_benchmark_regression` is what lets you see that full, mixed picture, rather than a single averaged number hiding it.

</details>
