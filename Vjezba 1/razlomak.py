#Zadatak 1.1

class Razlomak(object):

    def __init__(self, brojnik, nazivnik):
        self.__brojnik = int(brojnik)
        self.__nazivnik = int(nazivnik)
        

    @property
    def brojnik(self):
        return self.__brojnik

    @property
    def nazivnik(self):
        return self.__nazivnik

    @brojnik.setter
    def brojnik(self, vrijednost):
        self.__brojnik = vrijednost

    @nazivnik.setter
    def nazivnik(self, vrijednost):
        self.__nazivnik = vrijednost



   #SKRATI 

    @property
    def skrati(self):
        nd = None

        if(self.brojnik <= self.nazivnik):
            manjibroj = self.brojnik
        else:
            manjibroj = self.nazivnik

        for i in range(2, int(manjibroj + 1)):
          if (self.brojnik % i == 0 and self.nazivnik % i == 0):
            nd = i

        if (nd == None):
           print("Ne moze se skratit.")

        else:
          self.nazivnik //= nd
          self.brojnik //= nd
          
#Zadatak 1.2
          
    def __repr__(self):
        return "Razlomak(" + repr(self.__brojnik) + ", " + repr(self.__nazivnik) + ")"

    def __str__(self):
        return str(self.brojnik) + "|" + str(self.nazivnik)


    def __eq__(self,other):
         return (self.brojnik/self.nazivnik) == (other.brojnik/other.nazivnik)
    
    def __ge__(self,other):
        return (self.brojnik/self.nazivnik) >= (other.brojnik/other.nazivnik)

    def __lt__(self,other):
        return (self.brojnik/self.nazivnik) < (other.brojnik/other.nazivnik)


#Zadatak 1.3


    def __add__(self,other):
        brojnik1 = (self.brojnik * other.nazivnik) + (other.brojnik * self.nazivnik)
        nazivnik1 = self.nazivnik * other.nazivnik

        return str(Razlomak(brojnik1,nazivnik1))
                    
    def __sub__(self,other):
        brojnik1 = (self.brojnik * other.nazivnik) - (other.brojnik * self.nazivnik)
        nazivnik1 = self.nazivnik*other.nazivnik

        return str(Razlomak(brojnik1,nazivnik1))
                    
    def __mul__(self,other):
        brojnik = self.brojnik * other.brojnik
        nazivnik = self.nazivnik * other.nazivnik

        return str(Razlomak(brojnik, nazivnik))
        
    def __truediv__(self,other):
        brojnik = self.brojnik * other.nazivnik
        nazivnik = self.nazivnik * other.brojnik

        return str(Razlomak(brojnik, nazivnik))

print('*** test 1 ***')
r1 = Razlomak(12, 30)
print(r1.brojnik, r1.nazivnik)
r1.skrati
print(r1.brojnik, r1.nazivnik)

print('*** test 2 ***')
r1 = Razlomak(12, 30)
r2 = Razlomak(2, 5)
r3 = Razlomak(3, 6)
print(r1, r2, repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(3,4)+Razlomak(5,2))
print(Razlomak(1,3)-Razlomak(2,6))
print(Razlomak(2,8)*Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))





