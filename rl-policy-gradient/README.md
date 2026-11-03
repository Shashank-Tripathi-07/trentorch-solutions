# Policy Gradient Methods

Advanced | rl | policy-gradient | actor | neural-networks

Policy gradient directly optimizes the policy by computing ∇log π(a|s) * return. Simpler than value-based methods but higher variance.

### The problem, from first principles

Value-based (DQN): learn V or Q, derive policy as argmax. Policy-based: directly parameterize policy π(a|s), optimize with gradient ∇log π(a|s) * R.

### From theory to code

Implement `policy_gradient_loss(log_probs, advantages)` which:

- Takes log probabilities of actions taken
- Takes advantage estimates (reward - baseline)
- Returns negative mean of log_prob * advantage

### Constraints

- Negative loss (gradient ascent toward high-reward actions)
- Element-wise multiply log_probs and advantages
- Average across batch

### Hints

<details>
<summary>Hint 1: REINFORCE</summary>
Loss = -E[log π(a|s) * G_t]
</details>

<details>
<summary>Hint 2: Baseline</summary>
Advantage A = G_t - V(s) reduces variance
</details>

<details>
<summary>Hint 3: Gradient direction</summary>
Higher advantage → increase log prob of that action
</details>
