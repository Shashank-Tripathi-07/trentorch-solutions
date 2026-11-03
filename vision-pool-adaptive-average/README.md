# Adaptive Average Pooling: The Modern Flatten Replacement

Intermediate | computer-vision | pooling | global-average-pooling

### The problem, from first principles

`02-average-pooling` needs a fixed `kernel_size` chosen to match a specific input size. But a real classifier's final layers need a FIXED-size feature vector regardless of the input image's resolution — a `224x224` photo and a `256x256` photo should both end up feeding the same-sized `Linear` layer. Adaptive pooling flips the question around: instead of "pool with this window size," it asks "give me exactly THIS output size, whatever window size that takes."

Its most common special case — pooling every channel all the way down to a single number — is the modern replacement for flattening a whole feature map before the final classifier: instead of a huge, resolution-dependent flatten, one number per channel, always, no matter the input size.

### From theory to code

Theory says: for each output cell, figure out which region of the input it's responsible for (a formula, not a fixed window size), and average that region. The region boundaries are computed from `output_size` and the input's actual `H`, `W` — they aren't given directly the way `kernel_size` was in `02-average-pooling`.

Implement `adaptive_avg_pool2d(image, output_size=(1, 1))` against that reasoning.

### Constraints

- `image`: shape `(C, H, W)`.
- `output_size`: `(out_h, out_w)` — the exact output spatial shape to produce.
- Output: shape `(C, out_h, out_w)`.
- `output_size == (1, 1)` (the global-average-pooling case) must average every pixel in each channel exactly once.
- `output_size` equal to the input's own `(H, W)` must be the identity (every output cell covers exactly one input pixel).
- `image` is never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

For output row `i` (out of `out_h` total), the input rows it should cover start at `(i * H) // out_h` and end at `ceil((i + 1) * H / out_h)` — the same idea applies to columns with `out_w`, `W`.

</details>

<details>
<summary>Hint 2</summary>

`ceil(a / b)` for positive integers can be computed without floating point as `-(-a // b)` — negate, floor-divide, negate again.

</details>

<details>
<summary>Hint 3</summary>

When `H` divides evenly by `out_h`, every region ends up the same fixed size — in that special case this reduces exactly to `02-average-pooling`'s fixed-window pooling.

</details>
