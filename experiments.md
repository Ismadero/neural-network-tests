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
- reward:

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
- reward: +10 if eaten, -0.1 per step, -10 if die

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
- reward: +10 if eaten, -0.1 per step, -10 if die

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

### Experiment 3 — 2026-05-23
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 1500
- reward: +10 if eaten, +0.1 if moving closer to food, -0.1 if moving away, -10 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.1       | 44.1      | ~0.801  |
| 200       | 0         | 1         | 0.2       | 40.6      | ~0.650  |
| 300       | 0         | 1         | 0.1       | 53.2      | ~0.496  |
| 400       | 0         | 2         | 0.3       | 57.6      | ~0.370  |
| 500       | 0         | 1         | 0.1       | 61.7      | ~0.270  |
| 600       | 0         | 2         | 0.2       | 80.1      | ~0.180  |
| 700       | 0         | 1         | 0.3       | 163.2     | ~0.079  |
| 800       | 0         | 2         | 0.3       | 273.3     | ~0.05   |
| 900       | 0         | 2         | 0.4       | 304.6     | ~0.05   |
| 1000      | 0         | 2         | 0.5       | 280.9     | ~0.05   |
| 1100      | 0         | 2         | 0.5       | 383.3     | ~0.05   |
| 1200      | 0         | 3         | 0.3       | 327.6     | ~0.05   |
| 1300      | 0         | 3         | 0.5       | 399.9     | ~0.05   |
| 1400      | 0         | 3         | 0.3       | 511.5     | ~0.05   |
| 1500      | 0         | 2         | 0.5       | 401.6     | ~0.05   |

**Observations**
    In this case the model learns to make circles, again it eats little food and repeats this behavior where it just loops in circles. 

**Choice for next experiment**
    We will adjust the reward shaping to make moving away more punishing, or getting closer more rewarding, to discourage the circular looping behavior.
    The changes will be applied with the following values: +0.2 / -0.5

### Experiment 4 — 2026-05-23
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 1500
- reward: +10 if eaten, **BUG** -0.5 if moving closer to food, +0.2 if moving away, -10 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.2       | 35.2      | ~0.837  |
| 200       | 0         | 2         | 0.2       | 43.1      | ~0.671  |
| 300       | 0         | 2         | 0.1       | 50.8      | ~0.518  |
| 400       | 0         | 1         | 0.1       | 52.3      | ~0.397  |
| 500       | 0         | 1         | 0.2       | 71.9      | ~0.276  |
| 600       | 0         | 1         | 0.1       | 85.6      | ~0.179  |
| 700       | 0         | 2         | 0.3       | 114.5     | ~0.100  |
| 800       | 0         | 1         | 0.3       | 209.2     | ~0.05   |
| 900       | 0         | 1         | 0.3       | 328.9     | ~0.05   |
| 1000      | 0         | 2         | 0.4       | 334.8     | ~0.05   |
| 1100      | 0         | 2         | 0.3       | 364.2     | ~0.05   |
| 1200      | 0         | 1         | 0.3       | 311.9     | ~0.05   |
| 1300      | 0         | 2         | 0.3       | 313.8     | ~0.05   |
| 1400      | 0         | 2         | 0.2       | 216.6     | ~0.05   |
| 1500      | 0         | 1         | 0.3       | 323.3     | ~0.05   |

**Observations**
    In this case the model behaves strangely and it seems that it wants to be away from the food instead to get closer.

**Choice for next experiment**
    It was a logic bug where I put the reward shaping inverted, in the next step I'm going to fix this and see new results. :)

### Experiment 5 — 2026-05-23
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 1500
- reward: +10 if eaten, **FIX** +0.2 if moving closer to food, -0.5 if moving away, -10 if die
**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.2       | 38.9      | ~0.822  |
| 200       | 0         | 1         | 0.2       | 46.2      | ~0.649  |
| 300       | 0         | 1         | 0.2       | 49.3      | ~0.505  |
| 400       | 0         | 2         | 0.1       | 65.7      | ~0.361  |
| 500       | 0         | 1         | 0.2       | 61.6      | ~0.264  |
| 600       | 0         | 1         | 0.2       | 98.9      | ~0.160  |
| 700       | 0         | 1         | 0.2       | 129.1     | ~0.084  |
| 800       | 0         | 2         | 0.3       | 295.6     | ~0.05   |
| 900       | 0         | 2         | 0.3       | 311.3     | ~0.05   |
| 1000      | 0         | 3         | 0.4       | 358.1     | ~0.05   |
| 1100      | 0         | 1         | 0.4       | 478.7     | ~0.05   |
| 1200      | 0         | 3         | 0.6       | 251.3     | ~0.05   |
| 1300      | 0         | 2         | 0.4       | 303.2     | ~0.05   |
| 1400      | 0         | 1         | 0.3       | 253.5     | ~0.05   |
| 1500      | 0         | 2         | 0.4       | 205.9     | ~0.05   |

**Observations**
    The snake approaches food but then moves away without eating. Based in Exp 1 and 2, where score avg starts rising once epsilon stabilizes at 0.05 — the model needs more exploitation time to consolidate the learned behavior. The current 1500 episodes may not be enough training at low epsilon.

**Choice for next experiment**
    Load exp_5.pth and continue training with the same hyperparameters but more episodes (3000).

### Experiment 6 — 2026-05-23
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (loaded from exp_5.pth, continued from ep 1500)
- reward: +10 if eaten, +0.2 if moving closer to food, -0.5 if moving away, -10 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 1600      | 0         | 2         | 0.2       | 183.7     | ~0.05   |
| 1700      | 0         | 2         | 0.2       | 283.6     | ~0.05   |
| 1800      | 0         | 2         | 0.2       | 273.1     | ~0.05   |
| 1900      | 0         | 1         | 0.2       | 452.6     | ~0.05   |
| 2000      | 0         | 2         | 0.2       | 288.7     | ~0.05   |
| 2100      | 0         | 1         | 0.1       | 297.9     | ~0.05   |
| 2200      | 0         | 1         | 0.1       | 176.2     | ~0.05   |
| 2300      | 0         | 1         | 0.0       | 74.0      | ~0.05   |
| 2400      | 0         | 1         | 0.1       | 9.2       | ~0.05   |
| 2500      | 0         | 1         | 0.0       | 9.5       | ~0.05   |
| 2600      | 0         | 2         | 0.1       | 9.0       | ~0.05   |
| 2700      | 0         | 1         | 0.1       | 9.4       | ~0.05   |
| 2800      | 0         | 1         | 0.0       | 8.8       | ~0.05   |
| 2900      | 0         | 1         | 0.0       | 9.2       | ~0.05   |
| 3000      | 0         | 1         | 0.0       | 8.8       | ~0.05   |

**Observations**
    In this case the model learns how to die fast, not the result i was hoping for but what i got.
    Based on experiments 1, 2 the actual reward shaping is behaving worst than the simple reward.

**Choice for next experiment**
    Load exp_2.pth and continue training with the same hyperparameters but more episodes (3000)

### Experiment 7 — 2026-05-23
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (loaded from exp_2.pth, continued from ep 1500)
- reward: +10 if eaten, -0.1 per step, -10 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 1600      | 0         | 3         | 0.5       | 373.6     | ~0.05   |
| 1700      | 0         | 3         | 0.6       | 377.2     | ~0.05   |
| 1800      | 0         | 2         | 0.3       | 274.6     | ~0.05   |
| 1900      | 0         | 3         | 0.5       | 374.7     | ~0.05   |
| 2000      | 0         | 3         | 0.6       | 447.4     | ~0.05   |
| 2100      | 0         | 2         | 0.5       | 543.9     | ~0.05   |
| 2200      | 0         | 2         | 0.6       | 440.6     | ~0.05   |
| 2300      | 0         | 2         | 0.5       | 398.6     | ~0.05   |
| 2400      | 0         | 3         | 0.6       | 430.2     | ~0.05   |
| 2500      | 0         | 3         | 0.6       | 333.4     | ~0.05   |
| 2600      | 0         | 3         | 0.5       | 309.9     | ~0.05   |
| 2700      | 0         | 2         | 0.6       | 412.1     | ~0.05   |
| 2800      | 0         | 3         | 0.5       | 336.6     | ~0.05   |
| 2900      | 0         | 4         | 0.5       | 356.4     | ~0.05   |
| 3000      | 0         | 3         | 0.8       | 308.1     | ~0.05   |

**Observations**
    In this case the growth of score avg is noticeable but when evaluated we can see that the snake loops in circles most of the time, that explains the high steps avg.

**Choice for next experiment**
    We will set a step limit per episode according to the next formula: step_max = 100 + 50 * score.

### Experiment 8 — 2026-05-23
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -0.1 per step, -10 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.2       | 42.5      | ~0.807  |
| 200       | 0         | 1         | 0.1       | 45.7      | ~0.640  |
| 300       | 0         | 1         | 0.1       | 35.1      | ~0.534  |
| 400       | 0         | 2         | 0.2       | 53.0      | ~0.408  |
| 500       | 0         | 2         | 0.2       | 51.9      | ~0.313  |
| 600       | 0         | 1         | 0.2       | 62.7      | ~0.228  |
| 700       | 0         | 2         | 0.2       | 55.8      | ~0.172  |
| 800       | 0         | 2         | 0.2       | 68.3      | ~0.122  |
| 900       | 0         | 1         | 0.2       | 74.8      | ~0.084  |
| 1000      | 0         | 2         | 0.2       | 78.5      | ~0.056  |
| 1100      | 0         | 2         | 0.2       | 83.6      | ~0.05   |
| 1200      | 0         | 2         | 0.2       | 77.4      | ~0.05   |
| 1300      | 0         | 3         | 0.1       | 82.9      | ~0.05   |
| 1400      | 0         | 2         | 0.2       | 84.5      | ~0.05   |
| 1500      | 0         | 2         | 0.2       | 88.2      | ~0.05   |
| 1600      | 0         | 3         | 0.2       | 84.7      | ~0.05   |
| 1700      | 0         | 2         | 0.3       | 84.8      | ~0.05   |
| 1800      | 0         | 2         | 0.3       | 87.7      | ~0.05   |
| 1900      | 0         | 2         | 0.2       | 92.2      | ~0.05   |
| 2000      | 0         | 2         | 0.2       | 95.0      | ~0.05   |
| 2100      | 0         | 2         | 0.2       | 87.3      | ~0.05   |
| 2200      | 0         | 2         | 0.2       | 91.5      | ~0.05   |
| 2300      | 0         | 3         | 0.3       | 91.6      | ~0.05   |
| 2400      | 0         | 1         | 0.1       | 89.1      | ~0.05   |
| 2500      | 0         | 2         | 0.2       | 87.4      | ~0.05   |
| 2600      | 0         | 3         | 0.2       | 88.2      | ~0.05   |
| 2700      | 0         | 3         | 0.2       | 94.7      | ~0.05   |
| 2800      | 0         | 2         | 0.2       | 96.7      | ~0.05   |
| 2900      | 0         | 3         | 0.3       | 93.2      | ~0.05   |
| 3000      | 0         | 3         | 0.3       | 92.5      | ~0.05   |

**Observations**
    In this case there is not much to see, only that the model progressively tends to live longer, also the snake keeps looping when evaluated.

**Choice for next experiment**
    Change gamma to 0.6 in order to make it go straighter and avoid looping.

### Experiment 9 — 2026-05-26
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -0.1 per step, -10 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.1       | 35.4      | ~0.836  |
| 200       | 0         | 1         | 0.1       | 41.4      | ~0.676  |
| 300       | 0         | 1         | 0.2       | 44.9      | ~0.538  |
| 400       | 0         | 2         | 0.2       | 42.7      | ~0.433  |
| 500       | 0         | 2         | 0.2       | 51.2      | ~0.333  |
| 600       | 0         | 2         | 0.4       | 48.4      | ~0.261  |
| 700       | 0         | 2         | 0.3       | 55.5      | ~0.197  |
| 800       | 0         | 2         | 0.2       | 58.9      | ~0.146  |
| 900       | 0         | 2         | 0.3       | 60.4      | ~0.108  |
| 1000      | 0         | 2         | 0.4       | 62.6      | ~0.078  |
| 1100      | 0         | 2         | 0.5       | 78.1      | ~0.053  |
| 1200      | 0         | 4         | 0.5       | 92.2      | ~0.05   |
| 1300      | 0         | 3         | 0.4       | 90.7      | ~0.05   |
| 1400      | 0         | 3         | 0.6       | 86.0      | ~0.05   |
| 1500      | 0         | 4         | 0.3       | 79.9      | ~0.05   |
| 1600      | 0         | 4         | 0.5       | 80.1      | ~0.05   |
| 1700      | 0         | 3         | 0.5       | 92.9      | ~0.05   |
| 1800      | 0         | 4         | 0.4       | 82.4      | ~0.05   |
| 1900      | 0         | 3         | 0.5       | 70.6      | ~0.05   |
| 2000      | 0         | 2         | 0.3       | 78.2      | ~0.05   |
| 2100      | 0         | 5         | 0.5       | 86.7      | ~0.05   |
| 2200      | 0         | 2         | 0.5       | 64.7      | ~0.05   |
| 2300      | 0         | 3         | 0.4       | 81.5      | ~0.05   |
| 2400      | 0         | 2         | 0.4       | 86.1      | ~0.05   |
| 2500      | 0         | 3         | 0.4       | 78.2      | ~0.05   |
| 2600      | 0         | 2         | 0.3       | 83.7      | ~0.05   |
| 2700      | 0         | 3         | 0.5       | 84.2      | ~0.05   |
| 2800      | 0         | 3         | 0.5       | 90.1      | ~0.05   |
| 2900      | 0         | 3         | 0.5       | 91.5      | ~0.05   |
| 3000      | 0         | 3         | 0.4       | 88.0      | ~0.05   |

**Observations**
    We can see a better growth in score_avg, with better results in score max. When evaluated the snake behaves less irregularly moving straighter.

**Choice for next experiment**
    Because the model eats little food, I decided to make the eating reward higher (50), thus it should make the model search for more food when running.

### Experiment 10 — 2026-05-27
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +50 if eaten, -0.1 per step, -10 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.1       | 37.4      | ~0.828  |
| 200       | 0         | 2         | 0.1       | 40.5      | ~0.673  |
| 300       | 0         | 1         | 0.1       | 44.4      | ~0.537  |
| 400       | 0         | 1         | 0.2       | 45.7      | ~0.425  |
| 500       | 0         | 2         | 0.2       | 46.4      | ~0.336  |
| 600       | 0         | 3         | 0.2       | 43.0      | ~0.269  |
| 700       | 0         | 2         | 0.3       | 49.6      | ~0.209  |
| 800       | 0         | 2         | 0.2       | 41.9      | ~0.169  |
| 900       | 0         | 2         | 0.3       | 47.5      | ~0.133  |
| 1000      | 0         | 2         | 0.3       | 56.8      | ~0.100  |
| 1100      | 0         | 2         | 0.3       | 35.1      | ~0.083  |
| 1200      | 0         | 2         | 0.3       | 36.6      | ~0.069  |
| 1300      | 0         | 2         | 0.3       | 35.5      | ~0.057  |
| 1400      | 0         | 2         | 0.3       | 43.5      | ~0.05   |
| 1500      | 0         | 2         | 0.4       | 31.2      | ~0.05   |
| 1600      | 0         | 2         | 0.2       | 27.4      | ~0.05   |
| 1700      | 0         | 2         | 0.3       | 36.1      | ~0.05   |
| 1800      | 0         | 2         | 0.3       | 31.1      | ~0.05   |
| 1900      | 0         | 2         | 0.3       | 38.2      | ~0.05   |
| 2000      | 0         | 2         | 0.4       | 24.1      | ~0.05   |
| 2100      | 0         | 2         | 0.4       | 25.9      | ~0.05   |
| 2200      | 0         | 2         | 0.4       | 26.1      | ~0.05   |
| 2300      | 0         | 1         | 0.4       | 31.1      | ~0.05   |
| 2400      | 0         | 2         | 0.3       | 26.9      | ~0.05   |
| 2500      | 0         | 1         | 0.2       | 23.7      | ~0.05   |
| 2600      | 0         | 2         | 0.3       | 23.6      | ~0.05   |
| 2700      | 0         | 2         | 0.3       | 28.1      | ~0.05   |
| 2800      | 0         | 2         | 0.3       | 24.6      | ~0.05   |
| 2900      | 0         | 2         | 0.3       | 30.8      | ~0.05   |
| 3000      | 0         | 2         | 0.4       | 30.6      | ~0.05   |

**Observations**
    We can observe that the step_avg keeps low values, same happens with the score_avg, this happens when higher eating rewards appears, the model looks to eat once and then die.

**Choice for next experiment** 
    Lower the eating reward till 10 again, but we increase the death penalty to -25, so the ratio between eat:die is 1:2.5.

### Experiment 11 — 2026-05-27
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -0.1 per step, -25 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.1       | 34.3      | ~0.841  |
| 200       | 0         | 3         | 0.1       | 35.5      | ~0.701  |
| 300       | 0         | 1         | 0.1       | 30.3      | ~0.599  |
| 400       | 0         | 1         | 0.1       | 37.8      | ~0.494  |
| 500       | 0         | 1         | 0.1       | 38.0      | ~0.406  |
| 600       | 0         | 2         | 0.2       | 38.4      | ~0.334  |
| 700       | 0         | 3         | 0.2       | 42.7      | ~0.268  |
| 800       | 0         | 2         | 0.2       | 54.5      | ~0.203  |
| 900       | 0         | 2         | 0.2       | 46.2      | ~0.161  |
| 1000      | 0         | 4         | 0.3       | 63.0      | ~0.117  |
| 1100      | 0         | 3         | 0.4       | 84.4      | ~0.076  |
| 1200      | 0         | 3         | 0.3       | 81.0      | ~0.051  |
| 1300      | 0         | 3         | 0.4       | 86.8      | ~0.05   |
| 1400      | 0         | 4         | 0.6       | 97.0      | ~0.05   |
| 1500      | 0         | 4         | 0.6       | 91.1      | ~0.05   |
| 1600      | 0         | 4         | 0.7       | 97.8      | ~0.05   |
| 1700      | 0         | 4         | 0.8       | 101.0     | ~0.05   |
| 1800      | 0         | 5         | 0.9       | 100.5     | ~0.05   |
| 1900      | 0         | 4         | 0.7       | 94.5      | ~0.05   |
| 2000      | 0         | 4         | 0.8       | 92.1      | ~0.05   |
| 2100      | 0         | 4         | 0.8       | 92.2      | ~0.05   |
| 2200      | 0         | 4         | 0.8       | 96.6      | ~0.05   |
| 2300      | 0         | 5         | 0.8       | 95.8      | ~0.05   |
| 2400      | 0         | 4         | 0.9       | 100.3     | ~0.05   |
| 2500      | 0         | 4         | 0.9       | 95.8      | ~0.05   |
| 2600      | 0         | 5         | 1.1       | 100.3     | ~0.05   |
| 2700      | 0         | 5         | 1.0       | 96.5      | ~0.05   |
| 2800      | 0         | 5         | 1.1       | 101.0     | ~0.05   |
| 2900      | 0         | 5         | 0.9       | 104.2     | ~0.05   |
| 3000      | 0         | 6         | 1.2       | 95.3      | ~0.05   |

**Observations**
    We can see that we obtained the best result in score_avg and score_max so far. It tends to use the maximum steps available. Also, it learns better when epsilon stays at 0.05.

**Choice for next experiment**
    I would like to try this with a higher gamma, so the model values future rewards more heavily. I'm going to change it to 0.9. Exp_12.
    Otherwise, later I would like to adjust the death penalty a little more in order to find the value with the best results.

### Experiment 12 — 2026-05-27
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.90
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -0.1 per step, -25 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.1       | 36.3      | ~0.833  |
| 200       | 0         | 1         | 0.1       | 35.8      | ~0.693  |
| 300       | 0         | 1         | 0.1       | 38.7      | ~0.568  |
| 400       | 0         | 2         | 0.2       | 38.7      | ~0.466  |
| 500       | 0         | 1         | 0.1       | 36.0      | ~0.387  |
| 600       | 0         | 2         | 0.2       | 42.8      | ~0.311  |
| 700       | 0         | 2         | 0.2       | 50.0      | ~0.241  |
| 800       | 0         | 1         | 0.2       | 50.5      | ~0.187  |
| 900       | 0         | 1         | 0.3       | 55.7      | ~0.141  |
| 1000      | 0         | 2         | 0.3       | 63.6      | ~0.102  |
| 1100      | 0         | 2         | 0.3       | 70.8      | ~0.071  |
| 1200      | 0         | 2         | 0.3       | 61.7      | ~0.052  |
| 1300      | 0         | 1         | 0.2       | 71.6      | ~0.05   |
| 1400      | 0         | 3         | 0.3       | 71.4      | ~0.05   |
| 1500      | 0         | 3         | 0.3       | 65.3      | ~0.05   |
| 1600      | 0         | 2         | 0.3       | 76.5      | ~0.05   |
| 1700      | 0         | 2         | 0.3       | 76.4      | ~0.05   |
| 1800      | 0         | 4         | 0.4       | 76.7      | ~0.05   |
| 1900      | 0         | 4         | 0.4       | 76.9      | ~0.05   |
| 2000      | 0         | 3         | 0.3       | 77.1      | ~0.05   |
| 2100      | 0         | 3         | 0.4       | 77.6      | ~0.05   |
| 2200      | 0         | 2         | 0.3       | 69.4      | ~0.05   |
| 2300      | 0         | 3         | 0.2       | 73.5      | ~0.05   |
| 2400      | 0         | 3         | 0.4       | 72.8      | ~0.05   |
| 2500      | 0         | 3         | 0.5       | 80.8      | ~0.05   |
| 2600      | 0         | 2         | 0.3       | 76.5      | ~0.05   |
| 2700      | 0         | 4         | 0.5       | 71.0      | ~0.05   |
| 2800      | 0         | 4         | 0.5       | 69.0      | ~0.05   |
| 2900      | 0         | 4         | 0.3       | 68.0      | ~0.05   |
| 3000      | 0         | 3         | 0.5       | 72.9      | ~0.05   |

**Observations**
    In this case we can appreciate a worse performance compared to the previous exp, both in survival time as well as in score avg. This happens because the model is not correct in its calibration yet, for a higher gamma it needs a training that has good results before applying the higher values, that's why we should set a dynamic gamma that grows as the model learns and get bigger snake sizes.  

**Choice for next experiment**
    First I will try with lower gamma values i.e. 0.4.

### Experiment 13 — 2026-05-27
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.40
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -0.1 per step, -25 if die

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.1       | 36.3      | ~0.833  |
| 200       | 0         | 1         | 0.1       | 37.8      | ~0.686  |
| 300       | 0         | 1         | 0.1       | 35.3      | ~0.572  |
| 400       | 0         | 1         | 0.1       | 33.8      | ~0.481  |
| 500       | 0         | 2         | 0.2       | 32.8      | ~0.406  |
| 600       | 0         | 2         | 0.1       | 35.4      | ~0.339  |
| 700       | 0         | 2         | 0.2       | 44.4      | ~0.270  |
| 800       | 0         | 3         | 0.3       | 51.1      | ~0.208  |
| 900       | 0         | 2         | 0.2       | 54.3      | ~0.158  |
| 1000      | 0         | 2         | 0.3       | 67.1      | ~0.113  |
| 1100      | 0         | 3         | 0.4       | 78.6      | ~0.076  |
| 1200      | 0         | 2         | 0.4       | 85.9      | ~0.05   |
| 1300      | 0         | 2         | 0.4       | 89.7      | ~0.05   |
| 1400      | 0         | 3         | 0.3       | 82.4      | ~0.05   |
| 1500      | 0         | 3         | 0.6       | 93.3      | ~0.05   |
| 1600      | 0         | 2         | 0.5       | 86.1      | ~0.05   |
| 1700      | 0         | 4         | 0.7       | 85.7      | ~0.05   |
| 1800      | 0         | 5         | 0.7       | 88.8      | ~0.05   |
| 1900      | 0         | 4         | 0.8       | 95.3      | ~0.05   |
| 2000      | 0         | 5         | 0.7       | 93.5      | ~0.05   |
| 2100      | 0         | 4         | 0.7       | 96.7      | ~0.05   |
| 2200      | 0         | 4         | 0.9       | 95.5      | ~0.05   |
| 2300      | 0         | 4         | 0.8       | 89.4      | ~0.05   |
| 2400      | 0         | 4         | 0.8       | 90.9      | ~0.05   |
| 2500      | 0         | 5         | 0.7       | 94.0      | ~0.05   |
| 2600      | 0         | 5         | 0.8       | 97.7      | ~0.05   |
| 2700      | 0         | 5         | 0.9       | 94.8      | ~0.05   |
| 2800      | 0         | 5         | 1.0       | 103.1     | ~0.05   |
| 2900      | 0         | 4         | 1.0       | 99.1      | ~0.05   |
| 3000      | 0         | 6         | 1.0       | 102.1     | ~0.05   |

**Observations**
    We can observe a similar behavior as experiment 11 with gamma = 0.6, in this case it reaches lower values in score_avg, and when evaluated it tends to loop more than experiment 11.

**Choice for next experiment**
    Return to gamma = 0.6, but modify the reward shaping, just like exp 3 but only rewarding when the model is closer than it has ever been to the current food in the episode, this may avoid looping.

### Experiment 14 — 2026-05-27
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.2       | 37.7      | ~0.827  |
| 200       | 0         | 2         | 0.1       | 38.6      | ~0.678  |
| 300       | 0         | 2         | 0.2       | 38.6      | ~0.557  |
| 400       | 0         | 1         | 0.2       | 48.5      | ~0.435  |
| 500       | 0         | 2         | 0.2       | 48.3      | ~0.340  |
| 600       | 0         | 3         | 0.2       | 52.8      | ~0.260  |
| 700       | 0         | 2         | 0.2       | 68.7      | ~0.184  |
| 800       | 0         | 3         | 0.3       | 70.0      | ~0.129  |
| 900       | 0         | 3         | 0.3       | 75.7      | ~0.088  |
| 1000      | 0         | 3         | 0.5       | 91.6      | ~0.056  |
| 1100      | 0         | 2         | 0.5       | 99.1      | ~0.05   |
| 1200      | 0         | 3         | 0.7       | 97.5      | ~0.05   |
| 1300      | 0         | 4         | 0.7       | 89.4      | ~0.05   |
| 1400      | 0         | 3         | 0.6       | 88.3      | ~0.05   |
| 1500      | 0         | 4         | 0.8       | 90.2      | ~0.05   |
| 1600      | 0         | 4         | 0.7       | 99.0      | ~0.05   |
| 1700      | 0         | 2         | 0.4       | 72.6      | ~0.05   |
| 1800      | 0         | 3         | 0.4       | 79.9      | ~0.05   |
| 1900      | 0         | 3         | 0.5       | 76.5      | ~0.05   |
| 2000      | 0         | 2         | 0.5       | 86.7      | ~0.05   |
| 2100      | 0         | 3         | 0.5       | 83.4      | ~0.05   |
| 2200      | 0         | 3         | 0.4       | 79.2      | ~0.05   |
| 2300      | 0         | 3         | 0.5       | 88.4      | ~0.05   |
| 2400      | 0         | 6         | 0.5       | 92.8      | ~0.05   |
| 2500      | 0         | 4         | 0.5       | 75.5      | ~0.05   |
| 2600      | 0         | 4         | 0.8       | 97.8      | ~0.05   |
| 2700      | 0         | 5         | 0.6       | 90.4      | ~0.05   |
| 2800      | 0         | 4         | 0.6       | 89.7      | ~0.05   |
| 2900      | 0         | 3         | 0.8       | 91.9      | ~0.05   |
| 3000      | 0         | 4         | 0.6       | 93.9      | ~0.05   |

**Observations**
    Although the score avg didn't reach 1, score max reaches the same highest value as experiment 11, and the step average is slightly lower than what we saw in exp 11. According to the evaluation, we can appreciate that it tends to get closer to food instead of going anywhere like it used to in experiment 11.

**Choice for next experiment**
    Because the model seems to behave erratically most of the time, I would add a 4th channel to the tensor given to the network indicating the actual direction of the snake. And I will run this same experiment with that 4th channel.

### Experiment 15 — 2026-05-27
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.1       | 38.8      | ~0.823  |
| 200       | 0         | 2         | 0.2       | 40.9      | ~0.667  |
| 300       | 0         | 1         | 0.2       | 37.9      | ~0.549  |
| 400       | 0         | 2         | 0.2       | 43.3      | ~0.440  |
| 500       | 0         | 2         | 0.2       | 50.5      | ~0.341  |
| 600       | 0         | 1         | 0.2       | 57.5      | ~0.254  |
| 700       | 0         | 2         | 0.4       | 60.4      | ~0.187  |
| 800       | 0         | 2         | 0.4       | 63.4      | ~0.136  |
| 900       | 0         | 4         | 0.6       | 70.2      | ~0.095  |
| 1000      | 0         | 3         | 0.5       | 76.4      | ~0.065  |
| 1100      | 0         | 3         | 0.8       | 89.0      | ~0.05   |
| 1200      | 0         | 5         | 0.8       | 96.1      | ~0.05   |
| 1300      | 0         | 4         | 1.1       | 104.9     | ~0.05   |
| 1400      | 0         | 5         | 1.3       | 111.9     | ~0.05   |
| 1500      | 0         | 5         | 1.0       | 90.8      | ~0.05   |
| 1600      | 0         | 5         | 1.3       | 106.5     | ~0.05   |
| 1700      | 0         | 5         | 1.0       | 85.6      | ~0.05   |
| 1800      | 0         | 4         | 0.9       | 81.2      | ~0.05   |
| 1900      | 0         | 5         | 1.0       | 93.2      | ~0.05   |
| 2000      | 0         | 4         | 1.0       | 91.7      | ~0.05   |
| 2100      | 0         | 5         | 1.2       | 100.4     | ~0.05   |
| 2200      | 0         | 6         | 1.0       | 88.6      | ~0.05   |
| 2300      | 0         | 6         | 1.4       | 99.1      | ~0.05   |
| 2400      | 0         | 7         | 1.4       | 114.5     | ~0.05   |
| 2500      | 0         | 6         | 1.4       | 94.7      | ~0.05   |
| 2600      | 0         | 7         | 1.6       | 103.7     | ~0.05   |
| 2700      | 0         | 7         | 1.3       | 109.2     | ~0.05   |
| 2800      | 0         | 7         | 1.5       | 107.8     | ~0.05   |
| 2900      | 0         | 8         | 1.4       | 95.2      | ~0.05   |
| 3000      | 0         | 8         | 1.6       | 106.8     | ~0.05   |

**Observations**
    We can observe an obvious improvement compared to previous experiments, reaching the best values ever — score max of 8 and score avg of 1.6. Adding the direction field greatly benefited learning, and it seems it was one of the biggest bottlenecks in the project.

**Choice for next experiment**
    Replicate experiment 11 with this new neural network architecture.

### Experiment 16 — 2026-05-28
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -0.1 per step, -25 if die
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.1       | 39.6      | ~0.819  |
| 200       | 0         | 1         | 0.1       | 48.8      | ~0.639  |
| 300       | 0         | 1         | 0.1       | 32.0      | ~0.542  |
| 400       | 0         | 2         | 0.2       | 33.8      | ~0.455  |
| 500       | 0         | 1         | 0.1       | 30.2      | ~0.390  |
| 600       | 0         | 2         | 0.2       | 35.5      | ~0.325  |
| 700       | 0         | 1         | 0.1       | 36.8      | ~0.269  |
| 800       | 0         | 2         | 0.2       | 47.2      | ~0.211  |
| 900       | 0         | 2         | 0.2       | 49.2      | ~0.165  |
| 1000      | 0         | 3         | 0.3       | 56.2      | ~0.124  |
| 1100      | 0         | 2         | 0.3       | 68.0      | ~0.088  |
| 1200      | 0         | 3         | 0.3       | 65.4      | ~0.063  |
| 1300      | 0         | 3         | 0.3       | 71.0      | ~0.05   |
| 1400      | 0         | 3         | 0.3       | 78.7      | ~0.05   |
| 1500      | 0         | 3         | 0.4       | 89.1      | ~0.05   |
| 1600      | 0         | 4         | 0.5       | 80.2      | ~0.05   |
| 1700      | 0         | 3         | 0.3       | 82.4      | ~0.05   |
| 1800      | 0         | 3         | 0.4       | 85.5      | ~0.05   |
| 1900      | 0         | 3         | 0.5       | 80.8      | ~0.05   |
| 2000      | 0         | 2         | 0.3       | 76.9      | ~0.05   |
| 2100      | 0         | 2         | 0.3       | 80.1      | ~0.05   |
| 2200      | 0         | 3         | 0.4       | 86.0      | ~0.05   |
| 2300      | 0         | 4         | 0.4       | 87.0      | ~0.05   |
| 2400      | 0         | 3         | 0.5       | 92.6      | ~0.05   |
| 2500      | 0         | 2         | 0.5       | 84.5      | ~0.05   |
| 2600      | 0         | 3         | 0.3       | 79.0      | ~0.05   |
| 2700      | 0         | 3         | 0.5       | 85.3      | ~0.05   |
| 2800      | 0         | 2         | 0.3       | 77.1      | ~0.05   |
| 2900      | 0         | 3         | 0.3       | 76.7      | ~0.05   |
| 3000      | 0         | 2         | 0.2       | 85.8      | ~0.05   |

**Observations**
    In this case, without the distance-based reward shaping, we can observe that the model does not learn properly, the score_avg and score_max both are poor compared to the experiments 11 and 15, curious observation about exp 11, not expected because that experiment gave us the better results at that moment, this indicates that the new architecture may behave differently in experiments done with the previous one.

**Choice for next experiment**
    Return to the reward shaping seen in experiment 15, but modifying gamma a little higher (0.70) in order to see how it behaves.

### Experiment 17 — 2026-05-28
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.70
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 2         | 0.2       | 35.7      | ~0.835  |
| 200       | 0         | 1         | 0.2       | 38.0      | ~0.687  |
| 300       | 0         | 2         | 0.2       | 42.1      | ~0.554  |
| 400       | 0         | 2         | 0.1       | 47.2      | ~0.436  |
| 500       | 0         | 1         | 0.2       | 49.4      | ~0.339  |
| 600       | 0         | 1         | 0.3       | 50.9      | ~0.262  |
| 700       | 0         | 2         | 0.3       | 48.3      | ~0.205  |
| 800       | 0         | 1         | 0.2       | 60.5      | ~0.151  |
| 900       | 0         | 3         | 0.4       | 67.3      | ~0.107  |
| 1000      | 0         | 3         | 0.4       | 75.1      | ~0.073  |
| 1100      | 0         | 2         | 0.5       | 83.4      | ~0.05   |
| 1200      | 0         | 3         | 0.4       | 81.6      | ~0.05   |
| 1300      | 0         | 3         | 0.6       | 87.1      | ~0.05   |
| 1400      | 0         | 2         | 0.4       | 85.6      | ~0.05   |
| 1500      | 0         | 3         | 0.5       | 87.9      | ~0.05   |
| 1600      | 0         | 2         | 0.6       | 90.1      | ~0.05   |
| 1700      | 0         | 3         | 0.6       | 84.2      | ~0.05   |
| 1800      | 0         | 5         | 0.9       | 93.0      | ~0.05   |
| 1900      | 0         | 4         | 0.8       | 102.3     | ~0.05   |
| 2000      | 0         | 3         | 0.5       | 84.5      | ~0.05   |
| 2100      | 0         | 3         | 0.5       | 85.3      | ~0.05   |
| 2200      | 0         | 3         | 0.7       | 92.2      | ~0.05   |
| 2300      | 0         | 4         | 0.6       | 97.5      | ~0.05   |
| 2400      | 0         | 3         | 0.6       | 87.5      | ~0.05   |
| 2500      | 0         | 4         | 0.7       | 96.1      | ~0.05   |
| 2600      | 0         | 3         | 0.6       | 89.7      | ~0.05   |
| 2700      | 0         | 3         | 0.6       | 88.7      | ~0.05   |
| 2800      | 0         | 3         | 0.6       | 86.5      | ~0.05   |
| 2900      | 0         | 4         | 0.8       | 94.0      | ~0.05   |
| 3000      | 0         | 4         | 0.7       | 98.5      | ~0.05   |

**Observations**
    Increasing gamma caused the model to learn more slowly than what we have seen in experiment 15. Thus gamma should stay lower than 0.70 for initial training.

**Choice for next experiment**
    Train with gamma 0.50 in order to test lower gammas.

### Experiment 18 — 2026-05-28
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.50
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 3000 (fresh training, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.1       | 38.2      | ~0.825  |
| 200       | 0         | 1         | 0.1       | 38.6      | ~0.677  |
| 300       | 0         | 1         | 0.1       | 41.2      | ~0.548  |
| 400       | 0         | 1         | 0.1       | 40.9      | ~0.445  |
| 500       | 0         | 2         | 0.2       | 37.0      | ~0.368  |
| 600       | 0         | 2         | 0.2       | 44.2      | ~0.294  |
| 700       | 0         | 2         | 0.1       | 41.9      | ~0.237  |
| 800       | 0         | 2         | 0.2       | 52.3      | ~0.182  |
| 900       | 0         | 2         | 0.2       | 56.9      | ~0.136  |
| 1000      | 0         | 2         | 0.2       | 65.8      | ~0.098  |
| 1100      | 0         | 4         | 0.4       | 77.1      | ~0.066  |
| 1200      | 0         | 3         | 0.4       | 86.8      | ~0.05   |
| 1300      | 0         | 3         | 0.3       | 87.6      | ~0.05   |
| 1400      | 0         | 2         | 0.4       | 81.4      | ~0.05   |
| 1500      | 0         | 2         | 0.4       | 82.9      | ~0.05   |
| 1600      | 0         | 2         | 0.4       | 83.0      | ~0.05   |
| 1700      | 0         | 2         | 0.3       | 89.5      | ~0.05   |
| 1800      | 0         | 3         | 0.5       | 80.9      | ~0.05   |
| 1900      | 0         | 4         | 0.5       | 84.5      | ~0.05   |
| 2000      | 0         | 5         | 0.7       | 86.2      | ~0.05   |
| 2100      | 0         | 3         | 0.7       | 88.5      | ~0.05   |
| 2200      | 0         | 4         | 0.8       | 89.0      | ~0.05   |
| 2300      | 0         | 6         | 0.7       | 83.6      | ~0.05   |
| 2400      | 0         | 4         | 0.9       | 91.0      | ~0.05   |
| 2500      | 0         | 4         | 0.8       | 93.8      | ~0.05   |
| 2600      | 0         | 4         | 0.8       | 88.2      | ~0.05   |
| 2700      | 0         | 4         | 1.0       | 93.8      | ~0.05   |
| 2800      | 0         | 6         | 1.0       | 89.6      | ~0.05   |
| 2900      | 0         | 6         | 1.2       | 95.1      | ~0.05   |
| 3000      | 0         | 5         | 1.0       | 90.6      | ~0.05   |

**Observations**
    Using gamma 0.50 also causes slow training, similar to gamma 0.70, but it gives better results. Anyway, the sweet spot of gamma is around 0.60.

**Choice for next experiment**
    I will take the result model made in experiment 15, copy its hyperparameters, and continue training it until it reaches 5000 episodes in order to see where the learning limit is for the current state.

---

### Experiment 19 — 2026-05-28
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 5000 (loaded model from exp_15, continued from episode 3000)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 3100      | 0         | 7         | 1.4       | 104.0     | ~0.05   |
| 3200      | 0         | 5         | 1.5       | 110.1     | ~0.05   |
| 3300      | 0         | 6         | 1.5       | 105.3     | ~0.05   |
| 3400      | 0         | 6         | 1.6       | 108.5     | ~0.05   |
| 3500      | 0         | 8         | 1.6       | 109.0     | ~0.05   |
| 3600      | 0         | 8         | 1.5       | 122.2     | ~0.05   |
| 3700      | 0         | 8         | 1.9       | 115.9     | ~0.05   |
| 3800      | 0         | 5         | 1.5       | 114.2     | ~0.05   |
| 3900      | 0         | 6         | 1.6       | 95.1      | ~0.05   |
| 4000      | 0         | 8         | 1.9       | 114.1     | ~0.05   |
| 4100      | 0         | 6         | 1.8       | 103.7     | ~0.05   |
| 4200      | 0         | 8         | 1.7       | 118.5     | ~0.05   |
| 4300      | 0         | 7         | 1.7       | 113.3     | ~0.05   |
| 4400      | 0         | 7         | 1.8       | 117.5     | ~0.05   |
| 4500      | 0         | 7         | 1.8       | 119.4     | ~0.05   |
| 4600      | 0         | 10        | 1.9       | 116.0     | ~0.05   |
| 4700      | 0         | 8         | 1.8       | 109.8     | ~0.05   |
| 4800      | 0         | 6         | 1.9       | 114.2     | ~0.05   |
| 4900      | 0         | 8         | 1.6       | 104.5     | ~0.05   |
| 5000      | 0         | 7         | 1.7       | 114.7     | ~0.05   |

**Observations**
    We can observe that the model learns until near episode 3700, then score_avg tends to oscillate between 1.5 and 1.9, also we can see that steps avg stays around 100, that means that the snake doesn't survive longer, this is clearly a limit to the training.

**Choice for next experiment**
    In order to see beyond this point I will train this same model until episode 7000, hoping to see further improvement in score_avg.

---

### Experiment 20 — 2026-05-28
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 7000 (loaded model from exp_19, continued from episode 5000)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 5100      | 0         | 7         | 1.7       | 103.6     | ~0.05   |
| 5200      | 0         | 10        | 1.9       | 112.4     | ~0.05   |
| 5300      | 0         | 8         | 1.9       | 131.1     | ~0.05   |
| 5400      | 0         | 7         | 2.0       | 124.6     | ~0.05   |
| 5500      | 0         | 9         | 1.6       | 109.7     | ~0.05   |
| 5600      | 0         | 9         | 1.8       | 109.3     | ~0.05   |
| 5700      | 0         | 8         | 1.6       | 108.7     | ~0.05   |
| 5800      | 0         | 8         | 1.9       | 120.1     | ~0.05   |
| 5900      | 0         | 6         | 1.6       | 109.2     | ~0.05   |
| 6000      | 0         | 7         | 1.7       | 99.5      | ~0.05   |
| 6100      | 0         | 7         | 1.7       | 106.9     | ~0.05   |
| 6200      | 0         | 10        | 2.1       | 131.4     | ~0.05   |
| 6300      | 0         | 7         | 1.9       | 106.5     | ~0.05   |
| 6400      | 0         | 10        | 1.9       | 107.2     | ~0.05   |
| 6500      | 0         | 8         | 2.0       | 131.4     | ~0.05   |
| 6600      | 0         | 7         | 1.8       | 124.0     | ~0.05   |
| 6700      | 0         | 9         | 1.4       | 113.7     | ~0.05   |
| 6800      | 0         | 5         | 1.3       | 115.0     | ~0.05   |
| 6900      | 0         | 6         | 1.1       | 102.4     | ~0.05   |
| 7000      | 0         | 5         | 1.2       | 103.9     | ~0.05   |

**Observations**
    In this case it reaches score avg 2.1 in episode 6200, the best that we can obtain so far, after that the model tends to lower values with terrible behavior.

**Choice for next experiment**
    In order to see if we reached the plateau I will train a new model until episode 50,000.

---

### Experiment 21 — 2026-06-06
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.60
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 50,000 (started fresh, no loaded model)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       | 0         | 1         | 0.1       | 39.2      | 0.821   |
| 200       | 0         | 1         | 0.2       | 41.6      | 0.663   |
| 300       | 0         | 1         | 0.1       | 38.9      | 0.544   |
| 400       | 0         | 3         | 0.2       | 45.1      | 0.432   |
| 500       | 0         | 2         | 0.2       | 43.2      | 0.346   |
| 600       | 0         | 1         | 0.3       | 48.7      | 0.270   |
| 700       | 0         | 2         | 0.3       | 55.4      | 0.204   |
| 800       | 0         | 1         | 0.2       | 65.6      | 0.146   |
| 900       | 0         | 3         | 0.4       | 75.1      | 0.100   |
| 1000      | 0         | 3         | 0.5       | 78.0      | 0.068   |
| 1100      | 0         | 3         | 0.4       | 77.9      | ~0.05   |
| 1200      | 0         | 4         | 0.7       | 100.9     | ~0.05   |
| 1300      | 0         | 3         | 0.5       | 86.3      | ~0.05   |
| 1400      | 0         | 3         | 0.4       | 87.3      | ~0.05   |
| 1500      | 0         | 3         | 0.5       | 88.2      | ~0.05   |
| 1600      | 0         | 3         | 0.5       | 87.9      | ~0.05   |
| 1700      | 0         | 4         | 0.6       | 87.8      | ~0.05   |
| 1800      | 0         | 3         | 0.5       | 91.8      | ~0.05   |
| 1900      | 0         | 3         | 0.5       | 90.7      | ~0.05   |
| 2000      | 0         | 3         | 0.4       | 88.5      | ~0.05   |
| 2100      | 0         | 4         | 0.5       | 89.2      | ~0.05   |
| 2200      | 0         | 4         | 0.6       | 84.3      | ~0.05   |
| 2300      | 0         | 6         | 0.7       | 91.8      | ~0.05   |
| 2400      | 0         | 6         | 0.9       | 92.9      | ~0.05   |
| 2500      | 0         | 6         | 0.9       | 101.5     | ~0.05   |
| 2600      | 0         | 5         | 1.0       | 102.6     | ~0.05   |
| 2700      | 0         | 5         | 1.1       | 109.2     | ~0.05   |
| 2800      | 0         | 4         | 1.1       | 99.4      | ~0.05   |
| 2900      | 0         | 5         | 1.0       | 96.9      | ~0.05   |
| 3000      | 0         | 7         | 1.1       | 105.1     | ~0.05   |
| 3100      | 0         | 7         | 1.6       | 117.4     | ~0.05   |
| 3200      | 0         | 6         | 1.4       | 117.8     | ~0.05   |
| 3300      | 0         | 7         | 1.7       | 124.6     | ~0.05   |
| 3400      | 0         | 6         | 1.6       | 116.4     | ~0.05   |
| 3500      | 0         | 9         | 1.6       | 127.2     | ~0.05   |
| 3600      | 0         | 6         | 1.5       | 107.9     | ~0.05   |
| 3700      | 0         | 6         | 1.4       | 99.2      | ~0.05   |
| 3800      | 0         | 9         | 1.7       | 112.8     | ~0.05   |
| 3900      | 0         | 8         | 1.7       | 109.7     | ~0.05   |
| 4000      | 0         | 7         | 2.1       | 121.5     | ~0.05   |
| 4100      | 0         | 8         | 2.0       | 124.1     | ~0.05   |
| 4200      | 0         | 8         | 2.0       | 133.3     | ~0.05   |
| 4300      | 0         | 7         | 1.9       | 114.3     | ~0.05   |
| 4400      | 0         | 8         | 2.1       | 118.5     | ~0.05   |
| 4500      | 0         | 8         | 2.5       | 127.4     | ~0.05   |
| 4600      | 0         | 9         | 2.0       | 123.6     | ~0.05   |
| 4700      | 0         | 8         | 2.4       | 130.1     | ~0.05   |
| 4800      | 0         | 13        | 2.3       | 134.7     | ~0.05   |
| 4900      | 0         | 10        | 2.6       | 136.2     | ~0.05   |
| 5000      | 0         | 7         | 2.7       | 125.1     | ~0.05   |
| 5100      | 0         | 14        | 2.7       | 136.2     | ~0.05   |
| 5200      | 0         | 9         | 2.2       | 116.2     | ~0.05   |
| 5300      | 0         | 12        | 2.6       | 121.6     | ~0.05   |
| 5400      | 0         | 11        | 2.3       | 115.2     | ~0.05   |
| 5500      | 0         | 8         | 2.3       | 116.5     | ~0.05   |
| 5600      | 0         | 11        | 2.9       | 128.6     | ~0.05   |
| 5700      | 0         | 15        | 3.2       | 142.5     | ~0.05   |
| 5800      | 0         | 7         | 2.5       | 116.3     | ~0.05   |
| 5900      | 0         | 15        | 2.9       | 119.6     | ~0.05   |
| 6000      | 0         | 9         | 3.0       | 139.6     | ~0.05   |
| 6100      | 0         | 10        | 2.9       | 127.4     | ~0.05   |
| 6200      | 0         | 14        | 3.1       | 140.4     | ~0.05   |
| 6300      | 0         | 13        | 3.1       | 128.7     | ~0.05   |
| 6400      | 0         | 12        | 3.2       | 118.2     | ~0.05   |
| 6500      | 0         | 14        | 3.5       | 140.2     | ~0.05   |
| 6600      | 0         | 12        | 3.2       | 129.0     | ~0.05   |
| 6700      | 0         | 10        | 2.7       | 117.0     | ~0.05   |
| 6800      | 0         | 12        | 2.8       | 129.1     | ~0.05   |
| 6900      | 0         | 11        | 2.9       | 124.8     | ~0.05   |
| 7000      | 0         | 8         | 2.5       | 115.1     | ~0.05   |
| 7100      | 0         | 10        | 2.5       | 105.6     | ~0.05   |
| 7200      | 0         | 10        | 3.0       | 117.6     | ~0.05   |
| 7300      | 0         | 10        | 2.3       | 107.7     | ~0.05   |
| 7400      | 0         | 9         | 2.3       | 98.2      | ~0.05   |
| 7500      | 0         | 7         | 2.0       | 95.1      | ~0.05   |
| 7600      | 0         | 13        | 2.7       | 118.7     | ~0.05   |
| 7700      | 0         | 9         | 2.9       | 122.5     | ~0.05   |
| 7800      | 0         | 11        | 2.8       | 113.7     | ~0.05   |
| 7900      | 0         | 11        | 2.4       | 109.5     | ~0.05   |
| 8000      | 0         | 9         | 2.9       | 120.5     | ~0.05   |
| 8100      | 0         | 10        | 2.8       | 119.5     | ~0.05   |
| 8200      | 0         | 9         | 2.9       | 109.2     | ~0.05   |
| 8300      | 0         | 13        | 3.0       | 122.4     | ~0.05   |
| 8400      | 0         | 10        | 3.1       | 123.7     | ~0.05   |
| 8500      | 0         | 11        | 2.6       | 113.0     | ~0.05   |
| 8600      | 0         | 11        | 3.0       | 120.5     | ~0.05   |
| 8700      | 0         | 11        | 3.0       | 112.4     | ~0.05   |
| 8800      | 0         | 11        | 2.8       | 116.2     | ~0.05   |
| 8900      | 0         | 14        | 3.1       | 133.9     | ~0.05   |
| 9000      | 0         | 8         | 2.4       | 101.7     | ~0.05   |
| 9100      | 0         | 11        | 2.8       | 110.6     | ~0.05   |
| 9200      | 0         | 10        | 3.1       | 125.2     | ~0.05   |
| 9300      | 0         | 9         | 2.8       | 111.0     | ~0.05   |
| 9400      | 0         | 12        | 3.3       | 121.1     | ~0.05   |
| 9500      | 0         | 11        | 3.2       | 109.9     | ~0.05   |
| 9600      | 0         | 14        | 3.5       | 128.4     | ~0.05   |
| 9700      | 0         | 10        | 3.3       | 121.6     | ~0.05   |
| 9800      | 0         | 11        | 3.2       | 127.0     | ~0.05   |
| 9900      | 0         | 12        | 3.5       | 128.6     | ~0.05   |
| 10000     | 0         | 11        | 3.0       | 108.6     | ~0.05   |
| 10100     | 0         | 12        | 3.2       | 116.8     | ~0.05   |
| 10200     | 0         | 12        | 3.0       | 119.7     | ~0.05   |
| 10300     | 0         | 12        | 3.4       | 114.2     | ~0.05   |
| 10400     | 0         | 11        | 3.4       | 129.8     | ~0.05   |
| 10500     | 0         | 12        | 3.2       | 120.0     | ~0.05   |
| 10600     | 0         | 17        | 3.5       | 117.5     | ~0.05   |
| 10700     | 0         | 14        | 3.6       | 122.3     | ~0.05   |
| 10800     | 0         | 10        | 3.4       | 129.3     | ~0.05   |
| 10900     | 0         | 14        | 3.6       | 129.4     | ~0.05   |
| 11000     | 0         | 11        | 3.1       | 111.4     | ~0.05   |
| 11100     | 0         | 9         | 3.8       | 152.6     | ~0.05   |
| 11200     | 0         | 10        | 3.3       | 143.4     | ~0.05   |
| 11300     | 0         | 11        | 3.6       | 143.2     | ~0.05   |
| 11400     | 0         | 10        | 3.1       | 120.4     | ~0.05   |
| 11500     | 0         | 11        | 3.3       | 124.9     | ~0.05   |
| 11600     | 0         | 12        | 3.1       | 125.4     | ~0.05   |
| 11700     | 0         | 9         | 3.0       | 119.1     | ~0.05   |
| 11800     | 0         | 9         | 3.1       | 122.6     | ~0.05   |
| 11900     | 0         | 12        | 3.6       | 133.9     | ~0.05   |
| 12000     | 0         | 11        | 3.2       | 137.8     | ~0.05   |
| 12100     | 0         | 10        | 3.1       | 129.1     | ~0.05   |
| 12200     | 0         | 12        | 3.2       | 127.5     | ~0.05   |
| 12300     | 0         | 13        | 3.0       | 119.3     | ~0.05   |
| 12400     | 0         | 13        | 3.1       | 132.4     | ~0.05   |
| 12500     | 0         | 12        | 2.9       | 129.8     | ~0.05   |
| 12600     | 0         | 15        | 3.1       | 136.5     | ~0.05   |
| 12700     | 0         | 10        | 2.8       | 120.7     | ~0.05   |
| 12800     | 0         | 10        | 2.7       | 111.8     | ~0.05   |
| 12900     | 0         | 7         | 2.5       | 115.6     | ~0.05   |
| 13000     | 0         | 11        | 2.5       | 118.3     | ~0.05   |
| 13100     | 0         | 14        | 3.0       | 130.5     | ~0.05   |
| 13200     | 0         | 8         | 2.4       | 104.8     | ~0.05   |
| 13300     | 0         | 12        | 2.7       | 111.8     | ~0.05   |
| 13400     | 0         | 9         | 2.8       | 122.1     | ~0.05   |
| 13500     | 0         | 11        | 3.0       | 114.0     | ~0.05   |
| 13600     | 0         | 12        | 3.1       | 115.0     | ~0.05   |
| 13700     | 0         | 9         | 3.2       | 137.1     | ~0.05   |
| 13800     | 0         | 13        | 3.0       | 116.9     | ~0.05   |
| 13900     | 0         | 10        | 2.8       | 108.9     | ~0.05   |
| 14000     | 0         | 10        | 3.0       | 118.0     | ~0.05   |
| 14100     | 0         | 8         | 2.4       | 110.7     | ~0.05   |
| 14200     | 0         | 14        | 3.0       | 110.9     | ~0.05   |
| 14300     | 0         | 12        | 3.1       | 125.3     | ~0.05   |
| 14400     | 0         | 10        | 3.1       | 130.7     | ~0.05   |
| 14500     | 0         | 14        | 2.7       | 125.4     | ~0.05   |
| 14600     | 0         | 10        | 2.7       | 121.0     | ~0.05   |
| 14700     | 0         | 13        | 2.7       | 106.2     | ~0.05   |
| 14800     | 0         | 11        | 2.7       | 114.1     | ~0.05   |
| 14900     | 0         | 11        | 3.1       | 119.9     | ~0.05   |
| 15000     | 0         | 14        | 3.1       | 115.3     | ~0.05   |
| 15100     | 0         | 12        | 3.0       | 112.6     | ~0.05   |
| 15200     | 0         | 12        | 3.0       | 127.2     | ~0.05   |
| 15300     | 0         | 13        | 2.6       | 109.0     | ~0.05   |
| 15400     | 0         | 10        | 2.8       | 107.4     | ~0.05   |
| 15500     | 0         | 14        | 3.3       | 126.3     | ~0.05   |
| 15600     | 0         | 11        | 3.2       | 125.0     | ~0.05   |
| 15700     | 0         | 13        | 3.1       | 120.9     | ~0.05   |
| 15800     | 0         | 14        | 3.1       | 135.4     | ~0.05   |
| 15900     | 0         | 8         | 2.3       | 115.4     | ~0.05   |
| 16000     | 0         | 11        | 2.7       | 105.4     | ~0.05   |
| 16100     | 0         | 10        | 2.9       | 118.3     | ~0.05   |
| 16200     | 0         | 11        | 3.4       | 126.1     | ~0.05   |
| 16300     | 0         | 11        | 2.8       | 128.0     | ~0.05   |
| 16400     | 0         | 14        | 2.7       | 115.2     | ~0.05   |
| 16500     | 0         | 10        | 2.4       | 111.4     | ~0.05   |
| 16600     | 0         | 9         | 2.8       | 124.7     | ~0.05   |
| 16700     | 0         | 12        | 3.1       | 128.3     | ~0.05   |
| 16800     | 0         | 12        | 2.7       | 110.6     | ~0.05   |
| 16900     | 0         | 10        | 2.4       | 98.2      | ~0.05   |
| 17000     | 0         | 10        | 3.0       | 120.4     | ~0.05   |
| 17100     | 0         | 13        | 2.4       | 114.3     | ~0.05   |
| 17200     | 0         | 14        | 2.6       | 111.7     | ~0.05   |
| 17300     | 0         | 10        | 2.5       | 114.9     | ~0.05   |
| 17400     | 0         | 12        | 2.6       | 120.0     | ~0.05   |
| 17500     | 0         | 10        | 2.6       | 111.3     | ~0.05   |
| 17600     | 0         | 11        | 3.0       | 129.2     | ~0.05   |
| 17700     | 0         | 11        | 2.7       | 113.1     | ~0.05   |
| 17800     | 0         | 11        | 2.4       | 96.7      | ~0.05   |
| 17900     | 0         | 12        | 2.9       | 122.2     | ~0.05   |
| 18000     | 0         | 11        | 2.7       | 109.8     | ~0.05   |
| 18100     | 0         | 14        | 2.8       | 118.0     | ~0.05   |
| 18200     | 0         | 15        | 3.1       | 109.0     | ~0.05   |
| 18300     | 0         | 10        | 2.5       | 103.5     | ~0.05   |
| 18400     | 0         | 13        | 3.5       | 148.1     | ~0.05   |
| 18500     | 0         | 12        | 2.8       | 112.7     | ~0.05   |
| 18600     | 0         | 12        | 2.6       | 122.3     | ~0.05   |
| 18700     | 0         | 9         | 2.5       | 113.5     | ~0.05   |
| 18800     | 0         | 11        | 2.7       | 114.7     | ~0.05   |
| 18900     | 0         | 8         | 2.5       | 109.3     | ~0.05   |
| 19000     | 0         | 10        | 2.7       | 115.9     | ~0.05   |
| 19100     | 0         | 13        | 2.7       | 116.7     | ~0.05   |
| 19200     | 0         | 10        | 2.8       | 122.6     | ~0.05   |
| 19300     | 0         | 14        | 2.9       | 118.9     | ~0.05   |
| 19400     | 0         | 11        | 3.0       | 124.8     | ~0.05   |
| 19500     | 0         | 10        | 2.9       | 122.6     | ~0.05   |
| 19600     | 0         | 16        | 2.9       | 123.1     | ~0.05   |
| 19700     | 0         | 10        | 2.8       | 125.0     | ~0.05   |
| 19800     | 0         | 10        | 2.8       | 125.6     | ~0.05   |
| 19900     | 0         | 11        | 2.5       | 95.7      | ~0.05   |
| 20000     | 0         | 9         | 2.4       | 110.0     | ~0.05   |
| 20100     | 0         | 10        | 2.3       | 103.5     | ~0.05   |
| 20200     | 0         | 15        | 3.3       | 123.1     | ~0.05   |
| 20300     | 0         | 14        | 2.6       | 112.9     | ~0.05   |
| 20400     | 0         | 13        | 3.0       | 128.8     | ~0.05   |
| 20500     | 0         | 10        | 2.5       | 125.6     | ~0.05   |
| 20600     | 0         | 9         | 2.7       | 116.6     | ~0.05   |
| 20700     | 0         | 13        | 2.9       | 120.2     | ~0.05   |
| 20800     | 0         | 11        | 2.9       | 123.9     | ~0.05   |
| 20900     | 0         | 11        | 2.7       | 104.1     | ~0.05   |
| 21000     | 0         | 11        | 3.2       | 117.3     | ~0.05   |
| 21100     | 0         | 13        | 3.2       | 129.4     | ~0.05   |
| 21200     | 0         | 10        | 2.4       | 105.1     | ~0.05   |
| 21300     | 0         | 10        | 2.7       | 109.7     | ~0.05   |
| 21400     | 0         | 10        | 2.6       | 119.5     | ~0.05   |
| 21500     | 0         | 15        | 2.8       | 116.9     | ~0.05   |
| 21600     | 0         | 10        | 2.5       | 120.4     | ~0.05   |
| 21700     | 0         | 12        | 2.6       | 117.4     | ~0.05   |
| 21800     | 0         | 11        | 2.8       | 111.8     | ~0.05   |
| 21900     | 0         | 16        | 3.1       | 126.5     | ~0.05   |
| 22000     | 0         | 12        | 2.1       | 108.3     | ~0.05   |
| 22100     | 0         | 13        | 2.7       | 117.1     | ~0.05   |
| 22200     | 0         | 11        | 3.1       | 129.3     | ~0.05   |
| 22300     | 0         | 12        | 2.9       | 126.3     | ~0.05   |
| 22400     | 0         | 11        | 2.9       | 116.3     | ~0.05   |
| 22500     | 0         | 11        | 2.7       | 118.9     | ~0.05   |
| 22600     | 0         | 12        | 2.9       | 117.6     | ~0.05   |
| 22700     | 0         | 16        | 2.9       | 130.3     | ~0.05   |
| 22800     | 0         | 12        | 3.1       | 112.2     | ~0.05   |
| 22900     | 0         | 12        | 2.8       | 109.4     | ~0.05   |
| 23000     | 0         | 12        | 2.9       | 124.0     | ~0.05   |
| 23100     | 0         | 12        | 3.0       | 124.2     | ~0.05   |
| 23200     | 0         | 9         | 2.6       | 124.6     | ~0.05   |
| 23300     | 0         | 13        | 2.5       | 104.9     | ~0.05   |
| 23400     | 0         | 12        | 2.8       | 105.3     | ~0.05   |
| 23500     | 0         | 10        | 2.8       | 114.4     | ~0.05   |
| 23600     | 0         | 13        | 2.8       | 120.0     | ~0.05   |
| 23700     | 0         | 14        | 2.9       | 123.6     | ~0.05   |
| 23800     | 0         | 10        | 2.7       | 116.2     | ~0.05   |
| 23900     | 0         | 11        | 2.6       | 112.2     | ~0.05   |
| 24000     | 0         | 12        | 2.5       | 104.2     | ~0.05   |
| 24100     | 0         | 11        | 2.5       | 118.4     | ~0.05   |
| 24200     | 0         | 12        | 2.4       | 111.2     | ~0.05   |
| 24300     | 0         | 12        | 2.6       | 119.2     | ~0.05   |
| 24400     | 0         | 11        | 2.4       | 100.9     | ~0.05   |
| 24500     | 0         | 10        | 2.6       | 106.0     | ~0.05   |
| 24600     | 0         | 9         | 2.8       | 127.1     | ~0.05   |
| 24700     | 0         | 10        | 2.6       | 113.1     | ~0.05   |
| 24800     | 0         | 9         | 2.5       | 112.8     | ~0.05   |
| 24900     | 0         | 12        | 2.4       | 111.6     | ~0.05   |
| 25000     | 0         | 8         | 2.6       | 118.1     | ~0.05   |
| 25100     | 0         | 12        | 2.9       | 112.9     | ~0.05   |
| 25200     | 0         | 9         | 2.8       | 131.1     | ~0.05   |
| 25300     | 0         | 12        | 2.9       | 121.1     | ~0.05   |
| 25400     | 0         | 9         | 2.4       | 109.3     | ~0.05   |
| 25500     | 0         | 10        | 2.3       | 113.2     | ~0.05   |
| 25600     | 0         | 9         | 2.6       | 113.2     | ~0.05   |
| 25700     | 0         | 10        | 2.4       | 118.2     | ~0.05   |
| 25800     | 0         | 12        | 2.5       | 108.7     | ~0.05   |
| 25900     | 0         | 12        | 2.9       | 119.1     | ~0.05   |
| 26000     | 0         | 11        | 2.5       | 117.0     | ~0.05   |
| 26100     | 0         | 13        | 2.9       | 141.8     | ~0.05   |
| 26200     | 0         | 14        | 2.8       | 140.8     | ~0.05   |
| 26300     | 0         | 13        | 2.8       | 125.9     | ~0.05   |
| 26400     | 0         | 9         | 2.1       | 101.2     | ~0.05   |
| 26500     | 0         | 10        | 2.3       | 102.2     | ~0.05   |
| 26600     | 0         | 11        | 2.2       | 102.8     | ~0.05   |
| 26700     | 0         | 8         | 2.4       | 119.3     | ~0.05   |
| 26800     | 0         | 9         | 1.7       | 102.4     | ~0.05   |
| 26900     | 0         | 10        | 2.6       | 127.9     | ~0.05   |
| 27000     | 0         | 15        | 2.7       | 122.8     | ~0.05   |
| 27100     | 0         | 11        | 2.5       | 124.2     | ~0.05   |
| 27200     | 0         | 12        | 2.7       | 119.5     | ~0.05   |
| 27300     | 0         | 9         | 2.5       | 123.2     | ~0.05   |
| 27400     | 0         | 11        | 2.9       | 122.9     | ~0.05   |
| 27500     | 0         | 14        | 2.6       | 124.0     | ~0.05   |
| 27600     | 0         | 12        | 2.3       | 109.8     | ~0.05   |
| 27700     | 0         | 11        | 2.4       | 113.1     | ~0.05   |
| 27800     | 0         | 10        | 2.4       | 126.0     | ~0.05   |
| 27900     | 0         | 9         | 2.5       | 120.1     | ~0.05   |
| 28000     | 0         | 10        | 2.3       | 104.8     | ~0.05   |
| 28100     | 0         | 12        | 2.7       | 123.2     | ~0.05   |
| 28200     | 0         | 11        | 2.6       | 116.8     | ~0.05   |
| 28300     | 0         | 8         | 2.2       | 113.5     | ~0.05   |
| 28400     | 0         | 8         | 1.7       | 98.0      | ~0.05   |
| 28500     | 0         | 11        | 2.3       | 110.9     | ~0.05   |
| 28600     | 0         | 11        | 2.1       | 108.2     | ~0.05   |
| 28700     | 0         | 10        | 2.2       | 113.7     | ~0.05   |
| 28800     | 0         | 11        | 2.3       | 125.4     | ~0.05   |
| 28900     | 0         | 11        | 2.5       | 119.3     | ~0.05   |
| 29000     | 0         | 11        | 1.9       | 118.2     | ~0.05   |
| 29100     | 0         | 10        | 1.9       | 109.4     | ~0.05   |
| 29200     | 0         | 9         | 2.3       | 110.3     | ~0.05   |
| 29300     | 0         | 9         | 2.2       | 102.5     | ~0.05   |
| 29400     | 0         | 12        | 2.5       | 125.0     | ~0.05   |
| 29500     | 0         | 12        | 2.5       | 122.7     | ~0.05   |
| 29600     | 0         | 9         | 2.5       | 116.2     | ~0.05   |
| 29700     | 0         | 9         | 2.1       | 109.3     | ~0.05   |
| 29800     | 0         | 11        | 2.7       | 130.5     | ~0.05   |
| 29900     | 0         | 9         | 2.4       | 112.7     | ~0.05   |
| 30000     | 0         | 12        | 2.1       | 106.1     | ~0.05   |
| 30100     | 0         | 8         | 1.9       | 107.9     | ~0.05   |
| 30200     | 0         | 9         | 2.6       | 121.6     | ~0.05   |
| 30300     | 0         | 10        | 2.0       | 107.8     | ~0.05   |
| 30400     | 0         | 10        | 2.8       | 132.6     | ~0.05   |
| 30500     | 0         | 10        | 2.4       | 115.5     | ~0.05   |
| 30600     | 0         | 10        | 2.7       | 118.7     | ~0.05   |
| 30700     | 0         | 8         | 2.3       | 116.8     | ~0.05   |
| 30800     | 0         | 11        | 2.1       | 94.4      | ~0.05   |
| 30900     | 0         | 10        | 2.1       | 104.6     | ~0.05   |
| 31000     | 0         | 11        | 2.3       | 112.6     | ~0.05   |
| 31100     | 0         | 7         | 1.9       | 100.5     | ~0.05   |
| 31200     | 0         | 11        | 2.7       | 122.6     | ~0.05   |
| 31300     | 0         | 12        | 2.6       | 123.8     | ~0.05   |
| 31400     | 0         | 11        | 2.4       | 102.2     | ~0.05   |
| 31500     | 0         | 10        | 2.6       | 114.7     | ~0.05   |
| 31600     | 0         | 11        | 3.3       | 147.6     | ~0.05   |
| 31700     | 0         | 12        | 2.5       | 106.4     | ~0.05   |
| 31800     | 0         | 13        | 3.3       | 130.7     | ~0.05   |
| 31900     | 0         | 13        | 2.8       | 119.5     | ~0.05   |
| 32000     | 0         | 9         | 2.5       | 115.8     | ~0.05   |
| 32100     | 0         | 11        | 2.6       | 122.8     | ~0.05   |
| 32200     | 0         | 12        | 2.1       | 92.4      | ~0.05   |
| 32300     | 0         | 11        | 2.7       | 116.8     | ~0.05   |
| 32400     | 0         | 14        | 3.2       | 136.6     | ~0.05   |
| 32500     | 0         | 10        | 2.6       | 131.2     | ~0.05   |
| 32600     | 0         | 13        | 2.5       | 119.3     | ~0.05   |
| 32700     | 0         | 9         | 2.3       | 114.8     | ~0.05   |
| 32800     | 0         | 13        | 2.3       | 110.6     | ~0.05   |
| 32900     | 0         | 13        | 2.0       | 99.5      | ~0.05   |
| 33000     | 0         | 13        | 2.1       | 106.7     | ~0.05   |
| 33100     | 0         | 8         | 2.1       | 113.6     | ~0.05   |
| 33200     | 0         | 14        | 2.3       | 106.7     | ~0.05   |
| 33300     | 0         | 12        | 2.7       | 126.7     | ~0.05   |
| 33400     | 0         | 8         | 2.4       | 117.8     | ~0.05   |
| 33500     | 0         | 12        | 2.4       | 121.8     | ~0.05   |
| 33600     | 0         | 8         | 2.4       | 118.5     | ~0.05   |
| 33700     | 0         | 10        | 2.5       | 117.3     | ~0.05   |
| 33800     | 0         | 10        | 2.4       | 111.0     | ~0.05   |
| 33900     | 0         | 12        | 2.7       | 113.3     | ~0.05   |
| 34000     | 0         | 9         | 2.4       | 120.7     | ~0.05   |
| 34100     | 0         | 14        | 2.3       | 107.1     | ~0.05   |
| 34200     | 0         | 15        | 2.3       | 106.2     | ~0.05   |
| 34300     | 0         | 12        | 2.4       | 118.6     | ~0.05   |
| 34400     | 0         | 12        | 2.7       | 119.7     | ~0.05   |
| 34500     | 0         | 10        | 2.2       | 110.1     | ~0.05   |
| 34600     | 0         | 11        | 2.4       | 113.7     | ~0.05   |
| 34700     | 0         | 16        | 2.2       | 107.8     | ~0.05   |
| 34800     | 0         | 11        | 2.5       | 106.9     | ~0.05   |
| 34900     | 0         | 9         | 2.6       | 114.8     | ~0.05   |
| 35000     | 0         | 11        | 2.7       | 106.0     | ~0.05   |
| 35100     | 0         | 12        | 3.4       | 141.7     | ~0.05   |
| 35200     | 0         | 15        | 3.4       | 127.2     | ~0.05   |
| 35300     | 0         | 11        | 2.5       | 111.0     | ~0.05   |
| 35400     | 0         | 10        | 2.3       | 107.3     | ~0.05   |
| 35500     | 0         | 14        | 2.7       | 113.5     | ~0.05   |
| 35600     | 0         | 10        | 2.5       | 104.4     | ~0.05   |
| 35700     | 0         | 12        | 2.5       | 119.7     | ~0.05   |
| 35800     | 0         | 9         | 2.4       | 110.7     | ~0.05   |
| 35900     | 0         | 14        | 2.4       | 118.5     | ~0.05   |
| 36000     | 0         | 10        | 2.5       | 104.6     | ~0.05   |
| 36100     | 0         | 10        | 2.4       | 98.6      | ~0.05   |
| 36200     | 0         | 12        | 2.7       | 120.5     | ~0.05   |
| 36300     | 0         | 10        | 2.3       | 102.8     | ~0.05   |
| 36400     | 0         | 9         | 2.3       | 101.2     | ~0.05   |
| 36500     | 0         | 11        | 2.1       | 113.0     | ~0.05   |
| 36600     | 0         | 17        | 2.6       | 115.0     | ~0.05   |
| 36700     | 0         | 11        | 2.1       | 98.5      | ~0.05   |
| 36800     | 0         | 10        | 2.4       | 113.2     | ~0.05   |
| 36900     | 0         | 10        | 2.3       | 111.8     | ~0.05   |
| 37000     | 0         | 11        | 1.9       | 109.5     | ~0.05   |
| 37100     | 0         | 9         | 2.3       | 112.4     | ~0.05   |
| 37200     | 0         | 10        | 2.5       | 112.0     | ~0.05   |
| 37300     | 0         | 10        | 2.4       | 115.7     | ~0.05   |
| 37400     | 0         | 11        | 2.5       | 110.5     | ~0.05   |
| 37500     | 0         | 12        | 2.7       | 131.1     | ~0.05   |
| 37600     | 0         | 9         | 2.6       | 117.4     | ~0.05   |
| 37700     | 0         | 11        | 2.5       | 115.6     | ~0.05   |
| 37800     | 0         | 8         | 2.0       | 105.4     | ~0.05   |
| 37900     | 0         | 12        | 2.4       | 114.3     | ~0.05   |
| 38000     | 0         | 9         | 1.9       | 88.1      | ~0.05   |
| 38100     | 0         | 10        | 2.1       | 102.8     | ~0.05   |
| 38200     | 0         | 8         | 2.4       | 113.3     | ~0.05   |
| 38300     | 0         | 9         | 2.5       | 113.1     | ~0.05   |
| 38400     | 0         | 9         | 2.5       | 116.0     | ~0.05   |
| 38500     | 0         | 13        | 3.0       | 131.2     | ~0.05   |
| 38600     | 0         | 11        | 2.8       | 116.0     | ~0.05   |
| 38700     | 0         | 12        | 2.7       | 122.5     | ~0.05   |
| 38800     | 0         | 13        | 2.5       | 112.5     | ~0.05   |
| 38900     | 0         | 13        | 2.4       | 116.8     | ~0.05   |
| 39000     | 0         | 9         | 2.5       | 110.9     | ~0.05   |
| 39100     | 0         | 7         | 2.4       | 106.5     | ~0.05   |
| 39200     | 0         | 10        | 2.5       | 116.1     | ~0.05   |
| 39300     | 0         | 8         | 2.0       | 98.3      | ~0.05   |
| 39400     | 0         | 9         | 2.5       | 120.0     | ~0.05   |
| 39500     | 0         | 7         | 2.0       | 98.4      | ~0.05   |
| 39600     | 0         | 9         | 1.9       | 103.0     | ~0.05   |
| 39700     | 0         | 8         | 2.2       | 102.7     | ~0.05   |
| 39800     | 0         | 10        | 2.7       | 112.6     | ~0.05   |
| 39900     | 0         | 12        | 2.5       | 109.9     | ~0.05   |
| 40000     | 0         | 8         | 2.1       | 99.3      | ~0.05   |
| 40100     | 0         | 9         | 2.2       | 114.0     | ~0.05   |
| 40200     | 0         | 8         | 2.0       | 101.0     | ~0.05   |
| 40300     | 0         | 9         | 2.0       | 111.1     | ~0.05   |
| 40400     | 0         | 9         | 2.4       | 120.7     | ~0.05   |
| 40500     | 0         | 8         | 2.2       | 118.0     | ~0.05   |
| 40600     | 0         | 9         | 2.4       | 105.2     | ~0.05   |
| 40700     | 0         | 9         | 2.4       | 108.8     | ~0.05   |
| 40800     | 0         | 10        | 2.4       | 112.6     | ~0.05   |
| 40900     | 0         | 9         | 1.9       | 96.6      | ~0.05   |
| 41000     | 0         | 10        | 2.4       | 107.0     | ~0.05   |
| 41100     | 0         | 12        | 2.4       | 111.4     | ~0.05   |
| 41200     | 0         | 13        | 2.9       | 119.2     | ~0.05   |
| 41300     | 0         | 12        | 2.5       | 113.7     | ~0.05   |
| 41400     | 0         | 15        | 2.6       | 125.9     | ~0.05   |
| 41500     | 0         | 13        | 2.4       | 115.8     | ~0.05   |
| 41600     | 0         | 9         | 2.3       | 116.3     | ~0.05   |
| 41700     | 0         | 9         | 2.1       | 106.8     | ~0.05   |
| 41800     | 0         | 14        | 2.7       | 130.2     | ~0.05   |
| 41900     | 0         | 9         | 2.5       | 115.5     | ~0.05   |
| 42000     | 0         | 11        | 2.5       | 116.5     | ~0.05   |
| 42100     | 0         | 11        | 2.5       | 126.2     | ~0.05   |
| 42200     | 0         | 21        | 3.1       | 132.8     | ~0.05   |
| 42300     | 0         | 11        | 2.3       | 110.7     | ~0.05   |
| 42400     | 0         | 11        | 2.6       | 112.4     | ~0.05   |
| 42500     | 0         | 11        | 2.4       | 113.2     | ~0.05   |
| 42600     | 0         | 10        | 2.2       | 108.1     | ~0.05   |
| 42700     | 0         | 10        | 2.2       | 106.7     | ~0.05   |
| 42800     | 0         | 11        | 2.4       | 114.8     | ~0.05   |
| 42900     | 0         | 9         | 2.1       | 106.7     | ~0.05   |
| 43000     | 0         | 11        | 2.6       | 111.4     | ~0.05   |
| 43100     | 0         | 10        | 2.4       | 115.0     | ~0.05   |
| 43200     | 0         | 11        | 2.4       | 113.0     | ~0.05   |
| 43300     | 0         | 11        | 2.3       | 112.7     | ~0.05   |
| 43400     | 0         | 14        | 2.1       | 109.4     | ~0.05   |
| 43500     | 0         | 9         | 2.2       | 108.2     | ~0.05   |
| 43600     | 0         | 13        | 2.5       | 118.8     | ~0.05   |
| 43700     | 0         | 18        | 2.6       | 119.6     | ~0.05   |
| 43800     | 0         | 12        | 2.3       | 108.6     | ~0.05   |
| 43900     | 0         | 7         | 2.1       | 105.8     | ~0.05   |
| 44000     | 0         | 16        | 2.4       | 106.5     | ~0.05   |
| 44100     | 0         | 12        | 2.4       | 115.1     | ~0.05   |
| 44200     | 0         | 9         | 1.9       | 105.4     | ~0.05   |
| 44300     | 0         | 10        | 2.5       | 116.2     | ~0.05   |
| 44400     | 0         | 11        | 2.4       | 125.7     | ~0.05   |
| 44500     | 0         | 10        | 2.3       | 114.3     | ~0.05   |
| 44600     | 0         | 12        | 2.4       | 114.6     | ~0.05   |
| 44700     | 0         | 9         | 2.4       | 108.4     | ~0.05   |
| 44800     | 0         | 10        | 1.7       | 87.5      | ~0.05   |
| 44900     | 0         | 8         | 2.4       | 115.8     | ~0.05   |
| 45000     | 0         | 11        | 2.5       | 128.6     | ~0.05   |
| 45100     | 0         | 12        | 2.7       | 113.5     | ~0.05   |
| 45200     | 0         | 10        | 1.9       | 108.2     | ~0.05   |
| 45300     | 0         | 14        | 2.2       | 102.0     | ~0.05   |
| 45400     | 0         | 11        | 2.3       | 95.0      | ~0.05   |
| 45500     | 0         | 12        | 2.7       | 118.1     | ~0.05   |
| 45600     | 0         | 10        | 2.5       | 114.6     | ~0.05   |
| 45700     | 0         | 12        | 2.7       | 122.1     | ~0.05   |
| 45800     | 0         | 10        | 2.4       | 107.5     | ~0.05   |
| 45900     | 0         | 15        | 2.4       | 103.4     | ~0.05   |
| 46000     | 0         | 11        | 2.4       | 107.6     | ~0.05   |
| 46100     | 0         | 11        | 2.8       | 114.7     | ~0.05   |
| 46200     | 0         | 10        | 2.1       | 102.7     | ~0.05   |
| 46300     | 0         | 9         | 2.3       | 107.9     | ~0.05   |
| 46400     | 0         | 11        | 2.5       | 116.3     | ~0.05   |
| 46500     | 0         | 10        | 2.5       | 111.2     | ~0.05   |
| 46600     | 0         | 8         | 2.3       | 103.6     | ~0.05   |
| 46700     | 0         | 8         | 2.3       | 110.6     | ~0.05   |
| 46800     | 0         | 10        | 1.9       | 106.6     | ~0.05   |
| 46900     | 0         | 9         | 2.0       | 105.3     | ~0.05   |
| 47000     | 0         | 10        | 2.3       | 113.8     | ~0.05   |
| 47100     | 0         | 11        | 2.2       | 118.4     | ~0.05   |
| 47200     | 0         | 10        | 2.1       | 105.5     | ~0.05   |
| 47300     | 0         | 12        | 1.8       | 109.2     | ~0.05   |
| 47400     | 0         | 8         | 2.2       | 115.3     | ~0.05   |
| 47500     | 0         | 13        | 2.1       | 105.1     | ~0.05   |
| 47600     | 0         | 9         | 2.0       | 104.1     | ~0.05   |
| 47700     | 0         | 10        | 2.5       | 108.7     | ~0.05   |
| 47800     | 0         | 9         | 2.1       | 102.7     | ~0.05   |
| 47900     | 0         | 11        | 2.4       | 114.9     | ~0.05   |
| 48000     | 0         | 9         | 2.5       | 116.3     | ~0.05   |
| 48100     | 0         | 12        | 2.5       | 122.3     | ~0.05   |
| 48200     | 0         | 9         | 2.0       | 100.4     | ~0.05   |
| 48300     | 0         | 10        | 2.2       | 108.6     | ~0.05   |
| 48400     | 0         | 12        | 2.5       | 117.5     | ~0.05   |
| 48500     | 0         | 9         | 2.2       | 104.1     | ~0.05   |
| 48600     | 0         | 10        | 2.5       | 109.1     | ~0.05   |
| 48700     | 0         | 12        | 2.9       | 115.1     | ~0.05   |
| 48800     | 0         | 10        | 2.5       | 118.5     | ~0.05   |
| 48900     | 0         | 10        | 2.0       | 99.7      | ~0.05   |
| 49000     | 0         | 9         | 2.9       | 118.0     | ~0.05   |
| 49100     | 0         | 9         | 2.3       | 103.1     | ~0.05   |
| 49200     | 0         | 12        | 2.5       | 107.4     | ~0.05   |
| 49300     | 0         | 8         | 2.4       | 101.9     | ~0.05   |
| 49400     | 0         | 14        | 2.5       | 115.5     | ~0.05   |
| 49500     | 0         | 11        | 2.6       | 110.0     | ~0.05   |
| 49600     | 0         | 10        | 2.8       | 111.6     | ~0.05   |
| 49700     | 0         | 12        | 2.8       | 122.0     | ~0.05   |
| 49800     | 0         | 9         | 2.5       | 116.8     | ~0.05   |
| 49900     | 0         | 13        | 2.1       | 104.6     | ~0.05   |
| 50000     | 0         | 10        | 2.9       | 107.5     | ~0.05   |

**Observations**
    We can observe various things here: a new score max of 17 was reached at episodes 10600 and 36600, and a new score avg peak of 3.8 at episode 11100 (also 3.6 at episodes 10700, 10900, 11300, and 11900). This indicates that we clearly had not reached the plateau in early experiments and the model could keep growing. However, score avg oscillates between 2 and 3 after episode 16000.

**Choice for next experiment**
    I would take this model and set the gamma to 0.80 because the model has already learned a lot and it could be exploited even more by giving more importance to future rewards, and train it until episode 60,000.

---

### Experiment 22 — 2026-06-06
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.80
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 60,000 (loaded model from exp_21, continued from episode 50,000)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 50100     | 0         | 11        | 3.1       | 117.3     | ~0.05   |
| 50200     | 0         | 12        | 3.2       | 116.6     | ~0.05   |
| 50300     | 0         | 13        | 3.2       | 120.6     | ~0.05   |
| 50400     | 0         | 13        | 3.1       | 109.6     | ~0.05   |
| 50500     | 0         | 13        | 3.2       | 117.6     | ~0.05   |
| 50600     | 0         | 10        | 3.1       | 108.3     | ~0.05   |
| 50700     | 0         | 14        | 3.3       | 115.6     | ~0.05   |
| 50800     | 0         | 12        | 3.4       | 116.1     | ~0.05   |
| 50900     | 0         | 14        | 3.7       | 121.0     | ~0.05   |
| 51000     | 0         | 14        | 4.0       | 126.4     | ~0.05   |
| 51100     | 0         | 15        | 3.2       | 101.9     | ~0.05   |
| 51200     | 0         | 15        | 3.3       | 103.4     | ~0.05   |
| 51300     | 0         | 18        | 3.7       | 111.0     | ~0.05   |
| 51400     | 0         | 19        | 3.6       | 110.3     | ~0.05   |
| 51500     | 0         | 21        | 4.7       | 150.3     | ~0.05   |
| 51600     | 0         | 16        | 3.8       | 118.5     | ~0.05   |
| 51700     | 0         | 14        | 3.5       | 111.7     | ~0.05   |
| 51800     | 0         | 19        | 3.9       | 112.2     | ~0.05   |
| 51900     | 0         | 18        | 4.0       | 130.4     | ~0.05   |
| 52000     | 0         | 14        | 4.5       | 126.3     | ~0.05   |
| 52100     | 0         | 12        | 3.5       | 104.0     | ~0.05   |
| 52200     | 0         | 23        | 3.9       | 121.4     | ~0.05   |
| 52300     | 0         | 18        | 4.0       | 117.0     | ~0.05   |
| 52400     | 0         | 14        | 4.3       | 124.2     | ~0.05   |
| 52500     | 0         | 16        | 3.6       | 113.5     | ~0.05   |
| 52600     | 0         | 18        | 4.1       | 125.4     | ~0.05   |
| 52700     | 0         | 17        | 4.3       | 124.3     | ~0.05   |
| 52800     | 0         | 15        | 4.7       | 126.8     | ~0.05   |
| 52900     | 0         | 14        | 4.3       | 121.3     | ~0.05   |
| 53000     | 0         | 15        | 4.2       | 119.8     | ~0.05   |
| 53100     | 0         | 13        | 3.6       | 106.1     | ~0.05   |
| 53200     | 0         | 16        | 4.1       | 110.4     | ~0.05   |
| 53300     | 0         | 17        | 4.5       | 119.8     | ~0.05   |
| 53400     | 0         | 15        | 4.0       | 118.2     | ~0.05   |
| 53500     | 0         | 13        | 4.0       | 110.2     | ~0.05   |
| 53600     | 0         | 14        | 4.0       | 115.1     | ~0.05   |
| 53700     | 0         | 15        | 3.9       | 107.0     | ~0.05   |
| 53800     | 0         | 22        | 4.4       | 115.5     | ~0.05   |
| 53900     | 0         | 23        | 5.0       | 131.9     | ~0.05   |
| 54000     | 0         | 16        | 4.7       | 135.3     | ~0.05   |
| 54100     | 0         | 13        | 3.6       | 105.2     | ~0.05   |
| 54200     | 0         | 16        | 3.8       | 109.6     | ~0.05   |
| 54300     | 0         | 22        | 4.3       | 116.9     | ~0.05   |
| 54400     | 0         | 15        | 4.1       | 105.6     | ~0.05   |
| 54500     | 0         | 20        | 4.5       | 123.7     | ~0.05   |
| 54600     | 0         | 14        | 4.2       | 115.8     | ~0.05   |
| 54700     | 0         | 14        | 4.5       | 112.8     | ~0.05   |
| 54800     | 0         | 14        | 5.0       | 139.6     | ~0.05   |
| 54900     | 0         | 14        | 3.9       | 102.8     | ~0.05   |
| 55000     | 0         | 20        | 4.8       | 141.9     | ~0.05   |
| 55100     | 0         | 17        | 4.4       | 113.1     | ~0.05   |
| 55200     | 0         | 17        | 4.5       | 117.8     | ~0.05   |
| 55300     | 0         | 14        | 3.2       | 91.6      | ~0.05   |
| 55400     | 0         | 16        | 3.8       | 117.0     | ~0.05   |
| 55500     | 0         | 12        | 4.7       | 121.3     | ~0.05   |
| 55600     | 0         | 15        | 4.2       | 120.0     | ~0.05   |
| 55700     | 0         | 19        | 4.3       | 112.7     | ~0.05   |
| 55800     | 0         | 18        | 4.6       | 129.8     | ~0.05   |
| 55900     | 0         | 11        | 3.5       | 97.5      | ~0.05   |
| 56000     | 0         | 15        | 4.8       | 134.7     | ~0.05   |
| 56100     | 0         | 21        | 4.5       | 113.1     | ~0.05   |
| 56200     | 0         | 21        | 5.1       | 123.1     | ~0.05   |
| 56300     | 0         | 14        | 4.5       | 115.5     | ~0.05   |
| 56400     | 0         | 22        | 4.2       | 110.7     | ~0.05   |
| 56500     | 0         | 17        | 4.2       | 117.0     | ~0.05   |
| 56600     | 0         | 20        | 4.8       | 118.3     | ~0.05   |
| 56700     | 0         | 18        | 4.4       | 121.3     | ~0.05   |
| 56800     | 0         | 20        | 4.7       | 129.7     | ~0.05   |
| 56900     | 0         | 15        | 4.7       | 120.9     | ~0.05   |
| 57000     | 0         | 15        | 4.9       | 128.0     | ~0.05   |
| 57100     | 0         | 16        | 4.8       | 131.5     | ~0.05   |
| 57200     | 0         | 20        | 4.6       | 124.7     | ~0.05   |
| 57300     | 0         | 18        | 5.3       | 131.2     | ~0.05   |
| 57400     | 0         | 16        | 5.0       | 124.8     | ~0.05   |
| 57500     | 0         | 15        | 4.4       | 110.6     | ~0.05   |
| 57600     | 0         | 15        | 4.8       | 120.1     | ~0.05   |
| 57700     | 0         | 18        | 4.1       | 109.9     | ~0.05   |
| 57800     | 0         | 16        | 4.9       | 131.7     | ~0.05   |
| 57900     | 0         | 18        | 5.0       | 130.1     | ~0.05   |
| 58000     | 0         | 21        | 5.3       | 136.2     | ~0.05   |
| 58100     | 0         | 22        | 4.1       | 101.1     | ~0.05   |
| 58200     | 0         | 20        | 4.5       | 111.4     | ~0.05   |
| 58300     | 0         | 18        | 4.8       | 132.3     | ~0.05   |
| 58400     | 0         | 13        | 4.6       | 110.9     | ~0.05   |
| 58500     | 0         | 12        | 3.9       | 90.5      | ~0.05   |
| 58600     | 0         | 13        | 4.2       | 105.6     | ~0.05   |
| 58700     | 0         | 17        | 5.4       | 132.7     | ~0.05   |
| 58800     | 0         | 20        | 6.2       | 151.3     | ~0.05   |
| 58900     | 0         | 15        | 5.3       | 124.8     | ~0.05   |
| 59000     | 0         | 14        | 4.1       | 106.1     | ~0.05   |
| 59100     | 0         | 16        | 5.8       | 143.6     | ~0.05   |
| 59200     | 0         | 18        | 5.4       | 137.4     | ~0.05   |
| 59300     | 0         | 18        | 5.0       | 121.2     | ~0.05   |
| 59400     | 0         | 26        | 5.2       | 129.4     | ~0.05   |
| 59500     | 0         | 17        | 4.3       | 104.3     | ~0.05   |
| 59600     | 0         | 15        | 5.0       | 117.3     | ~0.05   |
| 59700     | 0         | 19        | 5.2       | 124.7     | ~0.05   |
| 59800     | 0         | 20        | 4.7       | 126.0     | ~0.05   |
| 59900     | 0         | 16        | 4.8       | 116.0     | ~0.05   |
| 60000     | 0         | 17        | 5.0       | 121.2     | ~0.05   |

**Observations**
    We can observe a clear improvement compared to the previous experiment. The model reached new maximum values: 26 for score max in episode 59400, and 5.8 for score avg in episode 59100. It clearly has more to learn. Changing the gamma to a higher value has improved the learning significantly.

**Choice for next experiment**
    I would set the gamma even higher to 0.9 in order to see how it handles it and train it until episode 70,000.

---

### Experiment 23 — 2026-06-06
**Hyperparameters**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.99995
- gamma: 0.90
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100
- episodes: 70,000 (loaded model from exp_22, continued from episode 60,000)
- step limit: step_max = 100 + 50 * score (dynamic)
- reward: +10 if eaten, -25 if die, +0.1 if closer to food than ever in episode, -0.1 otherwise
- model input: CNN (3 channels) + direction one-hot (4,) concatenated at FC layer

**Results** (every 100 episodes)
| Episodes  | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 60100     | 0         | 17        | 5.0       | 129.8     | ~0.05   |
| 60200     | 0         | 16        | 4.4       | 101.4     | ~0.05   |
| 60300     | 0         | 16        | 4.7       | 110.6     | ~0.05   |
| 60400     | 0         | 16        | 5.3       | 112.5     | ~0.05   |
| 60500     | 0         | 22        | 6.5       | 141.7     | ~0.05   |
| 60600     | 0         | 17        | 5.4       | 117.6     | ~0.05   |
| 60700     | 0         | 18        | 5.8       | 119.3     | ~0.05   |
| 60800     | 0         | 19        | 5.4       | 102.8     | ~0.05   |
| 60900     | 0         | 22        | 6.7       | 125.2     | ~0.05   |
| 61000     | 0         | 27        | 6.8       | 129.6     | ~0.05   |
| 61100     | 0         | 24        | 6.3       | 120.9     | ~0.05   |
| 61200     | 0         | 25        | 6.8       | 129.2     | ~0.05   |
| 61300     | 0         | 21        | 6.8       | 121.2     | ~0.05   |
| 61400     | 0         | 19        | 5.7       | 112.2     | ~0.05   |
| 61500     | 0         | 18        | 6.3       | 116.4     | ~0.05   |
| 61600     | 0         | 21        | 6.4       | 113.4     | ~0.05   |
| 61700     | 0         | 19        | 6.9       | 123.5     | ~0.05   |
| 61800     | 0         | 25        | 7.3       | 130.0     | ~0.05   |
| 61900     | 1         | 23        | 6.9       | 127.6     | ~0.05   |
| 62000     | 0         | 19        | 6.5       | 120.5     | ~0.05   |
| 62100     | 0         | 19        | 6.9       | 120.7     | ~0.05   |
| 62200     | 1         | 19        | 7.2       | 123.9     | ~0.05   |
| 62300     | 1         | 25        | 7.5       | 134.5     | ~0.05   |
| 62400     | 0         | 18        | 6.4       | 109.8     | ~0.05   |
| 62500     | 0         | 25        | 8.3       | 145.4     | ~0.05   |
| 62600     | 0         | 20        | 7.3       | 132.1     | ~0.05   |
| 62700     | 0         | 28        | 8.3       | 140.4     | ~0.05   |
| 62800     | 0         | 26        | 8.0       | 138.3     | ~0.05   |
| 62900     | 0         | 24        | 9.0       | 151.1     | ~0.05   |
| 63000     | 0         | 21        | 7.3       | 118.5     | ~0.05   |
| 63100     | 0         | 28        | 7.9       | 132.9     | ~0.05   |
| 63200     | 0         | 21        | 7.7       | 131.3     | ~0.05   |
| 63300     | 0         | 29        | 8.3       | 140.7     | ~0.05   |
| 63400     | 0         | 24        | 7.9       | 124.4     | ~0.05   |
| 63500     | 0         | 26        | 7.8       | 120.7     | ~0.05   |
| 63600     | 0         | 26        | 8.0       | 126.0     | ~0.05   |
| 63700     | 0         | 20        | 7.4       | 119.4     | ~0.05   |
| 63800     | 0         | 24        | 8.6       | 140.6     | ~0.05   |
| 63900     | 0         | 26        | 8.0       | 130.3     | ~0.05   |
| 64000     | 0         | 22        | 7.9       | 127.3     | ~0.05   |
| 64100     | 0         | 25        | 8.5       | 129.7     | ~0.05   |
| 64200     | 0         | 26        | 9.1       | 145.3     | ~0.05   |
| 64300     | 1         | 22        | 8.9       | 137.6     | ~0.05   |
| 64400     | 0         | 23        | 8.3       | 122.8     | ~0.05   |
| 64500     | 0         | 23        | 7.7       | 120.1     | ~0.05   |
| 64600     | 0         | 23        | 8.1       | 124.7     | ~0.05   |
| 64700     | 0         | 23        | 7.6       | 116.0     | ~0.05   |
| 64800     | 1         | 23        | 8.4       | 135.4     | ~0.05   |
| 64900     | 0         | 34        | 8.9       | 138.4     | ~0.05   |
| 65000     | 0         | 27        | 9.1       | 134.6     | ~0.05   |
| 65100     | 0         | 26        | 9.2       | 145.1     | ~0.05   |
| 65200     | 0         | 25        | 9.3       | 146.4     | ~0.05   |
| 65300     | 1         | 25        | 8.5       | 128.1     | ~0.05   |
| 65400     | 1         | 30        | 8.7       | 128.8     | ~0.05   |
| 65500     | 0         | 20        | 8.5       | 131.8     | ~0.05   |
| 65600     | 0         | 25        | 9.9       | 149.3     | ~0.05   |
| 65700     | 0         | 28        | 9.2       | 148.5     | ~0.05   |
| 65800     | 0         | 24        | 9.6       | 152.1     | ~0.05   |
| 65900     | 1         | 24        | 9.2       | 138.7     | ~0.05   |
| 66000     | 0         | 29        | 8.0       | 118.9     | ~0.05   |
| 66100     | 0         | 26        | 8.8       | 133.4     | ~0.05   |
| 66200     | 0         | 26        | 10.0      | 144.1     | ~0.05   |
| 66300     | 0         | 28        | 9.4       | 142.2     | ~0.05   |
| 66400     | 0         | 24        | 8.9       | 130.8     | ~0.05   |
| 66500     | 0         | 31        | 10.4      | 157.5     | ~0.05   |
| 66600     | 1         | 31        | 9.4       | 138.7     | ~0.05   |
| 66700     | 1         | 30        | 10.0      | 141.7     | ~0.05   |
| 66800     | 1         | 28        | 9.6       | 139.5     | ~0.05   |
| 66900     | 0         | 26        | 10.0      | 147.3     | ~0.05   |
| 67000     | 0         | 26        | 11.2      | 168.0     | ~0.05   |
| 67100     | 1         | 25        | 9.8       | 145.6     | ~0.05   |
| 67200     | 1         | 27        | 8.8       | 133.9     | ~0.05   |
| 67300     | 0         | 33        | 10.3      | 153.3     | ~0.05   |
| 67400     | 0         | 27        | 8.8       | 129.3     | ~0.05   |
| 67500     | 0         | 26        | 9.3       | 134.1     | ~0.05   |
| 67600     | 1         | 26        | 10.0      | 155.6     | ~0.05   |
| 67700     | 1         | 24        | 9.3       | 139.4     | ~0.05   |
| 67800     | 1         | 27        | 9.7       | 140.9     | ~0.05   |
| 67900     | 1         | 26        | 10.8      | 162.7     | ~0.05   |
| 68000     | 1         | 27        | 11.0      | 161.3     | ~0.05   |
| 68100     | 0         | 26        | 10.4      | 150.9     | ~0.05   |
| 68200     | 1         | 33        | 10.8      | 155.2     | ~0.05   |
| 68300     | 0         | 25        | 9.2       | 135.8     | ~0.05   |
| 68400     | 0         | 24        | 10.5      | 154.2     | ~0.05   |
| 68500     | 0         | 28        | 9.7       | 151.3     | ~0.05   |
| 68600     | 1         | 35        | 9.9       | 145.4     | ~0.05   |
| 68700     | 0         | 24        | 9.7       | 142.0     | ~0.05   |
| 68800     | 1         | 31        | 10.8      | 160.1     | ~0.05   |
| 68900     | 1         | 29        | 10.0      | 148.3     | ~0.05   |
| 69000     | 1         | 27        | 10.3      | 150.0     | ~0.05   |
| 69100     | 1         | 30        | 8.8       | 126.7     | ~0.05   |
| 69200     | 0         | 29        | 11.2      | 159.9     | ~0.05   |
| 69300     | 0         | 28        | 9.8       | 144.3     | ~0.05   |
| 69400     | 1         | 35        | 10.1      | 142.4     | ~0.05   |
| 69500     | 1         | 23        | 9.2       | 137.2     | ~0.05   |
| 69600     | 0         | 31        | 12.0      | 177.2     | ~0.05   |
| 69700     | 1         | 31        | 11.0      | 157.1     | ~0.05   |
| 69800     | 0         | 28        | 11.1      | 165.6     | ~0.05   |
| 69900     | 0         | 32        | 10.0      | 149.7     | ~0.05   |
| 70000     | 0         | 29        | 10.8      | 154.0     | ~0.05   |

**Observations**
    New record values were reached: 35 for score max in episodes 68600 and 69400, and 12.0 for score avg in episode 69600. The higher gamma continued to improve the model significantly.

**Choice for next experiment**
    Continue training this model until episode 100,000 in sessions of 10,000 episodes.