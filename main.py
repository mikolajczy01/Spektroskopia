import matplotlib.pyplot as mpl
import numpy as np
from gauss import d2Gauss, dGauss, Gauss
from algorytm import szukaj, peaks


if __name__ == '__main__':

    # Dziedzina funkcji
    x = np.arange(-10, 100, 0.5)

    # Losowe parametry (liczby całkowite)
    p = np.random.randint(1, 70, size=9)
    # p[2] = 100
    # p[5] = 300
    # p[8] = 600
    p = [25, 7, 11, 61, 30, 34, 52,  5, 63]

    print(p)

    # Generowanie zbioru wartości
    y = np.array([(Gauss(p[0], p[1], p[2], i) + Gauss(p[3], p[4], p[5], i) + Gauss(p[6], p[7], p[8], i))
                 for i in x])

    # Funkcja szukająca
    parametry = szukaj(x, y)
    y2 = np.array(
        [(Gauss(parametry[0], parametry[1], parametry[2], i) + Gauss(parametry[3], parametry[4], parametry[5], i) + Gauss(parametry[6], parametry[7], parametry[8], i)) for i in x])

    # Wyświetlanie wykresu
    mpl.plot(x, y)
    mpl.plot(x, y2, 'g', ls='dashed')
    mpl.show()

    # [25, 7, 11, 61, 30, 34, 52,  5, 63]
