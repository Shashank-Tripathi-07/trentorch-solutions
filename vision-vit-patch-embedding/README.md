# Patch Embedding

Beginner | computer-vision | transformers | vision-transformer

### The problem, from first principles

`01-patchify` turns an image into a sequence of flattened-patch vectors — but a transformer's tokens need to live in a fixed-size "embedding space" (dimension `d_model`) shared with everything else the transformer processes, and a flattened patch's raw pixel-vector length (`C * patch_size * patch_size`) has nothing to do with `d_model`. Something has to project every patch from "raw pixel space" into "embedding space." A word embedding table does this for word tokens by looking up a learned vector per word index; a ViT does the direct equivalent for patches with a learned linear projection, since a patch isn't a discrete symbol like a word — it's already a continuous vector.

### From theory to code

Theory says: apply a single, shared linear layer to every patch, mapping its raw `C*patch_size*patch_size`-dimensional pixel vector to a `d_model`-dimensional embedding — exactly the same linear transformation this curriculum's very first question already implemented for a completely different purpose.

Implement `patch_embedding(patches, weight, bias)` against that reasoning.

### Constraints

- `patches`: shape `(num_patches, C*patch_size*patch_size)`.
- `weight`: shape `(d_model, C*patch_size*patch_size)`.
- `bias`: shape `(d_model,)`.
- Returns shape `(num_patches, d_model)`.
- Every patch uses the exact same `weight` and `bias` (a single shared projection, not one per patch).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

This is not a new operation — it's `01-classical-ml/01-linear-regression/01-hypothesis-function`'s `linear(input, weight, bias)`, called with `patches` as the input.

</details>

<details>
<summary>Hint 2</summary>

`return linear(patches, weight, bias)` is the entire function body.

</details>
