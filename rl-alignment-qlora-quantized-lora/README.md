# QLoRA: LoRA on Top of a Quantized Base Model

Advanced | reinforcement-learning | mlops | neural-networks

### The problem, from first principles

LoRA already makes fine-tuning cheap by training only a small pair of low-rank matrices while the base model's weights stay frozen. But "frozen" doesn't mean "small": the base model still has to be loaded, in full precision, taking up exactly as much memory as it always did. QLoRA's contribution: since the base weights are frozen anyway, store them QUANTIZED (far less memory), only ever dequantizing on the fly for the forward pass's matmul, while the small LoRA matrices stay in full precision and train normally.

### From theory to code

Implement `compute_int8_scale`/`quantize_int8`/`dequantize_int8` (a self-contained int8 quantization scheme), `lora_delta` (LoRA's low-rank update), `qlora_linear_forward` (combining both), and `count_trainable_parameters`, quantifying just how few parameters QLoRA actually trains.

### Constraints

- `compute_int8_scale(weight)` returns `max(abs(weight)) / 127.0`.
- `quantize_int8(weight, scale)` returns `clip(round(weight / scale), -128, 127)` as `int8`; `dequantize_int8` reverses it (approximately: quantization is lossy).
- `lora_delta(input, lora_A, lora_B, alpha, rank)` returns `(alpha / rank) * (input @ lora_A.T) @ lora_B.T`, where `lora_A` has shape `(rank, in_features)` and `lora_B` has shape `(out_features, rank)`.
- `qlora_linear_forward` returns `input @ dequantize_int8(quantized_weight, scale).T + lora_delta(...)`.
- `count_trainable_parameters(in_features, out_features, rank)` returns `{"full_finetune": in_features * out_features, "qlora": rank * in_features + out_features * rank}`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

The quantized base weight and the LoRA matrices play completely different roles: the base weight is dequantized and used EXACTLY like an ordinary (frozen) `Linear` layer's weight; the LoRA delta is added ON TOP, as a separate, small, trainable contribution.

</details>

<details>
<summary>Hint 2</summary>

`lora_delta`'s output can never have a matrix rank higher than `rank`, no matter how large the batch: `input @ lora_A.T` collapses each input row down to a `rank`-dimensional vector before `lora_B.T` expands it back up, which is exactly LoRA's "low-rank" name.

</details>
