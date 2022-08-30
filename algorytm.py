import numpy as np


def polowka_L(x, y, p):
    yp = y[p]/2
    xp = x[p]
    while y[p] > yp:
        p -= 1
    return 2*(xp - x[p])


def polowka_P(x, y, p):
    yp = y[p]/2
    xp = x[p]
    while y[p] > yp:
        p += 1
    return 2*(x[p] - xp)


def polowka_S(x, y, p):
    yp = y[p]/2
    xp = x[p]
    pl = p
    pr = p
    while y[pl] > yp:
        pl += 1
    while y[pr] > yp:
        pr += 1
    return 2*(((x[pl]+x[pr])/2) - xp)


def peaks(x, y):
    p = []
    for i in range(1, len(x)-1):
        if y[i+1] < y[i] and y[i-1] < y[i]:
            p.append(i)
    return p


def szukaj(x, y):
    p = []
    peak = peaks(x, y)
    for i in peak:

        p.append(y[i])

        if i == peak[0]:
            p.append(polowka_L(x, y, i))
        elif i == peak[-1]:
            p.append(polowka_P(x, y, i))
        else:
            p.append(polowka_S(x, y, i))

        p.append(x[i])

    while len(p) != 9:
        p.append(0)
    print(p)
    return p
