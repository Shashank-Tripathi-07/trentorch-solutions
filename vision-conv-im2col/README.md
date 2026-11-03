# Stretch: im2col — Turning Convolution into One Matrix Multiply

Advanced | computer-vision | convolutions | optimization

### The problem, from first principles

`05-multiple-output-filters` computes one number per `(filter, output position)` pair via a Python loop, each iteration doing its own small elementwise-multiply-and-sum. That's correct, but it's exactly the kind of code that's slow in Python and doesn't map well onto how real hardware (GPUs, and CPUs with BLAS libraries) actually gets its speed: from doing a small number of very large matrix multiplies, not a huge number of tiny reductions.

im2col is the trick that closes that gap: gather every sliding-window patch the convolution would visit into the rows of one big matrix, flatten every filter into the rows of another, and replace the entire nested loop with a single matrix multiply. Same answer, computed the way real convolution implementations actually compute it.

### From theory to code

Theory says: every output position corresponds to one row of a "columns" matrix (the flattened patch at that position), and every output filter corresponds to one row of a flattened kernel matrix. Multiplying those two matrices together produces every `(position, filter)` output value at once.

Implement `conv2d_im2col(image, kernel)` against that reasoning — same contract as `05-multiple-output-filters`, different computation strategy.

### Constraints

- `image`: shape `(C_in, H, W)`. `kernel`: shape `(C_out, C_in, kH, kW)`.
- Output: shape `(C_out, H - kH + 1, W - kW + 1)`, numerically identical to `05-multiple-output-filters`'s output for the same inputs.
- The reduction over `(C_in, kH, kW)` for every `(position, filter)` pair must happen via a single matrix multiply, not a Python loop over output positions.
- `image` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.lib.stride_tricks.sliding_window_view(image, (kH, kW), axis=(1, 2))` returns every `(kH, kW)` patch, for every channel and every valid position, without a Python loop — shape `(C_in, out_h, out_w, kH, kW)`.

</details>

<details>
<summary>Hint 2</summary>

Rearrange those patches so each output position becomes one row: transpose to put `out_h, out_w` first, then reshape to `(out_h*out_w, C_in*kH*kW)`. Flatten `kernel` to `(C_out, C_in*kH*kW)` the same way, then it's one matrix multiply: `cols @ kernel_flat.T`, shape `(out_h*out_w, C_out)`.

</details>

<details>
<summary>Hint 3</summary>

The matmul's output has positions along one axis and filters along the other — transpose and reshape it back to `(C_out, out_h, out_w)` to match the expected output shape.

</details>
