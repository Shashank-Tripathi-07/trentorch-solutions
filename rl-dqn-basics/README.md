# Deep Q-Network (DQN) Fundamentals

Advanced | rl | deep-learning | q-learning | neural-networks

Deep Q-Network combines Q-learning with neural networks to scale to high-dimensional state spaces (images, etc). Use target network and replay buffer for stability.

### The problem, from first principles

Large state spaces (images: 84x84x3 = ~21k features) can't use tabular methods. Neural networks can approximate Q: Q(s,a) ≈ NN_w(s,a). But directly training on RL data is unstable. Two fixes: target network and experience replay.

### From theory to code

Implement `dqn_loss(q_predictions, actions, rewards, next_q_target, done, gamma)` which:

- Takes Q predictions from online network
- Takes actions, rewards, next-state target Q from target network
- Computes Huber loss (smooth L1)
- Returns scalar loss

### Constraints

- Huber loss instead of MSE (more stable)
- Handle terminal states (done flag)
- Target = reward if done, else reward + gamma*max_Q'
- Use gradient clipping friendly loss

### Hints

<details>
<summary>Hint 1: Compute target</summary>
target = r + gamma * max Q'(s') * (1 - done)
</details>

<details>
<summary>Hint 2: Huber loss</summary>
Smooth L1: smooth at zero, linear in tails
</details>

<details>
<summary>Hint 3: Gather selected actions</summary>
Use actions to index into Q predictions
</details>
