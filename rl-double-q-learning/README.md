# Double Q-Learning

Advanced | rl | temporal-difference | control | off-policy

Double Q-Learning addresses overestimation bias in standard Q-learning by maintaining two Q estimates and decoupling selection from evaluation.

### The problem, from first principles

Standard Q-learning uses max Q(s',a') which can overestimate values (max of noisy estimates is biased high). Double Q-learning uses one Q for selection and another for evaluation, reducing bias.

### From theory to code

Implement `double_q_learning(env_step, num_episodes, epsilon, gamma, alpha, seed=None)` which:

- Maintains two Q estimates: Q1 and Q2
- Updates both alternately
- Uses Q1 to select best action, Q2 to evaluate (and vice versa)
- Returns (Q_avg, policy)

### Constraints

- Two separate Q dictionaries
- Alternate which Q is used for selection vs evaluation
- Random choice of which Q to update each step
- Return averaged final Q values

### Hints

<details>
<summary>Hint 1: Two Q values</summary>
Keep Q1 and Q2 both as dicts.
</details>

<details>
<summary>Hint 2: Decoupling</summary>
Use one Q to pick best action, other Q to evaluate value.
</details>

<details>
<summary>Hint 3: Alternation</summary>
Each step, randomly choose which Q to update.
</details>
