import os
import sys
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from alive_progress import alive_bar
import matplotlib.pyplot as plt

# Device configuration
if torch.cuda.is_available():
    print("Running on GPU")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyper-parameters
input_size = 784  # 28 x 28
hidden_size = 700
num_classes = 10
num_epochs = 10
batch_size = 50
learning_rate = 0.0009

customTransformer = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.1307,), std=(0.3081,))
])

# MNIST dataset
train_dataset = torchvision.datasets.MNIST(root='dataset/',
                                           train=True,
                                           transform=customTransformer,
                                           download=True)

test_dataset = torchvision.datasets.MNIST(root='dataset/',
                                          train=False,
                                          transform=customTransformer,
                                          download=True)

# Data loader
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)

examples = iter(test_loader)
example_data, example_targets = examples.next()

for i in range(20):
    plt.subplot(5, 4, i+1)
    plt.imshow(example_data[i][0], cmap='gray')
plt.show()

# Fully connected neural network with 5 hidden layers


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.input_size = input_size
        self.relu = nn.ReLU()
        self.l1 = nn.Linear(input_size, hidden_size)  # Input Layer
        self.l2 = nn.Linear(hidden_size, int(hidden_size/2))
        self.l3 = nn.Linear(int(hidden_size/2), int(hidden_size/2))
        self.l4 = nn.Linear(int(hidden_size/2), int(hidden_size/4))
        self.l5 = nn.Linear(int(hidden_size/4), num_classes)  # Output Layer

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        out = self.relu(out)
        out = self.l4(out)
        out = self.relu(out)
        out = self.l5(out)
        # no activation and no softmax at the end
        return out


model = NeuralNet(input_size, hidden_size, num_classes).to(device)

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    with alive_bar(len(train_loader)) as trainbar:
        for idx, (images, labels) in enumerate(train_loader):
            # origin shape: [100, 1, 28, 28]
            # resized: [100, 784]
            images = images.reshape(-1, 28 * 28).to(device)
            labels = labels.to(device)

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1)

            # Adam step : This tweaks the weights and biases
            # based on gradients computed from above.
            optimizer.step()

            # if (idx + 1) % 5 == 0:
            #   print(
            #       f'Epoch [{epoch+1}/{num_epochs}], Step [{idx + 1}/{n_total_steps}], Loss: {loss.item():.6f}')
            trainbar()

# Test the model
# In test phase, we don't need to compute gradients (for memory efficiency)
n_correct = 0
n_samples = 0
model.eval()  # Important Step

with torch.no_grad():
    with alive_bar(len(test_loader)) as testbar:
        for images, labels in test_loader:

            images = images.to(device=device)
            labels = labels.to(device=device)

            images = images.reshape(images.shape[0], -1)
            outputs = model(images)

            # max returns (value ,index)
            _, predicted = torch.max(outputs.data, 1)
            n_correct += (predicted == labels).sum().item()
            n_samples += predicted.size(0)
            testbar()

    acc = 100.0 * n_correct / n_samples
    print(f'Accuracy of the network on the 10000 test images: {acc:.3f} %')

model.train()
