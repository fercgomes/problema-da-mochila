#!/bin/python
import sys
from random import randint

def VerificaPM(P, V, VMIN, W, CERT):
    assert(len(P) == len(V))
    assert(len(P) == len(CERT))

    PesoTotal = 0
    ValorTotal = 0

    for i in range(len(CERT)):
        PesoTotal += CERT[i] * P[i]
        ValorTotal += CERT[i] * V[i]

    if PesoTotal <= W and ValorTotal > VMIN:
        return True
    else:
        return False

def randomList(n, a, b):
    newList = []
    for i in range(n):
        newList.append(randint(a, b))

    return newList

def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        P = randomList(n, 0, 100)
        V = randomList(n, 0, 100)
        VMIN = randint(0, 100)
        W = randint(0, 100)
        CERT = randomList(n, 0, 1)

        VerificaPM(P, V, VMIN, W, CERT)


if __name__ == "__main__":
    main()
