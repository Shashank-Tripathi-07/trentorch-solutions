# Epsilon-Soft On-Policy Monte Carlo Control

Intermediate | rl | monte-carlo | control | on-policy

Epsilon-Soft Monte Carlo Control learns an optimal policy by alternating between evaluation (averaging returns) and improvement (shifting toward greedy actions with probability 1-ε).

### The problem, from first principles

Given a non-stationary policy that is ε-soft (probability ≥ ε/|A| for every action), estimate Q^π(s,a) and improve π by shifting weight toward best actions. Unlike bandits, we must balance exploration (epsilon) with exploitation (greedy).

### From theory to code

Implement `epsilon_soft_mc_control(env_step, num_episodes, epsilon, gamma)` which:

- Runs `num_episodes` episodes where at each state, we take action with probability (1-ε) if best, else uniform random among remaining
- Tracks Q values (state-action pair returns)
- Tracks action counts
- Returns (Q_final, policy_final) where policy[s] is the best action

The env_step function has signature: env_step(state, action) -> (next_state, reward, done)

### Constraints

- epsilon in (0, 1)
- ε-soft policy: always explores, but biased toward greedy
- Update Q incrementally or batch-average
- Return final Q dict and greedy policy dict

### Hints

<details>
<summary>Hint 1: Track Q and counts</summary>
Store Q values and visit counts per (state, action) pair.
</details>

<details>
<summary>Hint 2: Generate episodes</summary>
Sample actions epsilon-soft: with prob 1-ε choose argmax Q[s], else uniform random.
</details>

<details>
<summary>Hint 3: Update Q</summary>
After each episode, average returns for first (or every) visit to each (s,a).
</details>
