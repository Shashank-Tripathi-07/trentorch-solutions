# Epsilon-Greedy Action Selection for n-Armed Bandit

Beginner | rl | bandits | exploration | exploration-exploitation

Epsilon-greedy is the simplest exploration strategy: with probability ε, pick a random action; with probability 1-ε, pick the greedy action (highest estimated value).

### The problem, from first principles

The exploration-exploitation trade-off is central to reinforcement learning:

- **Exploit**: choose the action with the highest estimated value (greedy)
- **Explore**: try other actions to learn better estimates

Epsilon-greedy balances them: most of the time (1-ε), you exploit; occasionally (ε), you explore randomly. This ensures:

- You eventually find the optimal action (exploration)
- You spend most time on good actions (exploitation)

### From theory to code

Implement `select_epsilon_greedy_action(q_values, epsilon, rng)` which:

- Takes action values Q(a) for all actions a (1D array or list)
- Takes epsilon ∈ [0, 1]
- Takes a numpy random number generator
- Returns the selected action index (int)

With probability ε, return a random action index. With probability 1-ε, return the index of the highest-valued action.

### Constraints

- q_values has at least 1 action
- epsilon is in [0, 1]
- rng is a numpy random generator (use `rng.random()` for uniform [0,1) and `rng.choice()` for random selection)
- If there are ties for max, break ties deterministically or randomly (either is fine)

### Hints

<details>
<summary>Hint 1: Random vs Greedy</summary>
Generate u = rng.random(). If u < epsilon, choose random. Else choose greedy.
</details>

<details>
<summary>Hint 2: Greedy action</summary>
Use np.argmax(q_values) to find the highest-valued action.
</details>

<details>
<summary>Hint 3: Random action</summary>
Use rng.choice(len(q_values)) or rng.integers(0, len(q_values)).
</details>
