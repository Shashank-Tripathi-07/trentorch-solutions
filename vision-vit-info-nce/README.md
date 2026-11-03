# Stretch: InfoNCE Loss (CLIP-Style Contrastive Training)

Advanced | computer-vision | transformers | contrastive-learning

### The problem, from first principles

Everything so far in this track trains a ViT to predict a fixed, predefined set of class labels. CLIP trains an image encoder and a text encoder _jointly_, with no fixed classes at all — instead, given a batch of `N` genuinely matched (image, caption) pairs, it asks a purely relative question: "out of these `N` captions, which one actually goes with this image?" Solving that N-way matching problem, for every image AND every caption in the batch simultaneously, forces both encoders to place matching image/text pairs near each other in a shared embedding space, and everything else far apart — with no manually-labeled classes needed at all, since the "labels" are just which pairs happened to arrive in the batch together.

### From theory to code

Theory says: normalize every embedding to unit length (so only direction, not magnitude, matters), compute the full `N x N` matrix of image-to-text similarities, and treat row `i` of that matrix as an `N`-way classification problem where the correct answer is always class `i` (image `i` matches text `i`). Do this in BOTH directions — image-to-text and text-to-image — since the two are different classification problems with different softmax normalizations, and average the two resulting losses.

Implement `info_nce_loss(image_embeds, text_embeds, temperature=0.07)` against that reasoning.

### Constraints

- `image_embeds`, `text_embeds`: both shape `(N, D)`. Row `i` of each is a matched pair — this is the key assumption; there is no separate labels argument because the matching is implicit in row order.
- `temperature`: positive float scaling similarities before softmax; smaller values sharpen the resulting distribution.
- Returns a single Python `float`: the average of the image-to-text and text-to-image cross-entropy losses.
- Neither `image_embeds` nor `text_embeds` are modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`image_embeds / np.linalg.norm(image_embeds, axis=1, keepdims=True)` L2-normalizes every row — do the same for `text_embeds`. After normalizing, a dot product between two rows equals their cosine similarity.

</details>

<details>
<summary>Hint 2</summary>

`logits = (image_norm @ text_norm.T) / temperature` gives the `(N, N)` similarity matrix. `labels = np.arange(N)` says "row i's correct match is column i." `cce_loss(softmax(logits), labels)` scores the image-to-text direction; `cce_loss(softmax(logits.T), labels)` scores text-to-image (transposing swaps which axis is being classified over). Average the two.

</details>
