# Transposed Convolution

Intermediate | computer-vision | cnn | upsampling

### The problem, from first principles

A normal convolution shrinks (or preserves) spatial size — it never grows it. But plenty of tasks need the opposite: semantic segmentation needs a full-resolution output mask from a compressed feature map, and generative models need to turn a small latent representation into a full-size image. Something has to _learnably upsample_, and a transposed convolution is the standard way to do that: instead of sliding a kernel over the input and collapsing a patch into one output value, it takes each single input value and scatters a scaled copy of the kernel outward into the (larger) output.

### From theory to code

Theory says: build an all-zero output big enough to hold every scattered kernel copy, then for every input pixel, add that pixel's value times the kernel into the output window starting at that pixel's (stride-scaled) position — summing wherever windows from different input pixels overlap.

Implement `conv_transpose2d(x, kernel, stride=1)` against that reasoning, for the single-input-channel, single-output-filter case.

### Constraints

- `x`: shape `(1, H, W)`.
- `kernel`: shape `(1, 1, kH, kW)`.
- `stride`: positive integer controlling how far apart, in the output, consecutive input pixels' kernel copies are placed.
- Output shape: `(1, (H - 1) * stride + kH, (W - 1) * stride + kW)`.
- Overlapping contributions from different input pixels are summed, never overwritten.
- `x` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Compute `out_h = (H - 1) * stride + kH` and `out_w = (W - 1) * stride + kW` first, and allocate a zero array of that size before doing anything else.

</details>

<details>
<summary>Hint 2</summary>

Loop over every input pixel `(i, j)`: the window it contributes to starts at output position `(i * stride, j * stride)` and is `kH` by `kW` in size. Use `+=` (not `=`) so overlapping windows from different input pixels accumulate instead of clobbering each other.

</details>
