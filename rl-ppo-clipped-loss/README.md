# PPO Clipped Loss

Advanced | rl | ppo | policy-gradient | clipping

Proximal Policy Optimization (PPO): policy gradient with clipped objective. Prevents destructive large policy updates while allowing reasonable improvements.

### The problem, from first principles

Standard policy gradients can have huge step sizes. PPO clips the objective to bound updates: if new policy improves too much, ignore the excess. Dramatically more stable than vanilla REINFORCE.

### From theory to code

Implement `ppo_loss(log_probs_new, log_probs_old, advantages, epsilon=0.2)` which:

- Computes probability ratio: r = exp(log_probs_new - log_probs_old)
- Unclipped: r * advantages
- Clipped: clip(r, 1-ε, 1+ε) * advantages
- Loss: -min(unclipped, clipped) mean
- Returns scalar loss

### Constraints

- Clipping preserves good improvements
- Prevents backtracking
- Typically ε in [0.1, 0.3]

### Hints

<details>
<summary>Hint 1: Probability ratio</summary>
r = exp(log p_new - log p_old) = p_new / p_old
</details>

<details>
<summary>Hint 2: Clipping</summary>
Clip ratio to [1-ε, 1+ε], element-wise
</details>

<details>
<summary>Hint 3: Loss is minimum</summary>
Take min of unclipped and clipped, then negate and average
</details>
