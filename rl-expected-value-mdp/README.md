# Evaluate Expected Value in a Markov Decision Process

Intermediate | rl | mdp | value-functions | fundamentals

The expected value (or expected return) of a state under a policy is the average discounted return an agent can expect to achieve starting from that state and following the policy.

### The problem, from first principles

In an MDP, the state value function V^π(s) tells you how good it is to be in state s when following policy π:

V^π(s) = E_π[G_t | S_t = s]

where G_t is the discounted return from time t onward. For a finite horizon or episodic task, you can compute this by averaging the discounted returns from many rollouts starting in state s.

### From theory to code

Implement `evaluate_state_value(trajectories, state, gamma)` which:

- Takes a list of trajectories (each is a sequence of (state, reward) tuples)
- Takes a target state s
- Takes a discount factor γ
- Returns the expected (mean) discounted return starting from the first occurrence of state s in each trajectory
- If state s does not appear in a trajectory, skip that trajectory

### Constraints

- Each trajectory is a list of (state, reward) pairs where state is hashable
- The first visit to state s is the one we care about
- Return 0.0 if the state never appears in any trajectory
- Use first-visit semantics: only the first occurrence of s in each trajectory counts

### Hints

<details>
<summary>Hint 1: Loop through trajectories</summary>
For each trajectory, find the first index where state s occurs, then compute the discounted return from that point onward.
</details>

<details>
<summary>Hint 2: Discounted return calculation</summary>
Once you identify where state s first appears, sum γ^k * reward[k+1] for all future steps.
</details>

<details>
<summary>Hint 3: Averaging</summary>
Collect all returns from state s and average them. Handle the case where s never appears.
</details>
