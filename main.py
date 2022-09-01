import matplotlib.pyplot as mpl
import numpy as np
from gauss import d2Gauss, dGauss, Gauss
from algorytm import szukaj, peaks


if __name__ == '__main__':

    # kolory
    kolory = ['r', 'y', 'g']

    # Dziedzina funkcji
    x = np.arange(0, 500, 0.5)

    # Losowe parametry (liczby całkowite)
    p = np.random.randint(1, 70, size=9)
    # p[2] = 100
    # p[5] = 130
    # p[8] = 300
    p = [40,  24, 100,  20,  66, 130,  69,  23, 300]

    print(p)

    # Generowanie zbioru wartości oraz wykresu
    y = np.array([(Gauss(p[0], p[1], p[2], i) + Gauss(p[3], p[4], p[5], i) + Gauss(p[6], p[7], p[8], i))
                 for i in x])
    mpl.plot(x, y)

    # Funkcja szukająca
    parametry = szukaj(x, y)
    for j in range(len(parametry[0])):
        y2 = np.array(
            [(Gauss(parametry[0][j], parametry[1][j], parametry[2][j], i)) for i in x])
        mpl.plot(x, y2, kolory[j % 3], ls='dashed')

    # Wyświetlanie wykresu
    mpl.show()

    # [12, 62, 63, 25, 29,  7, 44, 39, 64]
    # [ 30,  49, 100,  65,  11, 130,  25,  69, 300]
    # [40,  24, 100,  20,  66, 130,  69,  23, 300]
