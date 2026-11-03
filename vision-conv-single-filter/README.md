# Single-Channel, Single-Filter 2D Convolution

Intermediate | computer-vision | convolutions

### The problem, from first principles

A `Linear` layer treats every input feature as independent — pixel (0, 0) and pixel (50, 50) get their own separate weight, with no notion that they're spatially near anything. That throws away the one fact that makes an image an image: nearby pixels are related, and the same small visual pattern (an edge, a corner) can show up anywhere in the frame.

A convolution fixes this by sliding one small, shared set of weights (a kernel) across every position in the image, computing the same local weighted sum wherever it lands. The same edge-detector kernel that works in the top-left corner works, unchanged, in the bottom-right — one small parameter set, reused everywhere, instead of one giant one used nowhere twice.

### From theory to code

Theory reduces this to one repeated operation: at every valid position, take the image patch directly under the kernel, multiply elementwise, and sum — a single number per position. Doing that at every position an unshifted kernel still fully overlaps the image (no padding yet, that's the next question) produces the whole output.

Implement `conv2d_single_filter(image, kernel)` against that reasoning. The signature and docstring are already in the editor.

### Constraints

- `image`: shape `(H, W)`.
- `kernel`: shape `(kH, kW)`.
- Output: shape `(H - kH + 1, W - kW + 1)` — "valid" convolution, no padding.
- This is cross-correlation, not textbook (flipped-kernel) convolution — matches what every deep learning framework calls "conv." Do not flip the kernel.
- `image` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

The output size shrinks because the kernel can't hang off the edge of the image — a `(kH, kW)` kernel has exactly `H - kH + 1` valid row positions to sit in.

</details>

<details>
<summary>Hint 2</summary>

For output position `(i, j)`, the corresponding image patch is `image[i : i+kH, j : j+kW]` — same top-left indexing you'd use to slice out any other sub-block.

</details>

<details>
<summary>Hint 3</summary>

`np.sum(patch * kernel)` is the entire computation for one output position. There's no matrix multiply here — just elementwise multiply, then sum everything.

</details>
