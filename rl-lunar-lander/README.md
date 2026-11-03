# Lunar Lander Simulation

Advanced | rl | continuous-control | physics-simulation | applications

Lunar Lander: soft-land spacecraft on moon. State: [x, y, vx, vy, angle, angular_vel]. Actions: [off, left-engine, main-engine, right-engine]. Reward: -1 per step, +200 landed, -100 crash.

### The problem, from first principles

Continuous control with sparse rewards. Must learn to descend, manage fuel, stabilize. Solved when mean reward >= 200 over 100 episodes.

### From theory to code

Implement `simulate_lunar_lander(initial_state, actions, max_steps)` which:

- Tracks fuel, position, velocity, attitude
- Applies thrust physics
- Computes rewards: step cost, landing bonus, crash penalty
- Returns trajectory with (state, reward) tuples

### Constraints

- Gravity = 1.5 m/s^2
- Main engine thrust = 13.5 m/s^2, side = 0.75 m/s^2
- Fuel limited
- Must land soft: vx, vy < 0.1 m/s and angle < π/4

### Hints

<details>
<summary>Hint 1: Thrust model</summary>
Acceleration = thrust_vector / mass - gravity
</details>

<details>
<summary>Hint 2: Landing condition</summary>
y < 0 and low velocity and stable angle
</details>

<details>
<summary>Hint 3: Fuel constraint</summary>
Track fuel consumption, episode ends if fuel depleted
</details>
