# CartPole Control

Intermediate | rl | control | simulation | applications

CartPole: balance a pole on a moving cart. Classic benchmark for RL. Observations: [x, v, θ, ω]. Actions: [left, right]. Reward: +1 per step balanced.

### The problem, from first principles

CartPole tests ability to learn stable control policies. Physics are simple but nonlinear. Solved when mean reward >= 195 over 100 episodes.

### From theory to code

Implement `simulate_cartpole(initial_state, actions, max_steps)` which:

- Takes initial [x, v, θ, ω] and sequence of actions
- Simulates CartPole dynamics using Euler integration
- Returns trajectory of (state, reward) pairs
- Done when |x| > 2.4 or |θ| > π/12

### Constraints

- Physics parameters from OpenAI Gym CartPole-v0
- Force = 10 N
- Gravity = 9.8 m/s^2
- Pole length = 0.5 m, mass = 0.1 kg
- Cart mass = 1.0 kg

### Hints

<details>
<summary>Hint 1: State transition</summary>
Use equations of motion for inverted pendulum on cart
</details>

<details>
<summary>Hint 2: Done condition</summary>
Episode ends if x > 2.4 or θ > π/12
</details>

<details>
<summary>Hint 3: Rewards</summary>
+1 per step while balanced, 0 when done
</details>
