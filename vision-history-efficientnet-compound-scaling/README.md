# Note: EfficientNet — Compound Scaling

Beginner | computer-vision | cnn | history | efficiency

### The problem, from first principles

If a CNN isn't accurate enough, the classic fix is to make it bigger — but "bigger" has three independent knobs: more layers (depth), more channels per layer (width), and larger input images (resolution). Scaling only one of these hits diminishing returns quickly: an extremely deep but narrow, low-resolution network wastes its depth on features too coarse to matter, and an extremely wide but shallow network can't build up the hierarchical features depth provides. EfficientNet's insight was that these three axes interact, so they should be scaled together, in a fixed, empirically-tuned ratio, controlled by a single number.

### From theory to code

Theory says: pick base per-step multipliers for depth, width, and resolution (`alpha`, `beta`, `gamma`), and scale all three simultaneously by raising each to the power of a single "compound coefficient" `phi` that the user chooses based on how much extra compute budget is available.

Implement `compound_scale(phi, alpha=1.2, beta=1.1, gamma=1.15)` against that reasoning.

### Constraints

- `phi`: a non-negative integer (`phi=0` means "the unscaled base model").
- `alpha`, `beta`, `gamma`: positive floats, each the base multiplier applied once per unit increase in `phi`.
- Returns a 3-tuple of floats: `(depth_mult, width_mult, resolution_mult)`.
- `phi=0` always returns `(1.0, 1.0, 1.0)` regardless of `alpha`/`beta`/`gamma`, since raising anything to the power 0 is 1.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Each multiplier is completely independent of the other two — there's no interaction between depth, width and resolution in the formula itself, only in how their base rates (`alpha`, `beta`, `gamma`) were chosen.

</details>

<details>
<summary>Hint 2</summary>

`alpha ** phi`, `beta ** phi`, `gamma ** phi` — that's the entire function.

</details>
