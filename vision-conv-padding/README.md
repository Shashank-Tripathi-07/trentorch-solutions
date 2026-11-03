# Padding: Same vs. Valid

Beginner | computer-vision | convolutions | padding

### The problem, from first principles

`01-single-filter-conv2d`'s output is always smaller than its input — a kernel can't hang off the edge, so every convolution shrinks the image a little. Stack enough convolutional layers and an image eventually shrinks to nothing, which is rarely what you want for a deep network's middle layers.

The fix is to give the kernel somewhere to go at the edges: surround the image with a border of zeros first, wide enough that the kernel can center itself on every original pixel, including the ones right at the edge. Do that and the output comes out the same size as the input went in.

### From theory to code

Theory gives two modes: `"valid"` is exactly what `01-single-filter-conv2d` already does — no border, output shrinks. `"same"` adds a zero border of the right width first, then runs the identical convolution.

Implement `conv2d_with_padding(image, kernel, padding="valid")` against that reasoning, reusing `01-single-filter-conv2d`'s `conv2d_single_filter` rather than reimplementing the sliding-window logic.

### Constraints

- `image`: shape `(H, W)`. `kernel`: shape `(kH, kW)`, both dimensions odd.
- `padding="valid"`: no padding, output shape `(H - kH + 1, W - kW + 1)`.
- `padding="same"`: zero-pad by `(kH-1)//2` and `(kW-1)//2` on each side per axis, output shape exactly `(H, W)`.
- Any other `padding` value raises `ValueError`.
- `image` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`"valid"` needs no new logic at all — it's a direct call to `conv2d_single_filter`.

</details>

<details>
<summary>Hint 2</summary>

`np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)))` adds a zero border of `pad_h` rows and `pad_w` columns on every side. Compute `pad_h`, `pad_w` from the kernel's shape, then convolve the padded image exactly as in `"valid"`.

</details>
