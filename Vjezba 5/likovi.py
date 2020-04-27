#Zadatak 5.1
class Kruznica(object):

    def __init__(self,radijus):
        self.radijus = radijus

    def __str__(self):
        return "Kruznica radijusa %.2f" % (self.radijus)

class Kvadrat(object):

    def __init__(self,stranica):
        self.stranica = stranica

    def __str__(self):
        return "Kvadrat stranice %.2f" %(self.stranica)


if __name__ == '__main__':
    print('*** test likovi ***')
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)





