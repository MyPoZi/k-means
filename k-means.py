# -*- coding: utf-8 -*-
import pandas as pd
import pylab
import matplotlib.pyplot as plt

# クラスタ数
K = 3

data = pd.read_csv("data.csv", header=None).values

idx = pylab.np.zeros(data.shape[0])
centers = pylab.np.array([[1.0, 2.0], [4.0, 1.0], [4.0, 4.0]])
plt.scatter(centers[:, 0], centers[:, 1], color=["r", "b", "g"])

for j in pylab.np.arange(0, 3):

    for i in range(data.shape[0]):
        idx[i] = pylab.np.argmin(pylab.np.sum((data[i, :] - centers) ** 2, axis=1))

    for k in range(K):
        centers[k, :] = data[idx == k, :].mean(axis=0)

    plt.subplot(2, 2, j + 1)
    plt.scatter(data[idx == 0, 0], data[idx == 0, 1], color="r", s=10, alpha=0.5)
    plt.scatter(data[idx == 1, 0], data[idx == 1, 1], color="b", s=10, alpha=0.5)
    plt.scatter(data[idx == 2, 0], data[idx == 2, 1], color="g", s=10, alpha=0.5)
    plt.scatter(centers[:, 0], centers[:, 1], color=["r", "b", "g"])
    print(centers)

plt.show()
