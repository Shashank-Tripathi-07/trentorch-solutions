# Off-Policy Monte Carlo with Importance Sampling

Advanced | rl | monte-carlo | off-policy | importance-sampling

Off-policy MC learns about π* while following behavior policy β by reweighting episode returns using importance sampling. The weight corrects for the mismatch between behavior and target policies. For this exercise the behavior policy is uniform over the actions observed in the episode, and the target policy is greedy with respect to the mean return of each (state, action) pair seen so far (ties go to the action that appears first in the episode).

### The problem, from first principles

You have episodes from behavior policy β (e.g., ε-greedy). You want to estimate V^π*(s) or Q^π*(s,a) for the greedy policy. Importance sampling computes W_t = ∏(π(a_i|s_i) / β(a_i|s_i)) to reweight returns.

### From theory to code

Implement `estimate_off_policy_returns(episodes, gamma)` which:

- Takes episodes (list of (state, action, reward) tuples)
- Takes gamma
- Uses π (greedy) and β (uniform over non-zero actions)
- Returns dict {(state, action): weighted_value}

Compute ordinary importance sampling weight for each return.

### Constraints

- Behavior policy β is uniform over actions seen in the episode
- Target policy π is greedy w.r.t. learned Q
- Weight is product of π/β over entire trajectory from first visit
- Zero weight paths are dropped or clipped

### Hints

<details>
<summary>Hint 1: Track π and β</summary>
For each state-action, estimate π from Q and β from episode.
</details>

<details>
<summary>Hint 2: Compute importance weight</summary>
W = product of (π(a|s) / β(a|s)) along the path.
</details>

<details>
<summary>Hint 3: Weight the return</summary>
Weighted return = W * G. Average weighted returns.
</details>
