# Build a Multi-Armed Bandit Testbed

Intermediate | rl | bandits | experimentation | performance-evaluation

A bandit testbed is an experimental framework for evaluating bandit algorithms. You generate random bandit instances, run algorithms on them, and measure performance (cumulative regret, action accuracy).

### The problem, from first principles

To fairly compare epsilon-greedy and UCB, you need:

1. A random bandit instance (true rewards for each arm)
2. A way to run an algorithm on that instance
3. A way to measure performance (did we find the best arm?)

The testbed generates multiple independent bandits and averages the results across them. This controls for randomness in the problem and gives stable performance estimates.

### From theory to code

Build a class `BanditTestbed` with:

- Constructor: `__init__(num_arms, num_instances, seed)` - creates `num_instances` random bandits with `num_arms` arms
- Method: `run_algorithm(select_fn, num_steps)` - runs the selection function for `num_steps` steps on all instances
- Method: `get_results()` - returns (mean_rewards, optimal_counts, regrets)

True rewards are drawn from N(0, 1), then for each step, the agent selects an arm, observes a reward drawn from N(true_reward, 1).

### Constraints

- num_arms ≥ 2
- num_instances ≥ 1
- num_steps ≥ 1
- select_fn has signature: select_fn(q_estimates, counts, time_step, rng) -> action (int)
- Return three arrays: (rewards per step, times optimal arm was selected, cumulative regret)

### Hints

<details>
<summary>Hint 1: Class structure</summary>
Store the true arm rewards in __init__. In run_algorithm, track Q estimates, counts, and rewards for each instance.
</details>

<details>
<summary>Hint 2: Evaluation loop</summary>
For each step and each instance: select action, observe reward, update Q and counts, record result.
</details>

<details>
<summary>Hint 3: Results aggregation</summary>
Average rewards and regrets across instances. Count optimal selections across all instances.
</details>
