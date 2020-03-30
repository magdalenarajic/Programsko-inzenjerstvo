class Razlomak(object):
     '''Klasa razlomak'''

     def __init__(self, brojnik, nazivnik = 1):
           if nazivnik == 0:
             raise Exception('Nazivnik ne moze biti 0')
           self._brojnik = brojnik
           self._nazivnik = nazivnik

     def __str__(self):
            return '%d|%d' % (self._brojnik, self._nazivnik)
#Zadatak 2.2

     @staticmethod
     def inverz(self):
         return Razlomak(self._nazivnik,self._brojnik)

#Zadatak 2.3

     @staticmethod
     def stvori(broj:float):
        stringBroja = str(broj)
        if not '.' in stringBroja:
            return 0
        else:
            brojDecimalnihMjesta = len(stringBroja) - stringBroja.index('.') - 1  #-1 radi tocke

            br = "1"
            for i in range (brojDecimalnihMjesta):
                br += "0"

            return Razlomak(broj * int(br), int(br))

print('*** test1 ***')
r1 = Razlomak(314,100)
r2 = Razlomak.inverz(r1)
print(r1,r2,r1)

print('*** test2 ***')
r1 = Razlomak.stvori(3.14)
print(r1)
r2 = Razlomak.stvori(0.006021)
print(r2)
r3 = Razlomak.stvori(-75.204)
print(r3)





