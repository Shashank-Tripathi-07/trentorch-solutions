# VGG: Stacking Small 3x3 Convolutions

Intermediate | computer-vision | cnn | history | architecture

### The problem, from first principles

A single 5x5 convolution and two stacked 3x3 convolutions both let a pixel's output "see" a 5x5 neighborhood of the original input (their receptive fields match) — but they are not equivalent networks. The two-3x3 version has a ReLU sandwiched between the two convolutions, giving the network an extra nonlinearity for the same receptive field, and it has fewer parameters: `2 * (C^2 * 3 * 3) = 18*C^2` versus `C^2 * 5 * 5 = 25*C^2` for equal channel counts `C`. VGG's core insight, which became the default choice for essentially every CNN architecture afterward, is: stop reaching for large kernels — just stack more small (3x3) ones.

### From theory to code

Theory says: apply a same-padded 3x3 convolution, then a ReLU, then repeat with the next kernel in the stack, feeding each layer's output into the next as input.

Implement `vgg_stack(x, kernels)` against that reasoning, reusing this track's existing multi-filter convolution and ReLU.

### Constraints

- `x`: shape `(C, H, W)`.
- `kernels`: a list of 3x3 kernels, each shape `(C, C, 3, 3)` (channel count stays fixed through the stack).
- Every convolution uses padding 1 (so spatial size never changes, no matter how many layers are stacked).
- An empty `kernels` list returns `x` unchanged.
- Returns an array the same shape as `x`.
- `x` and every kernel are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

A plain `for kernel in kernels:` loop, reassigning `x` to the result of each iteration, is all the "stacking" is — each layer's output becomes the next layer's input.

</details>

<details>
<summary>Hint 2</summary>

Inside the loop: `np.pad` by 1 pixel on H and W, run `conv2d_multi_filter`, then `relu_forward` the result, and that becomes the new `x` for the next iteration.

</details>
