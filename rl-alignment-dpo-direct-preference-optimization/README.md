# DPO: Optimizing the Preference Directly, No Separate Reward Model or RL Loop

Advanced | reinforcement-learning | nlp

### The problem, from first principles

`05-rlhf-pipeline-memory-cost` quantified PPO's real cost: four models resident in memory, plus an entire RL rollout loop, just to optimize against a reward model that itself had to be trained separately (`04-reward-modeling-bradley-terry`) on the same preference data. DPO's key insight: the optimal policy under an RLHF-style objective has a closed-form relationship to an IMPLICIT reward, expressible directly in terms of the policy's own log-probabilities, so preference data can train the policy directly, no reward model and no RL loop required at all.

### From theory to code

Implement `implicit_reward_margin` (DPO's substitute for an explicit reward-model score difference) and `dpo_loss`, the exact loss function from the DPO paper.

### Constraints

- `implicit_reward_margin(policy_chosen_logprob, policy_rejected_logprob, ref_chosen_logprob, ref_rejected_logprob, beta)` returns `beta * [(policy_chosen_logprob - ref_chosen_logprob) - (policy_rejected_logprob - ref_rejected_logprob)]`.
- `dpo_loss(..., beta=0.1)` returns `-log(sigmoid(implicit_reward_margin(...)))`: the same Bradley-Terry-shaped loss as `04-reward-modeling-bradley-terry`, applied to this margin instead of a raw reward-model score difference.
- Shifting BOTH reference log-probabilities by the same constant must leave the margin unchanged: only the relative log-ratios matter.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`(policy_chosen_logprob - ref_chosen_logprob)` measures how much MORE likely the current policy has made the chosen response, relative to where the frozen reference model started: that quantity is DPO's implicit "reward" for the chosen response; the same for rejected, and the margin is the difference of those two implicit rewards.

</details>

<details>
<summary>Hint 2</summary>

Once you have `implicit_reward_margin`, `dpo_loss` is a one-line reuse of the exact same `-log(sigmoid(...))` shape `04-reward-modeling-bradley-terry`'s `reward_model_loss` uses: DPO didn't invent a new loss function, it found a way to plug log-probabilities directly into the SAME Bradley-Terry loss a reward model would have used.

</details>
