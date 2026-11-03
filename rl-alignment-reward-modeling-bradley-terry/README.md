# Reward Modeling: Training a Model to Score a Response Instead of Generate One

Advanced | reinforcement-learning | nlp | neural-networks

### The problem, from first principles

`03-preference-datasets-chosen-rejected` gave us pairs of (chosen, rejected) responses to the same prompt, but a preference PAIR isn't directly useful for guiding generation; what's needed is a single SCALAR reward function that can score any individual response on its own, so PPO (`06-ppo-clipped-surrogate-objective`) or best-of-N (`10-best-of-n-sampling`) can optimize against it. A reward model is exactly that: the same architecture as a language model, but repurposed to output one number instead of a next-token distribution.

### From theory to code

Implement `pooled_last_token_representation` (summarizing a whole response into one vector), `reward_model_score` (a linear "reward head" mapping that vector to a scalar), and `reward_model_loss`, the real Bradley-Terry pairwise preference loss used to train reward models in RLHF.

### Constraints

- `pooled_last_token_representation(hidden_states, seq_len)` returns `hidden_states[seq_len - 1]`: the LAST real (non-padding) token's hidden state.
- `reward_model_score(pooled_representation, reward_head_weight, reward_head_bias)` applies `01-hypothesis-function`'s `linear` and returns a plain Python `float`.
- `reward_model_loss(chosen_reward, rejected_reward)` returns `-log(sigmoid(chosen_reward - rejected_reward))`: low when `chosen_reward > rejected_reward`, high when it's backwards.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

By the time a causal transformer reaches the LAST token of a sequence, its hidden state has (via attention) already incorporated information from every earlier token: that's exactly why pooling just the last token's hidden state is enough to summarize the whole response.

</details>

<details>
<summary>Hint 2</summary>

`reward_model_loss` is the exact same shape as `07-dpo-direct-preference-optimization`'s loss, both are Bradley-Terry pairwise comparisons, `-log(sigmoid(difference))`, just applied to different quantities (a reward model's raw scalar scores here, versus DPO's implicit log-probability-ratio margin there).

</details>
