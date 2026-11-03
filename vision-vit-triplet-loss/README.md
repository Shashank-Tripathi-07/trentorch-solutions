# Stretch: Triplet Loss (Metric/Representation Learning)

Intermediate | computer-vision | transformers | contrastive-learning

### The problem, from first principles

`06-info-nce-loss` compares one anchor against many candidates at once (an entire batch). Triplet loss asks the simplest possible version of the same underlying question, using just three examples at a time: given an anchor, a "positive" example that should be similar to it, and a "negative" example that should be dissimilar, push the anchor closer to its positive than to its negative, by at least some margin. It doesn't care about absolute distances at all — only the _relative_ ordering, which is exactly what makes it useful for learning an embedding space with no fixed set of classes (face recognition being the classic example: there's no finite list of "face classes," only "same person" vs. "different person" comparisons).

### From theory to code

Theory says: for each anchor/positive/negative triplet, compute the anchor's distance to its positive and its distance to its negative. If the negative is already farther away than the positive by at least `margin`, that triplet contributes nothing (loss 0) — the model already has it right, with room to spare. Otherwise, the loss is exactly how far short of that margin the triplet currently falls.

Implement `triplet_loss(anchor, positive, negative, margin=1.0)` against that reasoning.

### Constraints

- `anchor`, `positive`, `negative`: all shape `(N, D)` — row `i` across the three arrays forms one triplet.
- `margin`: a positive float, the minimum required gap between the two distances.
- Returns a single Python `float`: the mean per-triplet loss across all `N` triplets.
- None of the three inputs are modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.linalg.norm(anchor - positive, axis=1)` computes the Euclidean distance for every row at once — `axis=1` reduces across the feature dimension, leaving one distance per triplet.

</details>

<details>
<summary>Hint 2</summary>

`np.maximum(0.0, dist_to_positive - dist_to_negative + margin)` is the per-triplet hinge loss — then `.mean()` averages across triplets, and `float(...)` converts the resulting NumPy scalar to a plain Python float.

</details>
