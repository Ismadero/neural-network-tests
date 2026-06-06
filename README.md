# Neural Network Tests — Snake AI

A project to train a neural network to play Snake using **Deep Q-Learning (DQN)** with a convolutional neural network (CNN).

---

## Goal

Train an AI agent that learns to play Snake autonomously. The agent will use a DQN architecture where a CNN processes the game grid (as a 3-channel tensor) and outputs the optimal action at each step.

AI architecture (subject to change as experiments progress):
- **Algorithm:** Deep Q-Network (DQN)
- **Model:** CNN receiving a `(3, 15, 15)` state tensor (body, head, food channels) + direction one-hot vector `(4,)` concatenated at the FC layer
- **Actions:** 3 relative actions — go straight, turn left, turn right
- **Rewards:** `+10` eat food · `-25` die · `+0.1` new closest point to food ever in episode · `-0.1` otherwise
- **Step limit:** dynamic — `step_max = 100 + 50 × score` (prevents looping)
- **DQN components:** Q-network, target network, experience replay buffer, epsilon-greedy exploration

---

## What Works Now

- **Playable Snake game** — fully functional human-controlled Snake built with Pygame
  - 15×15 grid
  - Keyboard arrow controls
  - Score tracking and session summary on exit
- **DQN Agent** — fully trained with CNN + direction channel, replay buffer, and epsilon-greedy exploration
  - Training loop with model checkpointing and resume from checkpoint
  - Dynamic step limit per episode to penalize looping
  - Evaluation mode to watch the trained agent play
- **23 experiments completed** — systematic hyperparameter search across reward shaping, gamma, epsilon decay, model architecture, and extended training
  - Best result: **score avg 12.0, score max 35** (Experiment 23, episode 69,600)
  - Key findings:
    - **direction channel** (Exp 15) was the single biggest architectural improvement
    - **distance-based reward shaping** (rewarding only when the snake reaches a new closest point to food within the episode) significantly reduced looping behavior
    - **gamma = 0.60** works best when training from scratch — lower values loop more, higher values learn too slowly from zero
    - **fine-tuning with gamma = 0.90** on a pre-trained model (Exp 21→22→23) broke through the plateau dramatically: avg went from 2.9 to 12.0 over 20,000 additional episodes
    - Model is still improving at Experiment 23 — no plateau reached yet

---

## How to Run

### 1. Set up the virtual environment

```bash
python3 -m venv .nnt
source .nnt/bin/activate
pip install pygame
pip install numpy
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Or for GPU (CUDA) — select the right version for your system at:
# https://pytorch.org/get-started/locally/
```

### 2. Play the game manually

```bash
cd snake_ai/snake
python main.py
```

Use the **arrow keys** to control the snake. Your score, max possible score, and session time are printed on exit.

### 3. Train the AI agent

```bash
python snake_ai/train.py
```

To continue training from a saved checkpoint:

```bash
python snake_ai/train.py snake_dqn_<id>.pth
```

Press `Ctrl+C` at any time to stop and save the model.

### 4. Watch the trained agent play

```bash
python snake_ai/evaluate.py <path/to/checkpoint.pth>
```

Pass the path to any saved `.pth` checkpoint as the first argument.

---

## Architecture

### CNN Model

The input to the network is a `(3, 15, 15)` tensor representing the game grid as three binary channels:

| Channel | Represents |
|---------|------------|
| 0       | Snake body |
| 1       | Snake head |
| 2       | Food       |

This tensor is processed by two convolutional layers, then flattened and **concatenated with a direction one-hot vector** `(4,)` encoding the snake's current heading (UP, RIGHT, DOWN, LEFT) before passing through the fully connected layers:

```
Conv2d(3→16, 3×3) → ReLU → Conv2d(16→32, 3×3) → ReLU → MaxPool2d(2)
    → Flatten → Concat(direction) → Linear(conv_out+4 → 128) → ReLU → Linear(128 → 3)
```

Output: 3 Q-values corresponding to actions `{left, straight, right}`.

### DQN Agent

**Action selection — epsilon-greedy:**

```
a = random action,          if rand() ≤ ε
    argmax Q(s, a; θ),      otherwise
```

Epsilon decays after every training step: `ε ← max(ε_end, ε × ε_decay)`

**Bellman target (used for training):**

```
y = r + γ · max Q(s', a'; θ⁻) · (1 − done)
```

Where `θ⁻` are the weights of the frozen **target network**, copied from the Q-network every `target_update_freq` steps.

**Loss:**

```
L = MSE(Q(s, a; θ),  y)
```

Minimized with Adam optimizer.

**Step limit per episode (prevents looping):**

```
step_max = 100 + 50 × score
```

---

## Project Structure

```
neural_network_tests/
|
├── snake_ai/
|   |
|   |── train.py       # Training loop
|   |── evaluate.py    # Trained model runner
|   |   
│   |── snake/
│   |   ├── main.py        # Entry point
│   |   ├── game.py        # Game loop
│   |   ├── snake.py       # Snake logic
│   |   ├── food.py        # Food spawning
│   |   ├── screen.py      # Pygame rendering
│   |   ├── score.py       # Score tracking
│   |   └── constants.py   # Grid size, colors,timing
|   |
|   |── dqn/
|   |   |── agent.py       # Agent logic
|   |   └── model.py       # CNN Definition
|   |
|
```
