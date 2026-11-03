# Multiple Output Filters

Intermediate | computer-vision | convolutions | channels

### The problem, from first principles

`04-multi-channel-input` combines every input channel into a single output number per position — one filter, one "opinion" about what's at each location. A real convolutional layer never stops at one opinion: it applies many independent filters to the same input at once, each one free to learn a different pattern (one might respond to vertical edges, another to a particular color blob), producing many output channels instead of one.

This is the last piece needed to reach `torch.nn.functional.conv2d`'s actual signature: many input channels in, many output channels out, each output channel its own independent multi-channel filter over the same input.

### From theory to code

Theory says nothing new mathematically — it's `04-multi-channel-input`'s exact computation, run once per output filter, with the results stacked along a new leading axis.

Implement `conv2d_multi_filter(image, kernel)` against that reasoning, reusing `conv2d_multi_channel` rather than reimplementing anything.

### Constraints

- `image`: shape `(C_in, H, W)`.
- `kernel`: shape `(C_out, C_in, kH, kW)` — `C_out` independent filters, each shaped like `04-multi-channel-input`'s kernel.
- Output: shape `(C_out, H - kH + 1, W - kW + 1)`.
- `C_out = 1` must reduce exactly to `04-multi-channel-input`'s output, with a leading size-1 axis.
- `image` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Loop over the first axis of `kernel` (size `C_out`). Each `kernel[f]` is a `(C_in, kH, kW)` array — exactly what `04-multi-channel-input`'s `conv2d_multi_channel` expects.

</details>

<details>
<summary>Hint 2</summary>

Allocate the output as `(C_out, H_out, W_out)` up front and assign into `output[f]` for each filter, rather than building a Python list and stacking at the end — either works, but preallocating keeps the shape contract explicit.

</details>
