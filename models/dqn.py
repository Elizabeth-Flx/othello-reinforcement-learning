import torch
import torch.nn as nn

class OthelloDQN(nn.Module):

    # To do: Add norms to the layers
    def __init__(self):
        super(OthelloDQN, self).__init__()

        self.conv3x3 = nn.Conv2d(2, 64, 3, padding=1)
        self.conv5x5 = nn.Conv2d(64, 64, 5, padding=2)
        # self.conv3x8 = nn.Conv2d(64, 64, (3,8), padding=(1,7))
        # self.conv8x3 = nn.Conv2d(64, 64, (8,3), padding=(7,1))

        self.fc1 = nn.Linear(64*8*8, 512)
        self.fc2 = nn.Linear(512, 64)

        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid() 

    def forward(self, x):
        x = self.relu(self.conv3x3(x))
        x = self.relu(self.conv5x5(x))

        x = x.view(x.size(0), -1) # Flatten

        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        x = self.sigmoid(x)

        return x