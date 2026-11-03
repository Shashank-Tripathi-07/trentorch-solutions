# Gram Matrix & Style

Intermediate | computer-vision | style-transfer | features | gram-matrix

### The problem, from first principles

What is the "style" of a painting, as opposed to its content? Gatys and colleagues made the idea precise with the feature maps of a pretrained CNN. A layer produces `C` feature maps over `H x W` positions. The **content** is _where_ features fire. The **style** is _which features fire together_, regardless of position, and that is exactly what the **Gram matrix** records: entry `(i, j)` is the inner product of feature map `i` with feature map `j`, summed over all positions. Swirly brushstrokes make certain channels co-activate everywhere, and the position information, which says where the swirls are, has been summed away.

### From theory to code

Implement `gram_matrix`.

### Constraints

- `features` has shape `(C, H, W)`. Flatten each channel to a vector of length `H * W`, giving `F` of shape `(C, H * W)`.
- Return `F @ F.T / (C * H * W)`, a symmetric `(C, C)` matrix. The normalization makes values comparable across layers of different sizes.

### Hints

<details>
<summary>Hint 1</summary>

`features.reshape(C, -1)` flattens the spatial dimensions.

</details>

<details>
<summary>Hint 2</summary>

Moving the same texture to a different position leaves the Gram matrix unchanged, which the tests check.

</details>
