# Monte Carlo with Exploring Starts

Intermediate | rl | monte-carlo | control | exploration

Exploring Starts ensures all state-action pairs are visited by randomly starting episodes from (state, action) pairs. This eliminates the need for an ε-soft policy but requires restart capability.

### The problem, from first principles

Instead of using ε-soft exploration during episodes, start each episode from a random (s,a) pair and then follow the deterministic optimal policy. This guarantees coverage of all (s,a) without permanent exploration noise.

### From theory to code

Implement `mc_exploring_starts(env_step, num_episodes, gamma, seed=None)` which:

- Generates random start (state, action) pairs
- Simulates episode from that (s,a) under greedy policy
- Computes returns and updates Q
- Returns (Q, policy)

### Constraints

- Environment is deterministic or stochastic
- Start state can be any valid state
- Start action is sampled uniformly
- All (s,a) pairs must have nonzero probability of start
- Follow greedy policy after initial action

### Hints

<details>
<summary>Hint 1: Random initialization</summary>
Pick a state from {0, 1, ..., num_states-1} uniformly. Pick an action from {0, 1, ..., num_actions-1} uniformly.
</details>

<details>
<summary>Hint 2: Episode under greedy policy</summary>
Take initial action, then at each step choose greedy action from Q.
</details>

<details>
<summary>Hint 3: First-visit update</summary>
Update Q for first occurrence of each (s,a) in episode.
</details>
