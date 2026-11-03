# Preference Datasets: Chosen vs. Rejected Response Pairs

Beginner | reinforcement-learning | nlp

### The problem, from first principles

`02-instruction-vs-pretraining-datasets` built examples that teach a model to imitate ONE correct response per prompt. But "what's the single correct response" is often ambiguous or subjective: what's actually easy for a human to judge is COMPARISONS: "is response A better than response B?" A preference dataset captures exactly that comparison, and it's the foundation everything downstream in this track (reward modeling, PPO, DPO, GRPO) is built from.

### From theory to code

Implement `build_preference_pair` (packaging a prompt with two candidate responses), `shares_common_prompt_prefix` (a sanity check that both responses genuinely answer the same question), and `response_lengths`.

### Constraints

- `build_preference_pair(prompt_ids, chosen_ids, rejected_ids)` returns `{"prompt_len", "chosen", "rejected"}`, where `"chosen"`/`"rejected"` are each the FULL sequence `prompt_ids + <that response>`.
- `shares_common_prompt_prefix(preference_pair)` returns `True` exactly when both sequences' first `prompt_len` tokens are identical.
- `response_lengths(preference_pair)` returns `(chosen_response_length, rejected_response_length)`, computed as each full sequence's length minus `prompt_len`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Both `"chosen"` and `"rejected"` are built the SAME way: `prompt_ids` followed by the respective response: `shares_common_prompt_prefix` should hold trivially for any pair built with `build_preference_pair` itself, since they share the identical `prompt_ids` prefix by construction.

</details>

<details>
<summary>Hint 2</summary>

`response_lengths` doesn't need the original `chosen_ids`/`rejected_ids` lists at all: it can derive both lengths purely from the built sequences' lengths and `prompt_len`, which is exactly what `tests.py`'s independent-oracle test checks.

</details>
