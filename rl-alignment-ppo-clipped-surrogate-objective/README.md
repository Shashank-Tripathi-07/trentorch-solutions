# Note: PPO, Clipped Policy Updates for Stable RL Fine-Tuning

Intermediate | reinforcement-learning | nlp

### The problem, from first principles

`rl-alignment-tabular-q-learning`'s Q-learning updated a value TABLE directly from experience, but once the "policy" is a neural network being updated via gradient descent, a single overly-aggressive update can move the policy so far that all the data it just collected becomes stale and misleading. PPO solves this with one specific, elegant trick: instead of trusting the raw policy-gradient objective at face value, it explicitly CLIPS how much credit an update can take for a large policy change, keeping every step inside a safe "trust region".

### From theory to code

Implement `probability_ratio` (how much the policy has changed since the data was collected), `ppo_clipped_surrogate_loss` (the clipped objective itself), and `fraction_of_ratios_clipped`, a real training diagnostic.

### Constraints

- `probability_ratio(new_log_prob, old_log_prob)` returns `exp(new_log_prob - old_log_prob)`.
- `ppo_clipped_surrogate_loss(ratio, advantage, epsilon=0.2)` returns `-min(ratio * advantage, clip(ratio, 1-epsilon, 1+epsilon) * advantage)`.
- `fraction_of_ratios_clipped(ratio, epsilon=0.2)` returns the fraction of ratios falling outside `[1-epsilon, 1+epsilon]`.
- Clipping must never make the loss LOWER than the unclipped policy-gradient loss `-(ratio * advantage)` would be: clipping is a strictly pessimistic (conservative) correction.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Taking the MIN of the unclipped and clipped terms means PPO always uses whichever estimate is more PESSIMISTIC (lower reward-to-loss), for a positive advantage, that caps how much credit a large ratio can claim; for a negative advantage, clipping deliberately does NOT protect against moving too far in the wrong direction, since the min still picks the more negative (worse) unclipped term there.

</details>

<details>
<summary>Hint 2</summary>

`fraction_of_ratios_clipped` is a boolean mask, `(ratio < 1 - epsilon) | (ratio > 1 + epsilon)`, averaged: no need to actually recompute the clipped loss to answer "how many ratios got clipped".

</details>
