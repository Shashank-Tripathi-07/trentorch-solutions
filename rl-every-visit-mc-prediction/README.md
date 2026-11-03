# Every-Visit Monte Carlo Prediction

Intermediate | rl | monte-carlo | value-estimation | prediction

Every-Visit Monte Carlo is a variant of MC prediction that averages returns from all visits to a state, not just the first. This introduces a slight bias but can reduce variance in some settings.

### The problem, from first principles

Given episodes from a fixed policy π, estimate V^π(s) using every occurrence of state s in each episode. Unlike first-visit, a state visited multiple times in one episode contributes multiple returns.

### From theory to code

Implement `estimate_state_values_every_visit(episodes, gamma)` which:

- Takes a list of episodes (each is a list of (state, reward) tuples)
- Takes discount factor γ
- Returns a dict {state: estimated_value}

Use every-visit semantics and unbiased averaging.

### Constraints

- Count all visits to each state, including repeats within an episode
- Compute return from each visit onward
- Return a dict mapping states to float values
- If a state never appears, exclude it from the dict

### Hints

<details>
<summary>Hint 1: No first-visit check</summary>
Unlike first-visit MC, don't track visited_states. Just iterate through all positions.
</details>

<details>
<summary>Hint 2: Accumulate returns</summary>
For each index i in the episode, compute the discounted return from i onward.
</details>

<details>
<summary>Hint 3: Average all returns</summary>
Each state gets all its returns averaged, regardless of how many times it appeared.
</details>
