# Atari Game Playing

Advanced | rl | applications | deep-rl | vision

Apply DQN to Atari games: convert pixel observations to feature vectors, train on massive replay buffers, achieve superhuman performance.

### The problem, from first principles

Raw pixels as state: 84x84x4 = 28,224 inputs per frame. Fully connected networks fail. Convolutional networks extract features. DQN learns to play from pixels alone.

### From theory to code

Implement `preprocess_atari_frame(raw_frame)` which:

- Takes raw 210x160x3 RGB frame
- Crops to 160x160
- Resizes to 84x84
- Converts to grayscale
- Normalizes to [0, 1]
- Returns preprocessed frame

### Constraints

- Input: 210x160x3 uint8 Atari frame
- Output: 84x84 float32 frame
- Use standard preprocessing

### Hints

<details>
<summary>Hint 1: Grayscale</summary>
0.299*R + 0.587*G + 0.114*B
</details>

<details>
<summary>Hint 2: Resize</summary>
Bilinear interpolation or max-pool
</details>

<details>
<summary>Hint 3: Normalize</summary>
frame / 255.0
</details>
