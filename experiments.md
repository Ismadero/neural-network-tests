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
    The changes are gonna be applied with the next values: +0.2 / -0.5

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
    In this case the model behaves rarely and it seems that it wants to be away from the food instead to get closer.

**Choice for next experiment**
    It was a logic bug where i put the reward shaping inverted, in the next step im going to fix this and see new results. :)

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
    In this case the growth of score avg is notorious but when evaulated we can see that the snake loops in circles most of the time, that explains the high steps avg.

**Choice for next experiment**
    We will set an step limit per episode according to the next formule: step_max = 100 + 50 * score.

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
    We can see a better growing in score_avg, with better results in score max. When evaluated the snake behaves less irregularly moving straighter.

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
    Lower the eating reward till 10 again, but we punish more the dying reward till -25, so the relation between eat:die is 1:2.5.

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
    I would like to try this with a higher gamma, so the model considers farther foods. I'm going to change it to 0.9. Exp_12.
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
    In this case we can appreciate a worse performance compared to the previous exp, both in survival time as well as in score avg. This happens because the model is not correct in its calibration yet, for a higher gamma it needs a training that has good results before apply the higher values, that's why we should set a dynamic gamma that grows as the model learns and get bigger snake sizes.  

**Choice for next experiment**
    First I will try with lower gamma values i.e. 0.4.