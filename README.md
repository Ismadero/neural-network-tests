# Neural Network Tests — Snake AI

A project to train a neural network to play Snake using **Deep Q-Learning (DQN)** with a convolutional neural network (CNN).

---

## Goal

Train an AI agent that learns to play Snake autonomously. The agent will use a DQN architecture where a CNN processes the game grid (as a 3-channel tensor) and outputs the optimal action at each step.

Planned AI architecture:
- **Algorithm:** Deep Q-Network (DQN)
- **Model:** CNN receiving a `(3, 15, 15)` state tensor (body, head, food channels)
- **Actions:** 3 relative actions — go straight, turn left, turn right
- **Rewards:** `+10` eat food · `-10` die · `-0.1` per step (avoids looping)
- **DQN components:** Q-network, target network, experience replay buffer, epsilon-greedy exploration

---

## What Works Now

- **Playable Snake game** — fully functional human-controlled Snake built with Pygame
  - 15×15 grid
  - Keyboard arrow controls
  - Score tracking and session summary on exit

---

## How to Run

### 1. Set up the virtual environment

```bash
python3 -m venv .nnt
source .nnt/bin/activate
pip install pygame
pip install numpy
pip install torch
```

### 2. Play the game

```bash
cd snake_ai/snake
python main.py
```

Use the **arrow keys** to control the snake. Your score, max possible score, and session time are printed on exit.

---

## Project Structure

```
neural_network_tests/
├── snake_ai/
│   |── snake/
│   |   ├── main.py        # Entry point
│   |   ├── game.py        # Game loop
│   |   ├── snake.py       # Snake logic
│   |   ├── food.py        # Food spawning
│   |   ├── screen.py      # Pygame rendering
│   |   ├── score.py       # Score tracking
│   |   ├── constants.py   # Grid size, colors,timing
│   |   └── plan.txt       # Full DQN architecture plan
|   |
|   |── dqn/
|   |   |── agent.py       # Agent logic
|   |   |── model.py       # CNN Definition
|   |   |── train.py       # Training loop
|   |   |── evaluate.py    # Agent trained runner
|   |
|
```

---

## Roadmap

- [✅] Headless game mode (`Game(render=False)`) for fast training
- [✅] `game.step(action)` interface for external agent control
- [✅] `get_state()` — returns `(3, 15, 15)` tensor
- [✅] `model.py` — CNN definition in PyTorch
- [ ] `agent.py` — DQN agent (epsilon-greedy, replay buffer)
- [ ] `train.py` — training loop
- [ ] `evaluate.py` — watch the trained agent play
