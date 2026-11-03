# Rejection Sampling: Keep Only the Best of Several Sampled Responses

Beginner | reinforcement-learning | nlp

### The problem, from first principles

`04-reward-modeling-bradley-terry` gave us a way to score any individual response: the simplest possible thing to DO with that reward model, before touching PPO or DPO's more sophisticated machinery, is to just sample several candidate responses per prompt, throw away the worse ones, and fine-tune on what's left. This is rejection sampling fine-tuning: no RL loop, no gradient through the reward model at all: just filter, then ordinary SFT (`01-supervised-fine-tuning-response-loss-mask`) on the survivors.

### From theory to code

Implement `filter_top_k_by_reward` (keeping only the best `k` of a sampled group) and `build_rejection_sampling_sft_dataset`, turning many prompts' worth of filtered survivors into one flat SFT-ready dataset.

### Constraints

- `filter_top_k_by_reward(responses, rewards, k)` returns the `k` responses with the highest rewards, best-to-worst.
- `build_rejection_sampling_sft_dataset(prompts, response_groups, reward_groups, k)` applies `filter_top_k_by_reward` independently PER prompt, then returns a flat list of `(prompt, response)` pairs for every survivor.
- `k=0` returns an empty list; `k` equal to a group's full size keeps everything (in some order).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.argsort(-rewards)` sorts indices from HIGHEST reward to lowest (negating flips ascending sort into descending): the first `k` entries of that order are exactly the ones to keep.

</details>

<details>
<summary>Hint 2</summary>

`build_rejection_sampling_sft_dataset` is just a loop: for each `(prompt, responses, rewards)` triple (zipped together), call `filter_top_k_by_reward`, then append `(prompt, response)` for every survivor.

</details>
