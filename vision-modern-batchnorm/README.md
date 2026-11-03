# Batch Normalization

Intermediate | computer-vision | cnn | normalization

### The problem, from first principles

Deep networks are hard to train because the distribution of activations flowing into each layer keeps shifting as the parameters of every earlier layer change during training. A layer that learned to work well with inputs centered around 0 with unit spread can suddenly see inputs centered around 50 a few steps later, and has to re-adapt. Batch normalization fixes this by explicitly re-centering and re-scaling the activations of every channel, every forward pass, using statistics computed from the current batch.

### From theory to code

Theory says: for each channel, compute the mean and variance of that channel's values across the whole batch (and across every spatial position), use them to standardize that channel to zero mean and unit variance, then apply a learned per-channel scale (`gamma`) and shift (`beta`) so the network can undo the standardization if that turns out to be better for a particular channel.

Implement `batch_norm2d(x, gamma, beta, eps=1e-5)` against that reasoning.

### Constraints

- `x`: shape `(N, C, H, W)` — a batch of feature maps.
- `gamma`, `beta`: shape `(C,)` — one learned scale and shift per channel.
- Statistics (mean, variance) are computed per channel, over the `N`, `H` and `W` axes together — not per-sample, not per-spatial-position.
- `eps` is added inside the square root purely to avoid division by zero when a channel's variance is (near) zero.
- Returns an array the same shape as `x`.
- `x`, `gamma` and `beta` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`x.mean(axis=(0, 2, 3), keepdims=True)` and `x.var(axis=(0, 2, 3), keepdims=True)` compute exactly the per-channel batch statistics you need, and `keepdims=True` keeps them broadcastable against the original `(N, C, H, W)` shape.

</details>

<details>
<summary>Hint 2</summary>

`gamma` and `beta` are shape `(C,)` but need to broadcast against `(N, C, H, W)` — reshape each to `(1, C, 1, 1)` before multiplying/adding.

</details>
