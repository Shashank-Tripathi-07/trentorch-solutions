# Compute Discounted Return

Beginner | rl | tabular | fundamentals | mdp

The discounted return is a fundamental concept in reinforcement learning: the cumulative reward an agent receives, with future rewards discounted by a factor γ (gamma).

### The problem, from first principles

When an agent follows a trajectory through an environment, it receives rewards at each step. The return at time step t is defined as:

G_t = R_{t+1} + γR_{t+2} + γ²R_{t+3} + ... = Σ γ^(k-1) R_{t+k+1}

where R_i is the reward at step i and γ ∈ [0, 1] is the discount factor. This return captures:

- **Myopic agents** (γ ≈ 0): only care about immediate rewards
- **Farsighted agents** (γ ≈ 1): care equally about all future rewards
- **Realistic agents** (0.9-0.99): prefer nearer rewards slightly more

### From theory to code

You will implement `compute_discounted_return(rewards, gamma)` which:

- Takes a sequence of rewards (floats) received during an episode
- Takes a discount factor γ
- Returns the discounted return from the start of the episode

### Constraints

- Input rewards is a list/array of length ≥ 1
- gamma is in [0, 1]
- Return the scalar sum as a float
- Do not modify the input array

### Hints

<details>
<summary>Hint 1: Loop approach</summary>
Iterate through rewards with an index, multiply each reward by γ^(power) and sum.
</details>

<details>
<summary>Hint 2: Reverse iteration</summary>
Start from the last reward and work backward, multiplying by γ at each step (more numerically stable).
</details>

<details>
<summary>Hint 3: NumPy approach</summary>
Create an array of powers [0, 1, 2, ...] and use `np.sum(rewards * gamma ** powers)`.
</details>
