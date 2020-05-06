#Zadatak 6.1

import json
import sqlite3

class Ispiti(dict):

      def dodaj(self, student, kolegij, ocjena):
         if student not in self:
             self[student] = {}
         self[student][kolegij] = ocjena

      def izbrisi(self, student, kolegij):
          if kolegij in self[student]:
               self[student].pop(kolegij)

      def promijeni(self, student, kolegij, ocjena):
           self[student][kolegij] = ocjena


      def spremi_datoteku(self,naziv_dat):
        with open(naziv_dat, "w") as d :
            for student , kolegiji_dict in self.items():
                for kolegiji,ocjena in kolegiji_dict.items():
                    d.write("%s \t %s \t %s \n" %(student,kolegiji, str(ocjena)))

      @staticmethod
      def ucitaj_datoteku(naziv_dat):
        isp = Ispiti()
        with open(naziv_dat, "r") as d:
            for line in d.readlines():
                 student= (line.splitlines()[0]).split("\t")
                 isp.dodaj(student[0],student[1],student[2])
            return isp
#Zadatak 6.2
      def spremi_json(self, naziv_dat):
        with open(naziv_dat, "w") as d:
            json.dump(self,d)

      @staticmethod
      def ucitaj_json(naziv_dat):
        with open(naziv_dat) as d:
            student = json.load(d)
            return student


print("*** TEST datoteka ***")
isp = Ispiti()
isp.dodaj("Ante Antic", "Linearna algebra", 5)
isp.dodaj("Ante Antic", "Programiranje 1 ", 4)
isp.dodaj("MArija Marijic", "Linearna algebra", 4)
isp.dodaj("MArija Marijic", "Matematicka analiza", 5)
isp.spremi_datoteku("ispiti.txt")
print(open("ispiti.txt").read())
isp = Ispiti.ucitaj_datoteku("ispiti.txt")
print(isp)


print("*** TEST json ***")
isp = Ispiti()
isp.dodaj("Ante Antic", "Linearna algebra", 5)
isp.dodaj("Ante Antic", "Programiranje 1", 4)
isp.dodaj("Ante Antic", "Linearna algebra", 4)
isp.dodaj("Ante Antic", "Matematica analiza", 5)
isp.spremi_json("ispiti.json")
print(open("ispiti.json").read())
isp = Ispiti.ucitaj_json("ispiti.json")
print(isp)
