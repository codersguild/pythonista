#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import numpy as np
import torch
import random
from tqdm import tqdm
from torch import Tensor, from_numpy
from torch.nn import Linear, MSELoss, functional, BCELoss, LSTM, GRU as F
import matplotlib.pyplot as plt
from torch.optim import SGD, Adam, RMSprop
from torch.utils.data import Dataset, DataLoader
from torch.optim.lr_scheduler import StepLR

"""
 x 	y 	 output
6 	10 	265.2
12 	8 	308.4
-3 	-4 	46.4
5 	5 	88.3
2 	4 	37
3.5 	4.2 	55.3
"""

values = [
     [6.0, 10.0, 265.2],
     [12., 8., 308.4],
     [-3., -4., 46.4],
     [5., 5., 88.3],
     [2., 4., 37.],
     [3.5, 4.2, 55.3]
]

lr=0.0001

a = torch.tensor(random.uniform(0,1), dtype=torch.float32, requires_grad=True)
b = torch.tensor(random.uniform(0,1), dtype=torch.float32, requires_grad=True)
c = torch.tensor(random.uniform(0,1), dtype=torch.float32, requires_grad=True)
d = torch.tensor(random.uniform(0,1), dtype=torch.float32, requires_grad=True)
optimizer = torch.optim.SGD([a, b, c, d], lr=0.0001)
criterion = torch.nn.MSELoss()

def eval_f(x, y):
     return a*x**2 + b*y**2 + c*x*y + d

if __name__ == "__main__":
     for epochs in range(1000):
          for (x, y, target) in values:
               x = torch.tensor(float(x), dtype=torch.float32, requires_grad=False)
               y = torch.tensor(float(y), dtype=torch.float32, requires_grad=False)
               target = torch.tensor(target, dtype=torch.float32, requires_grad=False)
               loss = criterion(eval_f(x, y), target) / len(values)
               loss.backward()
               optimizer.step()
               for params in [a, b, c, d]:
                    params.grad = None

     print("Answer : ", a, b, c, d)
     for idx, (x, y, _) in enumerate(values):
          print(f"test_{idx} : ", eval_f(x, y))


