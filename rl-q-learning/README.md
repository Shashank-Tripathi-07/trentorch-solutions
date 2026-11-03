# Q-Learning (Off-Policy TD Control)

Intermediate | rl | temporal-difference | control | off-policy

Q-Learning is off-policy TD control: learn optimal Q(s,a) while following an ε-greedy behavior policy. Update uses greedy next action, not the action actually taken.

### The problem, from first principles

SARSA updates with the next action you take. Qlearning updates with the best action you could take. This decouples learning from the policy, enabling off-policy learning of the optimal policy while exploring.

### From theory to code

Implement `q_learning(env_step, num_episodes, epsilon, gamma, alpha, seed=None)` which:

- Generates episodes under ε-greedy policy
- Updates Q(s,a) using: Q(s,a) = Q(s,a) + α[r + γmax Q(s',a') - Q(s,a)]
- Returns (Q, policy)

### Constraints

- alpha in (0, 1], learning rate
- epsilon in (0, 1), exploration
- gamma in (0, 1], discount
- Update immediately after each transition
- Terminal state has value 0

### Hints

<details>
<summary>Hint 1: Select actions epsilon-greedy</summary>
With prob 1-ε pick greedy, else random.
</details>

<details>
<summary>Hint 2: Update with max</summary>
Use max Q(s',a') for all a', not just the action taken.
</details>

<details>
<summary>Hint 3: TD error for off-policy</summary>
delta = r + gamma * max_a Q(s',a) - Q(s,a)
</details>
