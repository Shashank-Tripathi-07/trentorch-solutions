# Note: Feature Pyramids — Combining Multiple Resolutions

Beginner | computer-vision | cnn | history | detection

### The problem, from first principles

A CNN backbone naturally produces a stack of feature maps at shrinking resolutions as it goes deeper: early layers have high spatial resolution but only simple, low-level features (edges, colors); late layers have low spatial resolution but rich, high-level, semantically meaningful features (object parts, whole shapes). Object detection needs BOTH at once — precise spatial localization (which the early layers have) and confident semantic understanding of what's actually there (which only the late layers have). A Feature Pyramid Network (FPN) solves this by explicitly merging a late, low-resolution layer's features back into an earlier, high-resolution layer, combining the strengths of both.

### From theory to code

Theory says: to merge a high-resolution, low-level feature map with a low-resolution, high-level one, first upsample the low-resolution map so its spatial size matches the high-resolution one (FPN uses simple nearest-neighbor upsampling, not a learned transposed convolution, for speed and simplicity), and run a small 1x1 "lateral" convolution on the high-resolution map purely to make its channel count match the low-resolution map's — then add the two together.

Implement `nearest_upsample_2x(x)` and `fpn_merge(higher_res, lower_res, lateral_kernel)` against that reasoning.

### Constraints

- `nearest_upsample_2x(x)`: `x` shape `(C, H, W)` → returns shape `(C, 2H, 2W)`, each input pixel replicated into a 2x2 output block.
- `fpn_merge(higher_res, lower_res, lateral_kernel)`: `higher_res` shape `(C_high, 2H, 2W)`, `lower_res` shape `(C_low, H, W)` — exactly half `higher_res`'s spatial size — `lateral_kernel` shape `(C_low, C_high, 1, 1)`.
- Returns shape `(C_low, 2H, 2W)`.
- None of the inputs are modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`x.repeat(2, axis=1).repeat(2, axis=2)` repeats every row twice, then every column twice — together that turns each single pixel into a 2x2 block of identical copies (nearest-neighbor upsampling).

</details>

<details>
<summary>Hint 2</summary>

`pointwise_conv(higher_res, lateral_kernel)` projects `higher_res` from `C_high` to `C_low` channels (the "lateral connection") — add that to `nearest_upsample_2x(lower_res)`, which is already `C_low` channels and now the right spatial size too.

</details>
