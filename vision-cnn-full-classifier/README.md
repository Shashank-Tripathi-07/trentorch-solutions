# Full CNN Classifier

Advanced | computer-vision | cnn | classification

### The problem, from first principles

Every piece needed for an actual image classifier already exists across this curriculum: a convolutional backbone that extracts features (`03-stack-multiple-blocks`), a way to flatten those features into a vector (`01-flatten`), a `Linear` layer that turns a feature vector into class scores (`01-classical-ml/01-linear-regression/01-hypothesis-function`), and softmax plus cross-entropy to turn those scores into probabilities and a trainable loss (`01-classical-ml/02-classification/06-softmax-cce`). This question is the capstone: wire all of them into one real, working classifier's forward pass.

### From theory to code

Theory says: run each image through the convolutional backbone, flatten the result, stack a whole batch of flattened vectors into one matrix, run that matrix through the final `Linear` layer, then softmax. If true labels are given, also score the result with cross-entropy — this is a genuine, if small, image classifier.

Implement `full_cnn_classifier(images, kernels, fc_weight, fc_bias, labels=None, pool_size=2)` against that reasoning, reusing every piece named above rather than reimplementing any of them.

### Constraints

- `images`: shape `(N, C, H, W)` — a batch of `N` images.
- `kernels`: list of conv kernels, passed straight through to `03-stack-multiple-blocks`.
- `fc_weight`: shape `(num_classes, flattened_feature_dim)`. `fc_bias`: shape `(num_classes,)`.
- `labels`: optional, shape `(N,)`, integer class indices.
- Returns `probs` (shape `(N, num_classes)`, rows summing to 1) if `labels is None`; otherwise returns `(probs, loss)` where `loss` is a plain Python float.
- `images`, every kernel, `fc_weight` and `fc_bias` are never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Process each image in the batch independently through the CNN backbone and flatten (`03-stack-multiple-blocks` and `01-flatten` both operate on a single image, with no batch dimension) — a list comprehension over `images`, then `np.stack` the results, turns that back into a proper `(N, flattened_dim)` batch matrix.

</details>

<details>
<summary>Hint 2</summary>

Once you have the `(N, flattened_dim)` matrix, everything downstream is exactly `01-classical-ml`'s classification pipeline: `linear(...)` for logits, `softmax(...)` for probabilities, `cce_loss(...)` if labels were given.

</details>
