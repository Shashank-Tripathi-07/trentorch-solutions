# Model-Based Planning with Learned Models

Advanced | rl | model-based | planning | world-models

Learn environment model: predict s_{t+1} from (s_t, a_t). Use model for planning: simulate trajectories, pick actions with highest simulated returns.

### The problem, from first principles

Sample efficiency: real rollouts are expensive. Learn a forward model and plan with it. Trade off: model error accumulates, but reduces real interactions.

### From theory to code

Implement `dyna_update(real_trajectory, model, planning_steps)` which:

- Uses real trajectory to update value function
- Uses learned model for planning updates
- Takes planning_steps imagined trajectories
- Returns improved value estimates

### Constraints

- Model learns from real data
- Planning uses model to generate imagined data
- Model error can cause suboptimal policies
- Balance real vs imagined data

### Hints

<details>
<summary>Hint 1: Model training</summary>
Learn model to minimize prediction error on real data
</details>

<details>
<summary>Hint 2: Planning</summary>
Simulate trajectories using model, apply RL to imagined transitions
</details>

<details>
<summary>Hint 3: Dyna</summary>
Integrate real and imagined updates in same learning loop
</details>
