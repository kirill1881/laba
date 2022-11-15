import random
from importlib.metadata import distribution
from turtle import st

import numpy as np
from collections import Counter

import math
import Table


# rvs [X] for 5000+ samples, generate by hi-square distribution
# transform this rvs [X] -> [Y]
# 2 ways of building(accurate and aprox) :
    # build table with confidence intervals values for params: [N] and [alfa - confidence level]


def rvsTransform(x,  ny):
    sum_amm = int(len(x) / ny)

    y = np.zeros(ny)
    for i in range(ny):
        sum = 0
        for j in range(sum_amm):
            sum += x[sum_amm * i + j]
        y[i] = sum
    return y

def Var(X):
    m = X.mean()
    res = 0
    for x in X:
        res += pow(m-x, 2)
    res /= len(X)-1
    return res

def t(k, pr):
    return st.t(k).ppf(pr)

def f(pr):
    return st.norm.ppf(pr)

def buildAccurateConfidenceInterval(X, alfa, ny):
    print()
    table = Table(alfa, ny, 'Accurate method')
    for i in range(len(ny)):
        Y = rvsTransform(X, ny[i])
        print(len(Y), 'E=', round(Y.mean(), precession), 'SD=', round(Y.std(), precession))
        for j in range(len(alfa)):
            delta = t(ny[i] - 1, alfa[j]) * Y.std() / math.sqrt(ny[i])
            table.set(i, j, Y.mean() - delta, Y.mean() + delta)
    return table

def biuldApproximateCondifenceInterval(X, alfa, ny):
    print()
    table = Table(alfa, ny, name='Approx method')
    for i in range(len(ny)):
        Y = rvsTransform(X, ny[i])
        print('n=', len(Y), 'E=', round(Y.mean(), precession), 'SD=', round(Y.std(), precession))
        for j in range(len(alfa)):
            delta = f(alfa[j]) * Y.std() / math.sqrt(ny[i])
            table.set(i, j, Y.mean() - delta, Y.mean() + delta)
    return table





if __name__ == '__main__':

    precession = 3
    hi_param = 5

    nx = 5000
    ny = [20, 50, 100]
    alfa = [0.9, 0.95, 0.99]

    X = distribution(hi_param).rvs(nx)

    buildAccurateConfidenceInterval(X, alfa, ny).print()
    biuldApproximateCondifenceInterval(X, alfa, ny).print()