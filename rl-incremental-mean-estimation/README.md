# Incremental Mean for Online Reward Estimation

Beginner | rl | bandits | estimation | online-learning

When estimating the mean reward of an action in a bandit problem, you can compute it incrementally as new samples arrive, without storing all historical samples.

### The problem, from first principles

In an n-armed bandit, the estimated value of action a is:

Q(a) = (R_1 + R_2 + ... + R_n) / n

If you've already computed Q after n samples, and receive a new reward R_{n+1}, you can update:

Q_{n+1} = Q_n + (1/(n+1)) * (R_{n+1} - Q_n)

This is the incremental mean formula. It lets you update online without storing all past rewards, using only the current estimate Q_n, the count n, and the new reward.

### From theory to code

Implement `update_incremental_mean(estimate, count, reward)` which:

- Takes the current estimate Q_n
- Takes the count of samples seen so far (n)
- Takes the new reward R_{n+1}
- Returns the updated estimate Q_{n+1}

### Constraints

- count is the number of samples BEFORE this reward (so n ≥ 0)
- reward is a float (can be positive, negative, or zero)
- Return the new estimate as a float
- Do not modify any input

### Hints

<details>
<summary>Hint 1: Direct formula</summary>
new_estimate = old_estimate + (1 / (count + 1)) * (reward - old_estimate)
</details>

<details>
<summary>Hint 2: Step size</summary>
The step size (1 / (count + 1)) decreases as we see more samples, so new rewards matter less.
</details>

<details>
<summary>Hint 3: Verify algebraically</summary>
Multiply out: Q_n + (1/(n+1))(R_{n+1} - Q_n) = (nQ_n + R_{n+1}) / (n+1) ✓
</details>
