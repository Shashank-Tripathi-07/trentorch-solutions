# First-visit Monte Carlo policy evaluation

Intermediate | reinforcement-learning | monte-carlo | policy-evaluation

### The problem, from first principles

Value iteration needs a model of the environment. Monte Carlo evaluation needs none: just run complete episodes, and for each state average the total discounted reward that followed its visits.

### From theory to code

Implement `first_visit_mc(episodes, gamma)`. Each episode is a list of `(state, reward)` pairs, where `reward` is received on leaving that state. For every state, average the discounted return that followed its _first_ visit in each episode.

### Constraints

- `episodes` is a list of episodes; an episode is a list of `(state, reward)` tuples in time order. States are hashable.
- `gamma` is the discount factor in `[0, 1]`.
- The return at step `t` is `reward_t + gamma * return_{t+1}`, with the return after the last step being 0.
- Return a `dict` mapping each visited state to a Python `float`. A state's value averages one return per episode that visits it.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Compute returns for an episode by sweeping backwards: `G = reward + gamma * G`.

</details>

<details><summary>Hint 2</summary>

Walk the episode forward and record a return only the first time each state appears.

</details>
