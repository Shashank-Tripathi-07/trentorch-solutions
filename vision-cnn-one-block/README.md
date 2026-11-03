# One CNN Block: Convolution, Activation, Pooling

Intermediate | computer-vision | cnn

### The problem, from first principles

A convolution alone is just a linear operation — stack two of them back to back with nothing in between and they collapse into one bigger linear operation, no more expressive than a single layer. Real networks need a nonlinearity between layers to actually gain expressive power, and they need periodic downsampling or the spatial size never shrinks. The standard building block that does both is exactly three operations in sequence: convolve, activate, pool.

This is the repeating unit nearly every classic CNN (LeNet, AlexNet, VGG) is built from — stack a few of these blocks (`03-stack-multiple-blocks`) and you have a feature extractor.

### From theory to code

Theory says the block is a strict pipeline: the convolution's output feeds directly into the activation, and the activation's output feeds directly into pooling. No new math — every piece already exists.

Implement `cnn_block(image, kernel, pool_size=2)` against that reasoning, reusing `05-multiple-output-filters`'s convolution, `02-deep-learning-core/02-activations/01-relu`'s ReLU, and `01-max-pooling`'s pooling.

### Constraints

- `image`: shape `(C_in, H, W)`. `kernel`: shape `(C_out, C_in, kH, kW)`.
- Order is fixed: convolve, then ReLU, then max-pool — never a different order.
- `pool_size` is passed straight through to the pooling step as its `kernel_size` (non-overlapping, stride defaults to `pool_size`).
- `image` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Three function calls, each one's output feeding the next one's input — no loop, no new arithmetic.

</details>

<details>
<summary>Hint 2</summary>

`conv2d_multi_filter(image, kernel)` → `relu_forward(...)` → `max_pool2d(..., kernel_size=pool_size)`, in that exact order.

</details>
