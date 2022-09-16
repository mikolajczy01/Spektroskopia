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
         sg.InputText(key="-COORD-", size=(30, None), enable_events=True)],
        [sg.FileBrowse('Parametry', target=(sg.ThisRow, 1), size=(13, None)),
         sg.InputText(key='-PARA-', size=(30, None))],
        [sg.Text()],
        [sg.Button("Dalej", key='-FUN-', disabled=True)]
    ]

    window = sg.Window('Spektroskopia', layout, font=12)

    while True:
        event, values = window.read()

        if values["-COORD-"] is not None:
            window['-FUN-'].update(disabled=False)
        else:
            window['-FUN-'].update(disabled=True)

        if event == "-FUN-":
            window.close()
            okno2()
            break

        if event == sg.WIN_CLOSED:
            window.close()
            break


def okno2():
    first_col = [
        [sg.Text("Funkcja: ")],
        [sg.Text('F(x) = a*exp( ( -(x+b) \ (c) )^2 * 4 * ln(2) )')],
        [sg.Text()],
        [sg.Text('Parametry: ')],
        [sg.Text('     a', size=(10, None)), sg.Text(
            '    b', size=(10, None)), sg.Text('    c', size=(10, None))]
    ] + parametry(3) + [
        [sg.Text()],
        [sg.Button('Wstępna Analiza'), sg.Button('Oblicz współczynniki')]
    ]

    second_col = [[sg.Text("Wykres")]]

    layout = [
        [sg.Column(first_col), sg.VSeparator(), sg.Column(second_col)]
    ]

    window = sg.Window("Spektroskopia", layout, font=12)

    while True:
        event, values = window.read()

        if event == '-+-':
            pass
        if event == '---':
            pass

        if event == sg.WIN_CLOSED:
            window.close()
            break


def parametry(x: int):
    y = []
    for i in range(x):
        y.append([sg.Text(i+1), sg.Input(enable_events=True, key=f"-a{i}-".format(i), size=(10, None), pad=(3, 8)), sg.Input(enable_events=True,
                                                                                                                             key="-b{}-".format(i), size=(10, None), pad=(3, 8)), sg.Input(enable_events=True, key="-c{}-".format(i), size=(10, None), pad=(3, 8))])
    y[-1].append(sg.Button('+', key='-+-', size=(2, None)))
    y[-1].append(sg.Button('-', key='---', size=(2, None)))
    return y


if __name__ == '__main__':

    okno1()

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
