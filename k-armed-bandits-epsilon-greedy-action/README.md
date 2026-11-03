# Epsilon-greedy action selection

Beginner | reinforcement-learning | bandits | exploration

### The problem, from first principles

A bandit agent must keep trying the arm that looks best (exploitation) while occasionally trying others in case its estimates are wrong (exploration). Epsilon-greedy is the simplest rule: explore with a small fixed probability, otherwise exploit.

### From theory to code

Implement `epsilon_greedy_action(q_values, epsilon, rng)`. With probability `epsilon` return a uniformly random arm; otherwise return the arm with the highest estimated value.

### Constraints

- `q_values` is a one-dimensional array of current value estimates, one per arm.
- `rng` is a `numpy.random.Generator`; draw the explore/exploit decision from it with `rng.random()`, and the random arm with `rng.integers(...)`.
- On exploiting, break ties toward the lowest arm index.
- Return a Python `int`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Draw one number in `[0, 1)`; if it is below `epsilon`, explore.

</details>

<details><summary>Hint 2</summary>

`np.argmax` already returns the first maximum, which gives the required tie-break.

</details>
