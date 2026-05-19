import torch
import torch.nn as nn


class SnakeCNN(nn.Module):
    """Trains one CNN in order to play the snake game"""
    def __init__(self, rows, cols, n_actions=3):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )

        conv_out = 32 * (rows // 2) * (cols // 2)

        self.fc = nn.Sequential(
            nn.Linear(conv_out, 128),
            nn.ReLU(),
            nn.Linear(128, n_actions),
        )

    def forward(self, x):
        """
        Executes the forward flow for a given tensor
        Args:
        x (Tensor): shape (B, 3, rows, cols)
        Returns:
        Tensor: shape (B, n_actions) - Q-Value per action

        Where B is batch size
        """
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)
