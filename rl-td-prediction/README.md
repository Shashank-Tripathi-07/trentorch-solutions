# TD(0) Prediction

Intermediate | rl | temporal-difference | td-learning | prediction

Temporal Difference (TD) learning combines ideas from MC and DP: update value estimates using a mix of immediate reward and bootstrapped next-state value. TD(0) is the one-step version.

### The problem, from first principles

Instead of waiting for episode completion (MC) or needing the full model (DP), TD updates immediately: V(s) = V(s) + α[r + γV(s') - V(s)]. The term [r + γV(s') - V(s)] is the TD error.

### From theory to code

Implement `td_prediction(episodes, gamma, alpha)` which:

- Takes episodes as list of (state, reward, next_state) tuples
- Takes discount factor γ and step size α
- Returns dict {state: estimated_value}

Update values incrementally using TD(0) rule.

### Constraints

- alpha in (0, 1], typically 0.1
- Process episode transitions online
- Terminal states have value 0
- Update only visited states

### Hints

<details>
<summary>Hint 1: Process online</summary>
For each (s, r, s') in episode, update V(s) immediately.
</details>

<details>
<summary>Hint 2: Compute TD error</summary>
delta = r + gamma * V(s') - V(s)
</details>

<details>
<summary>Hint 3: Update V</summary>
V(s) = V(s) + alpha * delta
</details>
