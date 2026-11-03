# Average Pooling: Downsampling by Smoothing Instead of Selecting

Beginner | computer-vision | pooling

### The problem, from first principles

`01-max-pooling` keeps only a window's single loudest value, discarding everything else outright — a deliberate, sometimes aggressive choice. Average pooling makes the opposite choice: instead of picking a winner, it blends every value in the window into one smoothed number, so a single unusually large or small pixel doesn't dominate the result the way it would under max pooling.

Both are valid ways to shrink a feature map; which one helps depends on whether you want the network to notice "did this pattern fire strongly anywhere" (max) or "what's the overall level of activity here" (average).

### From theory to code

Theory changes exactly one operation from `01-max-pooling`: replace the per-window maximum with the per-window mean. Everything about how windows are laid out and stepped through stays identical.

Implement `avg_pool2d(image, kernel_size, stride=None)` against that reasoning.

### Constraints

- `image`: shape `(C, H, W)`.
- `kernel_size`: the pooling window's height and width.
- `stride`: step between windows; if `None`, defaults to `kernel_size` (non-overlapping pooling).
- Output: shape `(C, (H - kernel_size)//stride + 1, (W - kernel_size)//stride + 1)`.
- Every value inside a window contributes equally to that window's output — no weighting, no learned parameters.
- `image` is never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

This is `01-max-pooling` with one line changed: `.mean(axis=(1, 2))` instead of `.max(axis=(1, 2))` on each window.

</details>

<details>
<summary>Hint 2</summary>

`window.mean(axis=(1, 2))` on a `(C, kernel_size, kernel_size)` slice reduces over just the spatial axes in one call, leaving one averaged value per channel.

</details>
