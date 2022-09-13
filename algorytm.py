from json import tool
from types import FunctionType
import numpy as np


class mrq(object):

    def __init__(self, x: list, y: list, sig: list, p: list, func: FunctionType):
        self.__x = np.array(x)  # X
        self.__y = np.array(y)  # Y
        self.__sig = np.array(sig)  # Odchylenie standardowe
        self.__p = np.array(p)  # Parametry
        self.__func = func  # Funkcja
        self.__sp = len(p)  # ilość parametrów (ma)

        # wektor holdowanych parametrów (ia) 0 - nie 1 - tak
        self.__held = np.zeros(len(p))

        self.__alfa = np.zeros((len(p), len(p)))  # macierz alfa
        self.__sh = len(p)  # ilość nieholdowanych (mfit)
        self.__sdat = len(x)  # ilość punktów
        self.__chi2 = 0.0  # chi^2
        self.__lamb = 0.001  # lamda
        self.__MAXITER = 1000  # ilość pętli
        self.__covar = np.zeros((len(p), len(p)))  # sigma
        self.__ndone = 4  # ilość spełnionych warunków
        self.__tol = 0.0001

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def sig(self):
        return self.__sig

    @property
    def p(self):
        return self.__p

    @property
    def func(self):
        return self.__func

    @property
    def sp(self):
        return self.__sp

    @property
    def held(self):
        return self.__held

    @property
    def alfa(self):
        return self.__alfa

    @alfa.setter
    def alfa(self, value):
        self.__alfa = value

    @property
    def sh(self):
        return self.__sh

    @sh.setter
    def sh(self, value: int):
        self.__sh = value

    @property
    def sdat(self):
        return self.__sdat

    @property
    def chi2(self):
        return self.__chi2

    @chi2.setter
    def chi2(self, value):
        self.__chi2 = value

    @property
    def lamb(self):
        return self.__lamb

    @lamb.setter
    def lamb(self, value):
        self.__lamb = value

    @property
    def MAXITER(self):
        return self.__MAXITER

    @MAXITER.setter
    def MAXITER(self, value):
        self.__MAXITER = value

    @property
    def covar(self):
        return self.__covar

    @property
    def ndone(self):
        return self.__ndone

    @ndone.setter
    def ndone(self, value):
        self.__ndone = value

    @property
    def tol(self):
        return self.__tol

    @tol.setter
    def tol(self, value):
        self.__tol = value

    @covar.setter
    def covar(self, value):
        self.__covar = value

    def covsrt(self, covar):
        for i in range(self.sh, self.sp):
            for j in range(0, i+1):
                covar[i][j] = 0
                covar[j][i] = 0
        k = self.sh - 1
        for j in range(self.sp-1, -1, -1):
            if self.held[j] == 0:
                for i in range(self.sp):
                    covar[i][k], covar[i][j] = covar[i][k], covar[i][j]
                for i in range(self.sp):
                    covar[k][i], covar[j][i] = covar[k][i], covar[j][i]
                k -= 1
        return covar

    def mqrcof(self, p: np.ndarray, alfa: np.ndarray, beta: np.ndarray):
        dyda = np.zeros((self.sp, 1))  # wektor pochodnych po parametrach

        for i in range(self.sh):
            for j in range(0, i+1):
                alfa[i][j] = 0.0
            beta[i] = 0.0

        self.chi2 = 0.0

        for i in range(self.sdat):
            dyda, ymod = self.func(self.x[i], p)
            sig2i = 1.0 / (self.sig[i] * self.sig[i])
            dy = self.y[i] - ymod
            j = 0
            for k in range(self.sp):
                if self.held[k] == 0:
                    wt = dyda[k]*sig2i
                    m = 0
                    for l in range(k+1):
                        if self.held[l] == 0:
                            alfa[j][m] += wt * dyda[l]
                            m += 1

                    beta[j] += dy*wt
                    j += 1
            self.chi2 += dy*dy*sig2i

        for i in range(1, self.sh):
            for j in range(i):
                alfa[j][i] = alfa[i][j]

        return alfa, beta

    def fit(self):

        done = 0
        self.tol = 0.0001

        # zmiena ilości nieholdowanych
        self.sh = self.sp - np.count_nonzero(self.held == 1)

        beta = np.zeros((self.sp, 1))  # wektor Beta
        atry = np.zeros((self.sp, 1))  # wektor nwm
        da = np.zeros((self.sp, 1))

        self.alfa, beta = self.mqrcof(self.p, self.alfa, beta)

        oneda = np.zeros((self.sh, 1))  # wektor nwm
        temp = np.zeros((self.sh, self.sh))  # wektor nwm

        for i in range(self.sp):
            atry[i] = self.p[i]
        ochi2 = self.chi2

        for i in range(1000):

            if done == self.ndone:
                self.lamb = 0.0

            for j in range(self.sh):

                for k in range(self.sh):
                    self.covar[j][k] = self.alfa[j][k]

                self.covar[j][j] = self.alfa[j][j] * (1.0+self.lamb)

                for k in range(self.sh):
                    temp[j][k] = self.covar[j][k]
                oneda[j] = beta[j]

            temp = np.linalg.inv(temp)
            oneda = temp @ oneda

            for j in range(self.sh):
                for k in range(self.sh):
                    self.covar[j][k] = temp[j][k]
                da[j] = oneda[j][0]

            if done == self.ndone:
                self.covsrt(self.covar)
                self.covsrt(self.alfa)
                return

            l = 0

            for j in range(self.sp):
                if self.held[j] == 0:
                    atry[j] = self.p[j] + da[l]
                    l += 1

            self.covar, da = self.mqrcof(atry, self.covar, da)

            if abs(self.chi2 - ochi2) < max([self.tol, self.tol*self.chi2]):
                done += 1

            if self.chi2 < ochi2:

                self.lamb *= 0.1
                ochi2 = self.chi2

                for j in range(self.sh):

                    for k in range(self.sh):
                        self.alfa[j][k] = self.covar[j][k]
                    beta[j] = da[j]

                for j in range(self.sp):
                    self.p[j] = atry[j]
            else:
                self.lamb *= 10.0
                self.chi2 = ochi2

    def hold(self, x: int):
        self.__held[x] = 1

    def free(self, x: int):
        self.held[x] = 0
