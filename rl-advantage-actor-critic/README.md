# Advantage Actor-Critic (A3C)

Advanced | rl | a3c | actor-critic | parallel

Advantage Actor-Critic (A3C): parallel actors, shared policy and value networks. Each actor collects rollouts, computes advantages, and pushes updates asynchronously.

### The problem, from first principles

Actor-Critic is good but samples slowly. A3C parallelizes: N workers collect N independent episodes concurrently, all update the same shared network without locks. Massive speedup, no batching needed.

### From theory to code

Implement `a3c_worker_update(actor_network, critic_network, trajectory, gamma, entropy_coeff)` which:

- Takes one rollout trajectory
- Computes GAE advantages over trajectory
- Computes actor loss: -log π(a|s) * advantage - entropy_coeff * H(π)
- Computes critic loss: MSE(V, target)
- Returns gradient updates for actor and critic

### Constraints

- Entropy regularization prevents premature policy collapse
- Asynchronous updates: no batch averaging
- One worker processes one episode independently

### Hints

<details>
<summary>Hint 1: Entropy regularization</summary>
H(π) = -π log π, added to actor loss to encourage exploration
</details>

<details>
<summary>Hint 2: Per-worker updates</summary>
Each worker maintains local copy, pushes gradients to shared weights
</details>

<details>
<summary>Hint 3: Trajectory processing</summary>
Process entire episode from trajectory, compute advantages via bootstrapped values
</details>
