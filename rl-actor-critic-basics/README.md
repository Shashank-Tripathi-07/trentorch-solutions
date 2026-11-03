# Actor-Critic Fundamentals

Advanced | rl | actor-critic | policy-gradient | temporal-difference

Actor-Critic combines policy gradient (actor) with value estimation (critic). The critic provides low-variance TD estimates to reduce policy gradient variance.

### The problem, from first principles

Policy gradients have high variance (return G_t varies a lot). TD critic provides estimate V(s) which reduces variance: use advantage A(s,a) = r + γV(s') - V(s) instead of full return.

### From theory to code

Implement `actor_critic_loss(policy_logprobs, actions, rewards, next_values, gamma)` which:

- Takes log probabilities from policy, actions taken
- Takes rewards and next-state values from critic
- Returns actor_loss and critic_loss

### Constraints

- Actor loss uses advantage as baseline
- Critic loss is MSE of value prediction
- Advantage = reward + gamma * next_value - current_value
- Return tuple (actor_loss, critic_loss)

### Hints

<details>
<summary>Hint 1: Compute advantage</summary>
A(s,a) = r + γV(s') - V(s)
</details>

<details>
<summary>Hint 2: Actor loss</summary>
Loss = -log π(a|s) * A(s,a) (negative advantage means we regret the action)
</details>

<details>
<summary>Hint 3: Critic loss</summary>
MSE of value prediction against bootstrapped target
</details>
