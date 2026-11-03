# Note: Adapter Methods, Prefix Tuning and Prompt Tuning, Other Parameter-Efficient Approaches

Beginner | reinforcement-learning | nlp | neural-networks

### The problem, from first principles

`14-qlora-quantized-lora`'s LoRA adds a trainable low-rank matrix INSIDE each `Linear` layer's computation. That's not the only way to fine-tune a frozen base model cheaply: a whole family of "adapter" methods instead adds small, trainable pieces AROUND the frozen model, without touching any of its weights at all. Prefix tuning and prompt tuning are the two simplest, most illustrative examples of this different strategy.

### From theory to code

Implement `prefix_tuning_augment` (prepending learnable K/V vectors to every attention layer) and `prompt_tuning_augment` (prepending learnable token embeddings, only at the input), plus their respective trainable-parameter counts.

### Constraints

- `prefix_tuning_augment(key, value, prefix_keys, prefix_values)` returns `(concat([prefix_keys, key]), concat([prefix_values, value]))`: the prefix comes FIRST in sequence order.
- `prompt_tuning_augment(input_embeddings, soft_prompt_embeddings)` returns `concat([soft_prompt_embeddings, input_embeddings])`.
- `count_trainable_parameters_prefix_tuning(num_layers, prefix_len, hidden_dim)` returns `num_layers * prefix_len * hidden_dim * 2` (the factor of `2` is for BOTH the key and value prefix).
- `count_trainable_parameters_prompt_tuning(prompt_len, hidden_dim)` returns `prompt_len * hidden_dim`: independent of the number of layers.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Prefix tuning needs its OWN learnable key/value prefix at EVERY attention layer of the network: that's why its parameter count scales with `num_layers`, while prompt tuning only ever touches the very first, input-embedding layer.

</details>

<details>
<summary>Hint 2</summary>

Once `prefix_tuning_augment` produces a longer key/value sequence, it can be fed directly into `01-scaled-dot-product-attention`'s existing attention function unchanged: the prefix tokens simply become extra "keys" every query can attend to, exactly like any other token in the sequence.

</details>
