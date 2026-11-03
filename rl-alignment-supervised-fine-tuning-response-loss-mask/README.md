# Supervised Fine-Tuning: Next-Token Loss, But Only on the Response Tokens

Intermediate | reinforcement-learning | nlp | neural-networks

### The problem, from first principles

Raw language-model pretraining trains next-token prediction on every single token in a corpus, with no notion of "the model's own turn" versus "context it was given". Supervised fine-tuning (SFT), the first step of turning a raw pretrained model into something that follows instructions, reuses the exact same next-token loss, but with one crucial change: the loss is only computed on the tokens the model is actually supposed to have generated, never on the prompt it was handed.

### From theory to code

Implement `make_response_mask` (marking which positions count) and `sft_loss` (the loss, restricted to those positions), reusing `dl-core-cross-entropy-loss`'s per-token cross-entropy directly, plus `raw_pretraining_loss` as the contrasting baseline.

### Constraints

- `make_response_mask(prompt_len, total_len)` returns a length-`total_len` boolean array, `False` for the first `prompt_len` positions and `True` after.
- `sft_loss(logits, targets, prompt_len)` averages the per-token cross-entropy loss ONLY over the response (masked-`True`) positions.
- `raw_pretraining_loss(logits, targets)` is the ordinary mean cross-entropy over every position, with no masking at all.
- Corrupting the prompt-region logits must never change `sft_loss`'s value.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`cross_entropy_forward(logits, targets, reduction="none")` (from `dl-core-cross-entropy-loss`) gives you the loss at every position individually: `sft_loss` is just that array, indexed by the response mask, then averaged.

</details>

<details>
<summary>Hint 2</summary>

`make_response_mask` is one line: start with an all-`False` array of length `total_len`, then set the slice `[prompt_len:]` to `True`.

</details>
