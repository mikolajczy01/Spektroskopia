import numpy as np
import gauss as g


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


def LSM(x, y, p1, p2, p3, NB):
    LP = 3
    A = np.zeros((NB*LP, NB*LP))
    B = np.zeros((NB*LP, 1))
    for i in range(A.shape[0]):
        l = 0
        m = 0
        for k in range(len(x)):
            B[i] += (y[k] - g.Gauss(p1[i % 3], p2[i % 3], p3[i % 3], x[k])) * g.dGaussk(p1[i % 3], p2[i % 3],
                                                                                        p3[i % 3], x[k], i % LP)
        for j in range(A.shape[1]):
            print(i % 3, (i+l) % 3, j % 3, (j+m) % 3)
            for k in range(len(x)):

                A[i, j] += g.dGaussk(p1[(i+l) % 3], p2[(i+l) % 3], p3[(i+l) % 3],
                                     x[k], i % 3) * g.dGaussk(p1[(j+m) % 3], p2[(j+m) % 3], p3[(j+m) % 3], x[k], j % 3)
            if j % LP == 2:
                l += 1
        if i % LP == 2:
            m += 1

    print(A)
    sol = np.linalg.inv(A) @ B
    print(sol)
    return [1, 1, 1, 1, 1, 1, 1, 1, 1]


def szukaj(x, y):
    p1 = []
    p2 = []
    p3 = []
    peak = peaks(x, y)
    for i in peak:

        p1.append(y[i])

        if i == peak[0]:
            p2.append(polowka_L(x, y, i))
        elif i == peak[-1]:
            p2.append(polowka_P(x, y, i))
        else:
            p2.append(polowka_S(x, y, i))

        p3.append(x[i])

    while len(p1) != 3:
        p1.append(y[int(len(y)/2)])

        p2.append(x[int(len(x)/2)]/10)

        p3.append(x[int(len(x)/2)])
    print(p1, p2, p3)

    p = LSM(x, y, p1, p2, p3, 3)
    return [p1, p2, p3]
