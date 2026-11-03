# Flatten: Bridging Convolutional and Linear Layers

Beginner | computer-vision | cnn

### The problem, from first principles

Everything built in `01-convolutions` and `02-pooling` operates on spatial data — arrays shaped `(C, H, W)`, where position matters. `01-classical-ml/01-linear-regression/01-hypothesis-function`'s `linear` operates on the opposite shape of assumption: a flat vector of features, no spatial structure at all. To connect a convolutional feature extractor to a `Linear` classifier head, something has to convert one shape convention into the other — that's flatten's entire job.

### From theory to code

Theory says there's no real computation here, only a reinterpretation: take every value in a `(C, H, W)` array and lay it out as one long 1D vector, in the same order the array is already stored in.

Implement `flatten(image)` against that reasoning.

### Constraints

- `image`: shape `(C, H, W)`.
- Output: shape `(C*H*W,)`.
- Order: channel-major, then row, then column — the same order `image.reshape(-1)` and `torch.flatten` both use by default.
- Every value must be preserved exactly, only the shape changes.
- `image` is never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

There's no computation to derive here — this is a single NumPy method call on `image`.

</details>

<details>
<summary>Hint 2</summary>

`.reshape(-1)` collapses every axis into one, in the array's existing memory order — exactly the channel-major, row-major order this question asks for.

</details>
