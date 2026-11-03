# Note: RLHF, the Full Pretrain to SFT to Reward Model to PPO Pipeline

Beginner | reinforcement-learning | nlp | mlops

### The problem, from first principles

This track has built the individual pieces, SFT (`01`), preference data (`03`), a reward model (`04`), but RLHF is specifically the PIPELINE connecting them: pretrain, then SFT, then train a reward model on preference data, then use PPO to optimize the SFT model against that reward model. Each stage has a genuinely different, quantifiable memory footprint, because PPO in particular needs several full models loaded into memory at once: a real, practical cost that's exactly why DPO (`07`) exists as an alternative.

### From theory to code

Implement `models_required_for_stage` (how many full model copies a given pipeline stage needs simultaneously in memory) and the derived `stage_memory_bytes`, `ppo_memory_multiplier_over_sft`, and `dpo_memory_multiplier_over_ppo`.

### Constraints

- `models_required_for_stage(stage)` returns `1` for `"pretraining"`, `"sft"`, and `"reward_modeling"`; `2` for `"dpo"`; `4` for `"ppo"`. Any other stage name raises `ValueError`.
- `stage_memory_bytes(stage, model_size_bytes)` returns `models_required_for_stage(stage) * model_size_bytes`.
- `ppo_memory_multiplier_over_sft()` returns `4.0`; `dpo_memory_multiplier_over_ppo()` returns `0.5`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

PPO needs FOUR models resident at once: the policy being trained, a FROZEN reference copy of it (to compute a KL penalty against, keeping the policy from drifting too far), the reward model (to score generated responses), and a value model (to estimate the baseline for advantage estimation).

</details>

<details>
<summary>Hint 2</summary>

DPO needs only TWO: the policy being trained, and a frozen reference copy: no reward model, and no value model, because DPO's loss (`07-dpo-direct-preference-optimization`) is computed directly from log-probabilities, with no separate RL rollout loop at all.

</details>
