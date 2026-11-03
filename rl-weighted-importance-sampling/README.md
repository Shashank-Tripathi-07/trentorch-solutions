# Weighted Importance Sampling

Advanced | rl | monte-carlo | off-policy | importance-weighting

Weighted Importance Sampling reduces variance of off-policy estimation by normalizing by the sum of importance weights. This trades unbiasedness for lower variance.

### The problem, from first principles

Ordinary importance sampling can have infinite variance when the behavior policy is far from the target. Weighted IS divides by the sum of weights: V(s) = Σ(W_i * G_i) / Σ(W_i), which reduces variance but adds bias.

### From theory to code

Implement `estimate_weighted_importance_sampling(episodes, gamma)` which:

- Takes episodes as list of (state, action, reward) tuples
- Computes importance weights
- Returns dict {(state, action): weighted_average_return}

Use the formula: V(s,a) = Σ(W_t * G_t) / Σ(W_t) for all visits.

### Constraints

- Zero weights are handled gracefully (skip or clip)
- Return dict of (state, action) -> value
- Gamma discount factor
- All episodes are valid sequences

### Hints

<details>
<summary>Hint 1: Accumulate weighted sums</summary>
Keep sum of weights and sum of weighted returns separately.
</details>

<details>
<summary>Hint 2: Compute importance weight</summary>
W_t = product of π(a|s) / β(a|s) along path from first visit.
</details>

<details>
<summary>Hint 3: Divide at the end</summary>
V(s,a) = (sum of weighted returns) / (sum of weights) for each (s,a).
</details>
