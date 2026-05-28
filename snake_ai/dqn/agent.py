import random
import copy
from collections import deque

import torch
import torch.nn as nn

from model import SnakeCNN


class ReplayBuffer:
    """Stores and samples (s, a, r, s', done) experience tuples."""

    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, direction, reward, next_state, next_direction, done):
        self.buffer.append((state, action, direction, reward, next_state, next_direction, done))

    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        states, actions, direction, rewards, next_states, next_direction, dones = zip(*batch)
        return (
            torch.stack(states),
            torch.tensor(actions),
            torch.stack(direction),
            torch.tensor(rewards, dtype=torch.float32),
            torch.stack(next_states),
            torch.stack(next_direction),
            torch.tensor(dones, dtype=torch.float32),
        )

    def __len__(self):
        return len(self.buffer)


class DQNAgent:
    """DQN agent: manages action selection, experience storage, and network training."""

    def __init__(self, rows = 15, cols = 15, lr=1e-3, gamma=0.60,
                 epsilon_start=1.0, epsilon_end=0.05, epsilon_decay=0.99995,
                 buffer_capacity=10_000, batch_size=64, target_update_freq=100):

        self.gamma = gamma
        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.batch_size = batch_size
        self.target_update_freq = target_update_freq
        self.steps = 0
        self.episodes = 0
        
        self.q_net = SnakeCNN(rows, cols)
        
        self.target_net = copy.deepcopy(self.q_net)
        self.target_net.eval()

        self.optimizer = torch.optim.Adam(self.q_net.parameters(), lr=lr)
        self.loss_fn = nn.MSELoss()
        self.buffer = ReplayBuffer(buffer_capacity)

    def select_action(self, state, direction):
        """Selects an action using epsilon-greedy: random action with probability epsilon,
        otherwise the action with the highest Q-value. Returns -1 (left), 0 (straight), 1 (right)."""
        if random.random() <= self.epsilon:
            return random.randint(-1, 1)
        else:
            with torch.no_grad():
                state = torch.tensor(state[0])
                direction = torch.tensor(direction, dtype=torch.float32)
                return self.q_net(state.unsqueeze(0), direction.unsqueeze(0)).argmax().item() - 1

    def store(self, state, action, direction, reward, next_state, next_dir, done):
        """Saves to the buffer state given"""
        action = action + 1
        state = torch.tensor(state[0])
        direction = torch.tensor(direction, dtype=torch.float32)
        next_state = torch.tensor(next_state)
        next_dir = torch.tensor(next_dir, dtype=torch.float32)
        self.buffer.push(state, action, direction, reward, next_state, next_dir, done)

    def train_step(self):
        """Trains the network using the states known in buffer"""
        if len(self.buffer) < self.batch_size:
            return

        states, actions, direction, rewards, next_states, next_direction, dones = self.buffer.sample(self.batch_size)

        current_q = self.q_net(states, direction).gather(1, actions.unsqueeze(1)).squeeze(1)

        with torch.no_grad():
            next_q = self.target_net(next_states, next_direction).max(1).values
            target_q = rewards + self.gamma * next_q * (1 - dones)

        loss = self.loss_fn(current_q, target_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)
        self.steps += 1

        if self.steps % self.target_update_freq == 0:
            self.target_net.load_state_dict(self.q_net.state_dict())

    def export_model(self):
        """Returns networks's state_dict"""
        return {'model': self.q_net.state_dict(),
                'epsilon': self.epsilon,
                'optimizer': self.optimizer.state_dict()
                }
    
    def import_model(self, model):
        self.q_net.load_state_dict(model['model'])
        self.epsilon = model['epsilon']
        self.optimizer.load_state_dict(model['optimizer'])
