# Prioritized Experience Replay

Advanced | rl | experience-replay | importance-sampling | optimization

Prioritized Experience Replay (PER) samples high-TD-error transitions more often during learning, focusing effort on surprising/informative experiences.

### The problem, from first principles

Standard experience replay samples uniformly. But some transitions are more informative: high TD-error means the value estimate is wrong. PER uses a priority weight proportional to |TD-error| to oversample these transitions.

### From theory to code

Implement `prioritized_replay_buffer(transitions, td_errors, batch_size, alpha=0.6)` which:

- Takes transitions (list of (s,a,r,s',done) tuples)
- Takes td_errors (list of TD-error magnitudes)
- Returns a batch of indices sampled with probability proportional to (priority + epsilon)^alpha

### Constraints

- alpha in [0,1]: interpolates between uniform (0) and max priority (1)
- Priorities are |TD-error| + epsilon
- Batch size is requested size
- Return indices, not transitions

### Hints

<details>
<summary>Hint 1: Normalize priorities</summary>
Priority_i = (|TD-error_i| + epsilon)^alpha. Normalize to sum to 1.
</details>

<details>
<summary>Hint 2: Sample with replacement</summary>
Use np.random.choice with probabilities.
</details>

<details>
<summary>Hint 3: Handle edge cases</summary>
Zero errors should have small nonzero priority.
</details>
