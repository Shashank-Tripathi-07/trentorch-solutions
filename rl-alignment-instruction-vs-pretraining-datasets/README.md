# Instruction Datasets: Prompt/Response Pairs vs. Raw Next-Token Pretraining

Beginner | reinforcement-learning | nlp

### The problem, from first principles

`01-supervised-fine-tuning-response-loss-mask` implemented the LOSS-masking mechanics of SFT, but it took for granted that a "prompt" and "response" were already separated. This question builds the actual data structure a real instruction-tuning dataset uses, and quantifies exactly how it differs from a raw pretraining example: not just "different content", but a structurally different relationship between the tokens and the loss.

### From theory to code

Implement `build_instruction_example` (turning a prompt/response pair into one training example with its own loss mask), `build_pretraining_example` (the raw-pretraining equivalent, with no prompt/response distinction), and `fraction_of_tokens_supervised`, quantifying the difference directly.

### Constraints

- `build_instruction_example(prompt_ids, response_ids, eos_token_id)` concatenates `prompt_ids + response_ids + [eos_token_id]`, with a `loss_mask` that's `False` over the prompt and `True` over the response AND the trailing EOS token.
- `build_pretraining_example(token_ids)` returns the tokens with a `loss_mask` that's `True` everywhere.
- `fraction_of_tokens_supervised(example)` returns the mean of `example["loss_mask"]`.
- A pretraining example's supervised fraction is always exactly `1.0`; an instruction example's is always strictly less than `1.0` whenever the prompt is nonempty.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

The EOS token belongs in the SUPERVISED region, not the prompt: the model needs to learn to predict "stop generating now" just as much as it needs to learn the actual response content.

</details>

<details>
<summary>Hint 2</summary>

`build_instruction_example`'s `loss_mask` is exactly `[False] * len(prompt_ids) + [True] * (len(response_ids) + 1)`: the `+1` accounts for the trailing EOS token also being supervised.

</details>
