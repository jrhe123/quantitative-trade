import pandas as pd

import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

from unittest import TestCase


class TestBoll(TestCase):
    def testBoll(self):
        # 绘制布林带
        N = 5

        weights = np.ones(N) / N
        print("Weights", weights)

        file_name = "./data/data.csv"
        c = np.loadtxt(file_name, delimiter=",", usecols=(2,), unpack=True)
        sma = np.convolve(weights, c)[N - 1 : -N + 1]
        deviation = []
        C = len(c)

        for i in range(N - 1, C):
            if i + N < C:
                dev = c[i : i + N]
            else:
                dev = c[-N:]

            averages = np.zeros(N)
            averages.fill(sma[i - N - 1])
            dev = dev - averages
            dev = dev**2
            dev = np.sqrt(np.mean(dev))
            deviation.append(dev)

        deviation = 2 * np.array(deviation)
        print(len(deviation), len(sma))
        upperBB = sma + deviation
        lowerBB = sma - deviation

        c_slice = c[N - 1 :]
        between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB))

        print(lowerBB[between_bands])
        print(c[between_bands])
        print(upperBB[between_bands])
        between_bands = len(np.ravel(between_bands))
        print("Ratio between bands", float(between_bands) / len(c_slice))

        t = np.arange(N - 1, C)
        plot(t, c_slice, lw=1.0)
        plot(t, sma, lw=2.0)
        plot(t, upperBB, lw=3.0)
        plot(t, lowerBB, lw=4.0)
        show()


def main():
    obj = TestBoll()
    obj.testBoll()


if __name__ == "__main__":
    main()
