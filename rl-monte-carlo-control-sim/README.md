# Monte Carlo Control Simulation

Intermediate | rl | monte-carlo | control | simulation

Build an end-to-end MC control system that learns a policy on a simple gridworld environment. Generate episodes, update Q values, and track convergence.

### The problem, from first principles

You have a simple environment. Run MC control: collect episodes under ε-soft policy, estimate Q values, improve the policy. Track how Q converges and how the policy evolves.

### From theory to code

Implement `mc_control_gridworld(num_episodes, epsilon, gamma)` which:

- Runs a simple gridworld: 4x4 grid, 4 actions (N, S, E, W)
- Start at (0,0), goal at (3,3), each step reward -1, goal reward +10
- Runs MC control for num_episodes
- Returns (Q_final, policy, rewards_per_episode)

### Constraints

- Gridworld is 4x4, state = (row, col)
- Actions: 0=North, 1=South, 2=East, 3=West
- Collision with boundary: stay in place
- Episode ends when reaching (3,3) or after 50 steps
- Update Q after each episode

### Hints

<details>
<summary>Hint 1: Define the environment</summary>
Implement step(state, action) that returns (next_state, reward, done).
</details>

<details>
<summary>Hint 2: Collect episodes</summary>
Generate episodes using ε-soft policy: explore with prob ε, exploit with prob 1-ε.
</details>

<details>
<summary>Hint 3: Update Q</summary>
After each episode, compute returns and average into Q values.
</details>
