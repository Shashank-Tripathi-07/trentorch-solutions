# Dilated Convolution

Intermediate | computer-vision | cnn | history | receptive-field

### The problem, from first principles

Growing a network's receptive field (how much of the input each output pixel "sees") the naive way costs something: bigger kernels mean more parameters, and stacking more layers means more depth and more downsampling (losing spatial resolution, which segmentation and dense-prediction tasks specifically can't afford to lose). Dilated ("atrous," from the French for "with holes") convolution grows the receptive field for free — same kernel, same parameter count — by spacing out where the kernel looks, skipping pixels between each tap instead of looking at a contiguous patch.

### From theory to code

Theory says: instead of a kernel scanning a contiguous `kH x kW` patch, spread its taps `dilation` pixels apart, so the same `kH x kW` set of weights now spans a `(kH-1)*dilation + 1` by `(kW-1)*dilation + 1` region of the input — the kernel's _effective_ footprint grows even though its _parameter count_ (`kH * kW`) doesn't.

Implement `dilated_conv2d(image, kernel, dilation=1)` against that reasoning.

### Constraints

- `image`: shape `(H, W)`.
- `kernel`: shape `(kH, kW)`.
- `dilation`: positive integer; `dilation=1` is an ordinary, non-dilated convolution.
- Output shape: `(H - eff_kH + 1, W - eff_kW + 1)`, where `eff_kH = (kH - 1) * dilation + 1` (same formula for `eff_kW`).
- `image` and `kernel` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Compute `eff_kH = (kH - 1) * dilation + 1` and `eff_kW` the same way, once, before the main loop — these are the true spatial span the kernel now reaches, even though the kernel array itself is still only `kH x kW`.

</details>

<details>
<summary>Hint 2</summary>

For output position `(i, j)`, the slice `image[i : i+eff_kH : dilation, j : j+eff_kW : dilation]` — note the `dilation` step — picks out exactly the `kH x kW` pixels the spread-out kernel taps land on, ready to multiply elementwise against `kernel` and sum.

</details>
