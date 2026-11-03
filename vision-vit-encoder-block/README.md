# Feed Through the Transformer Block, Unmodified

Intermediate | computer-vision | transformers | vision-transformer

### The problem, from first principles

Every step so far — patchify, patch embedding, CLS token + position embedding — existed purely to reshape an image into something that looks EXACTLY like a language transformer's input: a sequence of `d_model`-dimensional vectors. This question is the payoff for that work: the transformer block itself needs no vision-specific code whatsoever. Self-attention computes relationships between sequence positions using nothing but dot products and softmax — it has no built-in concept of "image" or "sentence," so a block already built and tested for language modeling works on patch sequences without a single line changed.

### From theory to code

Theory says: this curriculum already has a fully assembled, tested transformer block (`05-transformers-llm/01-transformer-block/06-assemble-full-block`). It expects a batch dimension (`(batch, seq_len, d_model)`); a single image's sequence has none. Add a batch dimension of size 1, run the existing block completely unmodified, then remove the batch dimension from the result.

Implement `vit_encoder_block(sequence, num_heads, ...)` against that reasoning.

### Constraints

- `sequence`: shape `(seq_len, d_model)` — the output of `03-cls-token-position-embedding`, no batch dimension.
- All other parameters are passed straight through to `transformer_block_forward`, unchanged.
- Returns shape `(seq_len, d_model)` — same shape as `sequence`.
- `sequence` is never modified in place.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`sequence[None, :, :]` inserts a new axis at the front, turning `(seq_len, d_model)` into `(1, seq_len, d_model)` — a "batch" of exactly one image.

</details>

<details>
<summary>Hint 2</summary>

`transformer_block_forward(batched_sequence, num_heads, ...)` returns shape `(1, seq_len, d_model)` — index `[0]` on the result strips the batch dimension back off.

</details>
