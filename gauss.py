from math import exp, log


def Gauss(x: float, p: list):
    y = 0.0
    dyda = []
    for i in range(0, len(p), 3):
        arg = (x - p[i + 1]) / p[i + 2]
        ex = exp(-((arg)**2) * 4 * log(2))
        fac = p[i] * ex * 2. * arg
        y += p[i] * ex
        dyda.append(ex)
        dyda.append(fac / p[i + 2])
        dyda.append(fac * arg / p[i + 2])
    return dyda, y
