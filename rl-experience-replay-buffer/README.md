# Experience Replay Buffer

Intermediate | rl | experience-replay | memory | off-policy

Experience Replay stores transitions in a buffer and samples minibatches for training, breaking correlation in the data stream and enabling off-policy learning.

### The problem, from first principles

Online learning from a stream of correlated transitions (consecutive transitions from the same episode are similar) leads to instability and poor generalization. Replay breaks temporal correlation by shuffling experience.

### From theory to code

Implement `experience_replay_buffer(capacity)` class with:

- `add(s, a, r, s', done)` to store transitions
- `sample(batch_size)` to return random minibatch
- `__len__` for current size

### Constraints

- Buffer has fixed capacity (FIFO when full)
- Sample without replacement (or with if capacity < batch_size)
- Return dict or list of transitions

### Hints

<details>
<summary>Hint 1: Store transitions</summary>
Use a deque or list with max length.
</details>

<details>
<summary>Hint 2: Sample uniformly</summary>
Random choice without replacement from stored transitions.
</details>

<details>
<summary>Hint 3: Handle small buffers</summary>
If batch_size > buffer_size, sample with replacement.
</details>
