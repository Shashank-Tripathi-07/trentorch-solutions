# Best-of-N: Sampling N Responses and Picking the Reward Model's Favorite

Beginner | reinforcement-learning | nlp

### The problem, from first principles

`09-rejection-sampling-finetuning` used a reward model to curate TRAINING data. Best-of-N uses the exact same "sample many, keep the best" idea, but at INFERENCE time instead: rather than changing the model's weights at all, just generate `N` candidate responses to a single prompt right now, score them with the reward model, and return only the winner to the user.

### From theory to code

Implement `best_of_n_select` (picking the single best already-sampled response) and `expected_best_of_n_reward`, a Monte-Carlo simulation quantifying how much reward best-of-`N` actually buys you as `N` grows.

### Constraints

- `best_of_n_select(responses, rewards)` returns `(best_response, best_reward)`: the response with the highest reward, and that reward.
- `expected_best_of_n_reward(reward_pool, n, num_trials, seed)` repeatedly draws `n` samples (with replacement) from `reward_pool`, takes each draw's max, and returns the average of those maxes over `num_trials` repetitions.
- `expected_best_of_n_reward` must never exceed `reward_pool`'s true maximum, and must be non-decreasing in expectation as `n` grows.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`expected_best_of_n_reward` is genuinely a MAX, not a mean, of each drawn sample: the whole point of best-of-N is that you get to pick the single best of your `n` attempts, not their average quality.

</details>

<details>
<summary>Hint 2</summary>

At `n=1`, best-of-`n` reduces to just picking a single random sample, so `expected_best_of_n_reward(pool, n=1, ...)` should converge (as `num_trials` grows) to `pool.mean()`, a useful sanity check on your Monte-Carlo loop.

</details>
