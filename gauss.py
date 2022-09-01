from math import sqrt, exp, pi, log


# def Gauss(p1, p2, p3, x):
#     return p1*(1/(p2*sqrt(2*pi))*exp((-(x-p3)**2)/2*(p2**2)))

def Gauss(p1, p2, p3, x):
    if p2 == 0:
        return 0
    return p1*exp((-(x-p3)**2)/(p2**2)*4*log(2))


def dGaussk(p1, p2, p3, x, k):
    if k == 0:
        return exp((-(x-p3)**2)/(p2**2)*4*log(2))
    if k == 1:
        return p1*exp((-(x-p3)**2)/(p2**2)*4*log(2))*(((x-p3)**2)/(p2**3)*8*log(2))
    if k == 2:
        return p1*exp((-(x-p3)**2)/(p2**2)*4*log(2))*((-(x-p3))/(p2**2)*8*log(2))

    # def dGauss(p1, p2, p3, x):
    #     return p1*(1/((p2**3)*sqrt(2*pi))*exp((-(x-p3)**2)/2*(p2**2)))*(-(x-p3)/p2**2)


def dGauss(p1, p2, p3, x):
    if p2 == 0:
        return 0
    return p1*exp((-(x-p3)**2)/(p2**2)*4*log(2))*((-(x-p3)/(p2**2))*8*log(2))


# def d2Gauss(p1, p2, p3, x):
#     return p1*(1/((p2**5)*sqrt(2*pi))*exp((-(x-p3)**2)/2*(p2**2)))*(((x-p3)**2)-p2**2)

def d2Gauss(p1, p2, p3, x):
    if p2 == 0:
        return 0
    return p1*exp((-(x-p3)**2)/(p2**2)*4*log(2))*((-(x-p3)/(p2**2))*8*log(2))*((p3/(p2**2))*8*log(2))
