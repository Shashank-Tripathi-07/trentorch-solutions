# Actor-Critic with Neural Networks

Advanced | rl | actor-critic | deep-learning | policy-gradient

Actor-Critic with neural networks: separate networks for policy (actor) and value (critic). Actor uses critic's gradient to reduce variance.

### The problem, from first principles

Policy gradients have high variance. Actor-Critic uses learned baseline V(s) to compute advantage, reducing variance dramatically. Both networks trained jointly.

### From theory to code

Implement `actor_critic_step(actor_logits, actions, rewards, critic_values, next_values, gamma, alpha_actor, alpha_critic)` which:

- Computes advantages: A = r + γV(s') - V(s)
- Actor loss: -log π(a|s) * A
- Critic loss: MSE(V(s), r + γV(s'))
- Returns updated actor_params, critic_params

### Constraints

- Advantage baseline reduces variance
- Actor and critic updated independently
- Both use same trajectories
- Critic stabilizes actor learning

### Hints

<details>
<summary>Hint 1: Separate networks</summary>
Actor outputs policy, critic outputs scalar value
</details>

<details>
<summary>Hint 2: Advantage computation</summary>
A(s,a) = r + γV(s') - V(s)
</details>

<details>
<summary>Hint 3: Joint training</summary>
Sample trajectory once, update both networks
</details>
