# import the required packages
import torch
from torch import Tensor
from torch.nn import Linear, MSELoss, functional as F
from torch.optim import SGD, Adam, RMSprop
from torch.autograd import Variable
import numpy as np
# define our data generation function
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# device = torch.device('cpu' if torch.cuda.is_available() else 'cuda')


def data_generator(data_size=50):
    # f(x) = y = 8x^2 + 4x - 3
    inputs = []
    labels = []

    # loop data_size times to generate the data
    for ix in range(data_size):

        # generate a random number between 0 and 1000
        x = np.random.randint(5500) / 5500

        # calculate the y value using the function 8x^2 + 4x - 3
        y = 4 * (x * x) + 3

        # append the values to our input and labels lists
        inputs.append([x])
        labels.append([y])

    return inputs, labels


# define the model
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = Linear(1, 12)
        self.fc2 = Linear(12, 10)
        self.fc3 = Linear(10, 10)
        self.fc4 = Linear(10, 1)

    def forward(self, x):
        x = F.dropout(F.relu(self.fc1(x)), p=0.4)
        x = F.dropout(F.relu(self.fc2(x)), p=0.5)
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x


model = Net().to(device)

# define the loss function
critereon = MSELoss()

# define the optimizer
# optimizer = SGD(model.parameters(), lr=0.01)

# define the optimizer
optimizer = Adam(model.parameters(), lr=0.01, weight_decay=1e-5)

# define the number of epochs and the data set size
nb_epochs = 300
data_size = 3000
# create our training loop
for epoch in range(nb_epochs):
    X, y = data_generator(data_size)
    epoch_loss = 0.00

    for ix in range(data_size):
        inputs = torch.tensor(X[ix]).to(device)
        outputs = torch.tensor(y[ix], requires_grad=False).to(device)
        y_pred = model(inputs)
        loss = critereon(y_pred, outputs)
        # loss = torch.tensor(y_pred.item() * (1 - outputs.item()),
        #                     requires_grad=True)
        epoch_loss = loss.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if ix % 500 == 0:
            print("Train Epoch: {} Loss: {:.6f}".format(epoch, epoch_loss))

# test the model
model.eval()
for _ in range(100):
    test_data = data_generator(3)
    test_input = torch.tensor(test_data[0][0]).to(device)
    prediction = model(test_input)

    print("Prediction: {}".format(prediction.data[0]))
    print("Expected: {}".format(test_data[1][0]))
