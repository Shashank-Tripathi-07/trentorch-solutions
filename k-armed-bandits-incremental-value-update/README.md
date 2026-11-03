# Incremental action-value update

Beginner | reinforcement-learning | bandits | value-estimation

### The problem, from first principles

To estimate an arm's value you could store every reward it ever gave and average them, but that needs ever-growing memory. The same average can be maintained with just the current estimate and a count.

### From theory to code

Implement `update_action_value(q_values, counts, action, reward)`. Increment the pulled arm's count and move its estimate toward the new reward by `1 / count` of the gap.

### Constraints

- `q_values` is a float array and `counts` an integer array, one entry per arm.
- Return new arrays `(q_values, counts)`; do not modify the inputs.
- Only the pulled arm changes.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Increase `counts[action]` first, so the first-ever reward uses a step size of exactly 1.

</details>

<details><summary>Hint 2</summary>

The update is `q += (reward - q) / n`.

</details>
