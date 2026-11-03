# Reward Hacking: When Optimizing the Reward Stops Meaning What You Wanted

Intermediate | reinforcement-learning | nlp

### The problem, from first principles

Every single technique in this track, best-of-N (`10`), PPO (`06`), DPO (`07`), GRPO (`08`), assumes the reward signal being optimized genuinely reflects what you actually want. But a reward model (`04-reward-modeling-bradley-terry`) is only ever a PROXY, trained on a finite sample of human preferences, and any proxy can be exploited: if optimizing HARDER against the proxy stops improving (or actively hurts) what you truly care about, that's reward hacking: a direct instance of Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure").

### From theory to code

Implement `select_best_by_proxy` (optimizing purely against an imperfect proxy, exactly like `10-best-of-n-sampling` does), `true_reward_of_selection`, and `reward_hacking_gap`, quantifying exactly how much true quality gets sacrificed when the proxy and the true objective disagree.

### Constraints

- `select_best_by_proxy(candidates, proxy_rewards)` returns the index of the highest-`proxy_rewards` candidate: it must NEVER look at true rewards at all.
- `true_reward_of_selection(true_rewards, selected_index)` looks up the TRUE reward of whichever candidate got selected.
- `reward_hacking_gap(true_rewards, proxy_rewards)` returns `max(true_rewards) - true_reward_of_selection(true_rewards, select_best_by_proxy(..., proxy_rewards))`: always `>= 0`, and exactly `0` when the proxy and the true reward agree on the best candidate.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`select_best_by_proxy`'s signature includes `candidates` but its logic should touch ONLY `proxy_rewards`: that's the entire point: a proxy-optimizing selector has no access to ground truth, by design.

</details>

<details>
<summary>Hint 2</summary>

`reward_hacking_gap` is a comparison between two DIFFERENT selections: "what the proxy actually picked" versus "what an all-knowing oracle with access to the true reward would have picked": the gap is exactly how much true quality was lost by trusting the proxy instead.

</details>
