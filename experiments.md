# Experiments Log

## Template
```
### Experiment N — YYYY-MM-DD
**Hyperparameters**
- epsilon_start / epsilon_end / epsilon_decay:
- gamma:
- lr:
- batch_size:
- buffer_capacity:
- target_update_freq:

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       |           |           |           |           |         |
| ...       |           |           |           |           |         |

**Observations**

**Choice for next experiment**
```

---

## Experiment 1 — 2026-05-21
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.9999
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 1500

**Results**
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.1       | 39.9      | ~0.668  |
| 200       | 0         | 2         | 0.2       | 51.4      | ~0.396  |
| 300       | 0         | 1         | 0.1       | 73.9      | ~0.188  |
| 400       | 0         | 2         | 0.1       | 256.0     | ~0.05   |
| 500       | 0         | 2         | 0.1       | 413.0     | ~0.05   |
| 600       | 0         | 2         | 0.3       | 284.3     | ~0.05   |
| 700       | 0         | 2         | 0.4       | 544.9     | ~0.05   |
| 800       | 0         | 2         | 0.4       | 427.3     | ~0.05   |
| 900       | 0         | 2         | 0.4       | 447.7     | ~0.05   |
| 1000      | 0         | 2         | 0.5       | 267.1     | ~0.05   |
| 1100      | 0         | 2         | 0.4       | 542.5     | ~0.05   |
| 1200      | 0         | 3         | 0.5       | 493.4     | ~0.05   |
| 1300      | 0         | 3         | 0.5       | 321.0     | ~0.05   |
| 1400      | 0         | 3         | 0.5       | 370.4     | ~0.05   |
| 1500      | 0         | 3         | 0.7       | 404.6     | ~0.05   |

**Observations**
    Based on steps avg we can see that the network learns to survive more. But it does not look for more food. The Epsilon decays very fast so the network rarely encounters situations where the snake is longer.

**Choice for next experiment**
    In the next case we would adjust the Epsilon decay so it has more time learning from random states.

### Experiment 2 — 2026-05-22
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 1500

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.2       | 42.7      | ~0.806  |
| 200       | 0         | 2         | 0.2       | 48.0      | ~0.631  |
| 300       | 0         | 2         | 0.1       | 57.9      | ~0.470  |
| 400       | 0         | 1         | 0.1       | 58.2      | ~0.349  |
| 500       | 0         | 1         | 0.1       | 56.4      | ~0.262  |
| 600       | 0         | 2         | 0.3       | 86.4      | ~0.169  |
| 700       | 0         | 2         | 0.4       | 150.2     | ~0.079  |
| 800       | 0         | 2         | 0.4       | 223.6     | ~0.05   |
| 900       | 0         | 2         | 0.4       | 212.6     | ~0.05   |
| 1000      | 0         | 2         | 0.5       | 358.7     | ~0.05   |
| 1100      | 0         | 3         | 0.4       | 350.2     | ~0.05   |
| 1200      | 0         | 3         | 0.4       | 376.1     | ~0.05   |
| 1300      | 0         | 3         | 0.6       | 409.5     | ~0.05   |
| 1400      | 0         | 3         | 0.6       | 363.7     | ~0.05   |
| 1500      | 0         | 3         | 0.6       | 461.6     | ~0.05   |

**Observations**
    Looking at the score avg the model is not learning to eat more food but learns how to survive longer while the epsilon is still decreasing.

**Choice for next experiment**
    We are going to change the reward values in order to get better eat-more learning.