# Patchify an Image into Fixed-Size Patches

Intermediate | computer-vision | transformers | vision-transformer

### The problem, from first principles

A transformer operates on a _sequence_ of tokens — that's the entire premise of everything in `05-transformers-llm`'s attention and transformer-block questions. An image isn't naturally a sequence at all; it's a 2D (or 3D, with channels) grid. The Vision Transformer's founding idea is disarmingly simple: chop the image into a grid of fixed-size square patches, treat each patch as if it were one "token," and feed the resulting sequence of patches through an ordinary transformer, completely unmodified from how it processes word tokens.

### From theory to code

Theory says: split the image into a regular grid of non-overlapping `patch_size x patch_size` squares (covering every channel), then flatten each individual patch (all its channels and pixels) down into one single vector — turning a `(C, H, W)` image into a `(num_patches, C*patch_size*patch_size)` sequence of flattened-patch vectors.

Implement `patchify(image, patch_size)` against that reasoning.

### Constraints

- `image`: shape `(C, H, W)`, with both `H` and `W` divisible by `patch_size`.
- `patch_size`: side length of each square patch.
- Returns shape `(num_patches, C * patch_size * patch_size)`, where `num_patches = (H // patch_size) * (W // patch_size)`.
- Patches are ordered row-major over the patch grid: left-to-right within a row of patches, then top-to-bottom across rows.
- `image` is never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`image.reshape(C, n_h, patch_size, n_w, patch_size)` (with `n_h = H // patch_size`, `n_w = W // patch_size`) splits `H` and `W` into "which patch" and "which pixel within that patch" without moving any data — reshape alone can do this because `H` and `W` are exact multiples of `patch_size`.

</details>

<details>
<summary>Hint 2</summary>

After that reshape, `.transpose(1, 3, 0, 2, 4)` moves the two grid axes (`n_h`, `n_w`) to the front, giving shape `(n_h, n_w, C, patch_size, patch_size)` — now a final `.reshape(n_h * n_w, C * patch_size * patch_size)` flattens the patch grid into a sequence and each patch's own data into one vector, in one step.

</details>
