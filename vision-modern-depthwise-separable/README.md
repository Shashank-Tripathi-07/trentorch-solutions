# Depthwise-Separable Convolution

Advanced | computer-vision | cnn | efficiency

### The problem, from first principles

A regular `(C_out, C_in, kH, kW)` convolution does two jobs at once, every single output pixel: it looks at a spatial neighborhood (spatial filtering) _and_ it combines every input channel together (channel mixing). Doing both jobs simultaneously means the cost scales with `C_out * C_in * kH * kW` — with enough channels, that's the majority of the compute in a modern CNN. Depthwise-separable convolution asks: what if these two jobs were split into two separate, much cheaper steps instead of one expensive combined one?

### From theory to code

Theory says: first, filter each input channel completely independently with its own small spatial kernel (the "depthwise" stage — no channel mixing at all, reusing `01-single-filter-conv2d`). Then, mix the resulting channels together with a 1x1 convolution (the "pointwise" stage — no spatial filtering at all, reusing `03-1x1-convolution`). Chaining these two cheap stages approximates what one expensive full convolution would have done, at a fraction of the compute.

Implement `depthwise_separable_conv2d(x, depthwise_kernel, pointwise_kernel)` against that reasoning.

### Constraints

- `x`: shape `(C_in, H, W)`.
- `depthwise_kernel`: shape `(C_in, 1, kH, kW)` — exactly one spatial filter per input channel, applied to that channel only.
- `pointwise_kernel`: shape `(C_out, C_in, 1, 1)` — mixes the depthwise stage's channels into `C_out` output channels.
- Returns shape `(C_out, H - kH + 1, W - kW + 1)`.
- `x`, `depthwise_kernel` and `pointwise_kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

The depthwise stage is a plain Python loop: `[conv2d_single_filter(x[c], depthwise_kernel[c, 0]) for c in range(C_in)]`, one independent 2D convolution per channel with no interaction between channels.

</details>

<details>
<summary>Hint 2</summary>

`np.stack(...)` the list of per-channel depthwise outputs back into one `(C_in, H', W')` array, then pass that straight into `pointwise_conv` with `pointwise_kernel` to get the final `(C_out, H', W')` result.

</details>
