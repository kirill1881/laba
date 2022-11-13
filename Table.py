import numpy as np


class Table:
    def __init__(self, alfa, n, name= None):
        self.name = name
        self.alfa = alfa
        self.n = n
        self.table = [[0 for j in range(len(n))] for i in range(len(alfa))]

    def set(self, i, j, leftEdge, rightEdge):
        self.table[i][j] = Field(leftEdge, rightEdge)

    def print(self):
        if self.name is not None:
            print(self.name)

        s = '   alfa:' + ' ' * 10
        for a in self.alfa:
            s += str(a) + ' ' * 30
        print(s)

        print('n: ' + ' ' * 50)
        for i in range(len(self.alfa)):
            s = '   ' + str(self.n[i]) + ': '
            for j in range(len(self.n)):
                s += self.table[i][j].toString() + '    '
            print(s)

class Field:
    def __init__(self, leftEdge = 0, rightEdge = 0):
        precession = 3
        self.leftEdge = round(leftEdge, precession)
        self.rightEdge = round(rightEdge, precession)
        self.width = round(self.rightEdge - self.leftEdge, precession)
    def toString(self):
        return '(' + str(self.leftEdge) + ', ' + str(self.rightEdge) + '),[' + str(self.width) +']'