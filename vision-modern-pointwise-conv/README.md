# 1x1 Convolution (Bottleneck)

Intermediate | computer-vision | cnn | architecture

### The problem, from first principles

Every convolution seen so far mixes information across a spatial neighborhood — a 3x3 kernel looks at a 3x3 patch. A 1x1 kernel is the degenerate case: it looks at exactly one pixel, so it can never mix spatial information at all. That sounds useless, but it does something else that's extremely valuable: it mixes information _across channels_ at each pixel independently, letting a network cheaply change how many channels it's carrying (e.g. compress 256 channels down to 64 — a "bottleneck") without touching the spatial structure at all.

### From theory to code

Theory says: since a 1x1 convolution never looks past a single pixel, every output pixel is just a fixed linear combination of that same pixel's input channels — the exact same `(C_out, C_in)` weight matrix applied at every spatial location. That means the whole operation can be done as one reshape and one matrix multiply, with no loop over spatial positions at all.

Implement `pointwise_conv(x, kernel)` against that reasoning.

### Constraints

- `x`: shape `(C_in, H, W)`.
- `kernel`: shape `(C_out, C_in, 1, 1)`.
- Returns shape `(C_out, H, W)` — same spatial size as `x`, remapped channel count.
- `x` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`kernel.reshape(C_out, C_in)` squeezes away the two trailing size-1 dimensions, turning the 1x1 conv kernel into a plain weight matrix.

</details>

<details>
<summary>Hint 2</summary>

`x.reshape(C_in, H * W)` turns every pixel's channel vector into one column of a `(C_in, H*W)` matrix — `weight @ x_flat` then applies the same linear map to every column (every pixel) at once. Reshape the `(C_out, H*W)` result back to `(C_out, H, W)`.

</details>
