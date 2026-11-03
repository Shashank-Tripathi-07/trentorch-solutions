# Note: Constitutional AI, Model-Written Critiques Instead of Human Labels

Beginner | reinforcement-learning | nlp

### The problem, from first principles

Every technique so far in this track (`03-preference-datasets-chosen-rejected` through `10-best-of-n-sampling`) assumes a human somewhere provided the preference labels or reward scores. Constitutional AI asks: can a model improve its OWN responses, and even generate its OWN preference data, using nothing but a written set of principles ("a constitution") and the model's own ability to critique and revise, with a human never directly labeling a single response?

### From theory to code

Implement `apply_critique_revision_step` (one principle-check-and-fix cycle) and `constitutional_ai_pipeline`, chaining that step across a whole list of principles, each building on the previous step's (possibly already-revised) output.

### Constraints

- `apply_critique_revision_step(response, principle, critique_fn, revise_fn)` calls `critique_fn(response, principle)`; if it returns `None`, nothing changed (`revised=False`); otherwise, `revise_fn(response, critique)` produces the new response (`revised=True`).
- `constitutional_ai_pipeline(response, principles, critique_fn, revise_fn)` applies `apply_critique_revision_step` once per principle, IN ORDER, always operating on the CURRENT (possibly already-revised) response.
- Returns `{"final_response", "critiques_applied"}`, where `critiques_applied` contains ONLY the critiques that actually triggered a revision, in the order they were applied.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`critique_fn` returning `None` means "no problem found": don't call `revise_fn` at all in that case, and don't add anything to `critiques_applied`.

</details>

<details>
<summary>Hint 2</summary>

`constitutional_ai_pipeline`'s loop must feed each step's OUTPUT response into the NEXT step's input: never re-check the original, unrevised response against later principles, since a genuine multi-principle revision process builds cumulatively.

</details>
