# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ep = 1


def orgcal(a):
    if 2*a[1]+3*a[0] > 5:
        return 1
    else:
        return -1


class Perceptron:
    w = np.array([1, 1])
    b = 1

    def __init__(self):
        pass

    def run(self, xr):
        result = np.dot(xr, self.w)+self.b
        if result >= 0:
            return 1
        return -1

if __name__ == '__main__':
    pp = Perceptron()
    for i in range(1, 200000):
        x = np.random.rand(2)*2
        y = orgcal(x)
        res = pp.run(x)
        # print(y*res)
        if y*res < 0:
            pp.w = pp.w+ep*y*x
            pp.b += ep*y
            ep = (np.sum(pp.w)+pp.b)/1000

    print(np.sum(pp.w)+pp.b)
