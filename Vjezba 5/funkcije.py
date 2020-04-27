#Zadatak 5.2

import likovi
from math import pi , pow

def opseg(lik):
    if isinstance(lik,likovi.Kruznica):
        return lik.radijus * 2 * pi
    elif isinstance(lik,likovi.Kvadrat):
        return lik.stranica * 4


def povrsina(lik):
    if isinstance(lik,likovi.Kruznica):
        return pow(lik.radijus,2) * pi
    elif isinstance(lik,likovi.Kvadrat):
        return lik.stranica * lik.stranica

if __name__ == '__main__':
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)




