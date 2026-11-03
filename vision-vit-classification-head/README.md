# Classification Head

Beginner | computer-vision | transformers | vision-transformer

### The problem, from first principles

After the transformer block runs, the sequence still has `seq_len` positions — one for the CLS token, one per patch. For whole-image classification, only one final number per class is wanted, not one per sequence position. Everything from `03-cls-token-position-embedding` onward was specifically designed to funnel a summary of the entire image into the CLS token's position through attention, which is exactly why classification only ever looks at that one position and throws every patch position's final output away.

### From theory to code

Theory says: take the CLS token's final representation (position 0 of the transformer's output sequence), run it through a linear layer mapping `d_model` to `num_classes`, then softmax to turn the resulting logits into a probability distribution over classes — the exact same classification pipeline `01-classical-ml/02-classification` already built, just fed a learned feature vector instead of raw tabular features.

Implement `classification_head(sequence, weight, bias)` against that reasoning.

### Constraints

- `sequence`: shape `(seq_len, d_model)` — the transformer block's output.
- `weight`: shape `(num_classes, d_model)`. `bias`: shape `(num_classes,)`.
- Returns shape `(num_classes,)`: a probability distribution (non-negative, summing to 1).
- Only `sequence[0]` (the CLS token) affects the output — every other position is ignored entirely.
- `sequence`, `weight` and `bias` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`sequence[0]` pulls out the CLS token's row, shape `(d_model,)` — but `linear` and `softmax` both expect a 2D `(batch, features)` input, so wrap it as `sequence[0][None, :]` (or equivalently `sequence[0:1]`) to get shape `(1, d_model)`.

</details>

<details>
<summary>Hint 2</summary>

`softmax(linear(cls_token_row, weight, bias))` returns shape `(1, num_classes)` — index `[0]` on the result to get the plain `(num_classes,)` vector this question asks for.

</details>
