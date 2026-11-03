# Class Token + Position Embedding

Intermediate | computer-vision | transformers | vision-transformer

### The problem, from first principles

Two problems remain before a sequence of patch embeddings is ready for a transformer. First: attention has no built-in sense of "position" — it computes weighted averages over a _set_ of vectors, so shuffling every patch in the sequence and running the exact same transformer would produce identically-shuffled output, with no way for the model to know patch 5 was originally in the top-right corner rather than the bottom-left. Second: a transformer produces one output vector _per input position_ — for classification, something has to decide which position's final output actually represents "the whole image." ViT solves both with ideas borrowed directly from BERT: a learned position embedding added to every patch (fixing problem one), and a dedicated, learned "CLS token" prepended to the sequence, whose job is purely to end up holding a summary of the whole image after attention has let it look at every patch (fixing problem two).

### From theory to code

Theory says: prepend the (single, shared, learned) CLS token vector to the front of the patch embedding sequence, then add a learned position embedding — one vector per sequence position, including the CLS token's own position 0 — elementwise to the whole sequence.

Implement `add_cls_token_and_position_embedding(patch_embeddings, cls_token, position_embedding)` against that reasoning.

### Constraints

- `patch_embeddings`: shape `(num_patches, d_model)`.
- `cls_token`: shape `(1, d_model)`.
- `position_embedding`: shape `(num_patches + 1, d_model)`.
- Returns shape `(num_patches + 1, d_model)`.
- The CLS token occupies sequence position 0; the original patches follow in their original order at positions 1 through `num_patches`.
- None of the inputs are modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.concatenate([cls_token, patch_embeddings], axis=0)` stacks `cls_token` in front of `patch_embeddings` along the sequence axis, giving a `(num_patches + 1, d_model)` array.

</details>

<details>
<summary>Hint 2</summary>

Once concatenated, adding `position_embedding` is a plain elementwise addition — both arrays are now the same `(num_patches + 1, d_model)` shape.

</details>
