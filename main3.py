from faulthandler import disable
import matplotlib.pyplot as mpl
import numpy as np
from gauss import Gauss
from algorytm import mrq
import PySimpleGUI as sg
import os.path


def okno1():

    layout = [
        [sg.Text("Wybierz funkcję opisującą rozkład: ")],
        [sg.Radio('Funkcje Gaussa', "-RADIO1-", default=True)],
        [sg.Radio('Pochodne Funkcji Gaussa', "-RADIO1-")],
        [sg.Text("Wybierz pliki: ")],
        [sg.FileBrowse('Współrzędne', target=(sg.ThisRow, 1), size=(13, None)),
         sg.InputText(key="-COORD-", size=(30, None))],
        [sg.FileBrowse('Parametry', target=(sg.ThisRow, 1), size=(13, None)),
         sg.InputText(key='-PARA-', size=(30, None))],
        [sg.Text()],
        [sg.Button("Dalej", key='-FUN-', disabled=True)]
    ]

    return sg.Window('Spektroskopia', layout, font=12)


def okno2():
    first_col = [[sg.Text("essa")]]

    second_col = [[sg.Text("essa")]]

    layout = [
        [sg.Column(first_col), sg.VSeparator(), sg.Column(second_col)]
    ]

    return sg.Window("Spektroskopia", layout, size=(1000, 677))


if __name__ == '__main__':

    window = okno1()

    while True:
        event, values = window.read()

        if values["-COORD-"]:
            print('essa')
            window['-FUN-'].update(disabled=False)

        if event == "-FUN-":
            window.close()
            window = okno2()

        if event == sg.WIN_CLOSED:
            break

    window.close()

#     y = []
#     x = []
#     p = []
#     sig = []
#     f = open("ABS.DAT", 'r')
#     for ind, dat in enumerate(f):
#         dat = dat.split(' ')
#         if ind > 0:
#             x.append(float(dat[2]))
#             y.append(float(dat[4]))
#             sig.append(1)
#     f.close()
#     f = open('PARD1.dat', 'r')
#     for ind, dat in enumerate(f):
#         dat = dat.split(' ')
#         if ind > 0:
#             try:
#                 p.append(float(dat[-1]))
#             except:
#                 pass
#     f.close()
# start = timer()
# z = mrq(x, y, sig, p, Gauss)
# z.fit()
# print(z.p)
