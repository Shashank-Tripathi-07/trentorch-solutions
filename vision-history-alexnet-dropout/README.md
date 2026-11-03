# Note: AlexNet — Dropout, and What Actually Changed from LeNet

Beginner | computer-vision | cnn | history | regularization

### The problem, from first principles

AlexNet (2012) is usually credited with "starting" deep learning's modern era, but its architecture wasn't a radical departure from LeNet (1998) — it's a deeper stack of the same convolution/pool/fully-connected pattern. What actually mattered was a handful of practical changes that made a deep network trainable and generalizable at all: ReLU instead of sigmoid/tanh (avoiding vanishing gradients — see `02-deep-learning-core`'s activation questions), and dropout, a regularization technique that fights overfitting in the large fully-connected layers that dominate AlexNet's parameter count. This question implements dropout, since it's the one AlexNet-era idea concrete and self-contained enough to code and test directly.

### From theory to code

Theory says: during training, randomly and independently zero out each unit with some probability `p`, forcing the network to not rely on any single unit too heavily (since it might vanish on any given forward pass). To keep the _expected_ value of the output unchanged (so nothing downstream needs to know or care whether dropout is active), scale every unit that survives by `1 / (1 - p)`.

Implement `dropout_forward(x, p, rng)` against that reasoning.

### Constraints

- `x`: any-shape array of activations.
- `p`: drop probability, in `[0, 1)`.
- `rng`: a `numpy.random.Generator`, passed in explicitly so tests (and callers) can control and reproduce randomness.
- Returns an array the same shape as `x`, where each element is either exactly `0.0` (dropped) or `x[i] / (1 - p)` (kept and rescaled).
- `x` is never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`rng.random(x.shape)` draws one uniform `[0, 1)` value per element of `x` — compare it against `p` to decide, per element, whether to keep or drop.

</details>

<details>
<summary>Hint 2</summary>

`mask = (rng.random(x.shape) >= p).astype(x.dtype)` is 1.0 wherever a unit survives and 0.0 wherever it's dropped — `x * mask / (1 - p)` applies the mask and the inverted-dropout rescaling in one expression.

</details>
