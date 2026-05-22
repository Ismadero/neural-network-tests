# Experiments Log

## Template
```
### Experimento N — YYYY-MM-DD
**Hiperparámetros**
- epsilon_start / epsilon_end / epsilon_decay:
- gamma:
- lr:
- batch_size:
- buffer_capacity:
- target_update_freq:

**Resultados** (cada 100 episodios)
| Episodios | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
| 100       |           |           |           |           |         |
| ...       |           |           |           |           |         |

**Observaciones**

**Decisión para el siguiente experimento**
```

---

## Experimento 1 — 2026-05-21
**Hiperparámetros**
- epsilon_start: 1.0 / epsilon_end: 0.05 / epsilon_decay: 0.9999
- gamma: 0.99
- lr: 1e-3
- batch_size: 64
- buffer_capacity: 10,000
- target_update_freq: 100

**Resultados**
| Episodios | Score min | Score max | Score avg | Steps avg | Epsilon |
|-----------|-----------|-----------|-----------|-----------|---------|
|           |           |           |           |           |         |

**Observaciones**

**Decisión para el siguiente experimento**
