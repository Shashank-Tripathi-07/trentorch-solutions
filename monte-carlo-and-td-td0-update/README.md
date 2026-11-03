# TD(0) value update

Beginner | reinforcement-learning | temporal-difference | policy-evaluation

### The problem, from first principles

Monte Carlo has to wait until an episode ends before it can learn anything. Temporal-difference learning updates after every single step, by comparing its current estimate with a slightly better one: the reward just received plus its estimate of where it landed.

### From theory to code

Implement `td0_update(V, state, reward, next_state, alpha, gamma, done=False)`, returning a new value table with only `V[state]` updated.

### Constraints

- `V` is a float array indexed by integer state. Do not modify it; return an updated copy.
- The TD target is `reward + gamma * V[next_state]`, or just `reward` if `done` is true (a terminal state has no future value).
- Move `V[state]` towards the target by a fraction `alpha` of the gap.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Compute the target, then the TD error `target - V[state]`.

</details>

<details><summary>Hint 2</summary>

Add `alpha * error` to `V[state]`.

</details>
