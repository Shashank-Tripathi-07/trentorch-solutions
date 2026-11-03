# DenseNet: Concatenating Every Previous Layer's Output

Intermediate | computer-vision | cnn | history | architecture

### The problem, from first principles

A residual connection (`04-modern-cnn-concepts/02-residual-connection`) helps gradients flow by _adding_ a layer's input to its output — but addition merges two feature maps into one, so whatever distinct information they each carried is now mixed together and can't be perfectly separated again downstream. DenseNet asks: what if, instead of merging, every layer's output were kept fully separate and simply _concatenated_ onto a growing stack that every subsequent layer gets to see in full? Every layer then has direct, unmodified access to every earlier layer's exact feature maps, not just an additive blend of them.

### From theory to code

Theory says: start with the input as the current "feature stack." For each layer, run a same-padded convolution and ReLU on the _entire current stack_ (not just the most recent layer's output), then concatenate that layer's result onto the stack, growing it by that layer's output channel count before the next layer runs.

Implement `dense_block(x, kernels)` against that reasoning.

### Constraints

- `x`: shape `(C, H, W)`.
- `kernels`: a list of 3x3 kernels. `kernels[i]`'s input-channel count must equal the running total of channels accumulated so far (`x`'s original channels plus every previous kernel's output channels).
- Every convolution uses padding 1 (spatial size never changes).
- Each layer's result is concatenated onto the _front-preserving_ running stack along the channel axis — the original `x` always remains the first channels of the final output.
- An empty `kernels` list returns `x` unchanged.
- `x` and every kernel are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Track a running `features` variable, starting as `x`. Each layer convolves `features` (the whole stack so far, not just `x`), producing a new set of channels.

</details>

<details>
<summary>Hint 2</summary>

`features = np.concatenate([features, new_layer_output], axis=0)` grows the channel axis after every layer — the next iteration's convolution then sees this larger `features` as its input, which is exactly why each `kernels[i]`'s input-channel count must match the running total.

</details>
