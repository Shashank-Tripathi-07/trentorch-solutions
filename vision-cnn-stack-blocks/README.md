# Stacking Multiple CNN Blocks

Intermediate | computer-vision | cnn

### The problem, from first principles

One CNN block (`02-one-cnn-block`) extracts one level of features and shrinks the spatial size once. A single block rarely learns anything rich enough for a real task — real image classifiers chain several blocks in sequence, each one operating on the PREVIOUS block's output rather than the raw image, so later blocks combine earlier features into progressively higher-level ones (edges → textures → parts → objects) while the spatial size keeps shrinking toward something small enough to flatten.

### From theory to code

Theory says: the first block sees the original image, and every later block sees the previous block's output. Chain them, feeding one into the next.

Implement `stack_cnn_blocks(image, kernels, pool_size=2)` against that reasoning, reusing `02-one-cnn-block`'s `cnn_block` once per kernel in the list.

### Constraints

- `image`: shape `(C_in, H, W)`.
- `kernels`: a list of kernels, one per block. Kernel `i`'s input-channel dimension must match block `i`'s actual input (either `image`'s own channels, for the first block, or the previous block's output channel count).
- `pool_size` is passed to every block identically.
- An empty `kernels` list returns `image` unchanged — zero blocks means no computation at all.
- `image` and every kernel in `kernels` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

A single loop over `kernels`, reassigning your running result each iteration — the same pattern as a training loop repeating one update rule.

</details>

<details>
<summary>Hint 2</summary>

Start with `x = image`, then for each `kernel` in `kernels`, set `x = cnn_block(x, kernel, pool_size=pool_size)`. Return `x` after the loop.

</details>
