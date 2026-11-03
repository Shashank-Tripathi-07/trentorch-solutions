# Note: GRPO, Group-Relative Advantage Without a Value Network

Intermediate | reinforcement-learning | nlp

### The problem, from first principles

`05-rlhf-pipeline-memory-cost` noted PPO needs a whole extra VALUE model just to estimate a baseline for its advantage calculation: one more full model to train and keep resident in memory. GRPO removes that requirement with a simple idea: sample several responses to the SAME prompt as a "group", score each with the reward model, and use each response's standing RELATIVE to its own group as the advantage: no separate value network needed at all.

### From theory to code

Implement `grpo_group_relative_advantage` (the group-normalized advantage) and `grpo_policy_gradient_loss` (the standard policy-gradient loss, using that advantage).

### Constraints

- `grpo_group_relative_advantage(rewards, eps=1e-8)` returns `(rewards - rewards.mean()) / (rewards.std() + eps)`.
- The result always has mean `0` (up to floating point) regardless of the input rewards' scale or offset.
- `grpo_policy_gradient_loss(log_probs, advantages)` returns `-mean(log_probs * advantages)`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Subtracting the mean centers the rewards around `0` (some end up positive, some negative, relative to the group's average); dividing by the standard deviation then rescales so the SPREAD of advantages is comparable across groups, regardless of whether the raw reward values happened to be tightly clustered or widely spread.

</details>

<details>
<summary>Hint 2</summary>

`grpo_policy_gradient_loss` doesn't care where the advantage came from: it's the exact same "push up log-probability where advantage is positive, push down where negative" formula that any policy-gradient method uses; GRPO's only real innovation is HOW the advantage gets computed.

</details>
