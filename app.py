import pandas as pd

FILENAME = './testdata/Leidingsvorming .xlsx'

class Leiding:
    def __init__(self, index, naam, relaties, groepen, eigenVoorkeur):
        self.index = index
        self.naam = naam
        # fix nog de twijfelaars : antwoorden als '4/1' enzo
        self.relaties = relaties # de scores die zij gaven aan anderen?
        self.groepen = groepen
        self.eigenVoorkeur = eigenVoorkeur

    # relaties
    def relatiesAlsArray(self):
        relaties = []

        for item in self.relaties: 
            relaties.append(item)

        return relaties

    def relatieMetIndex(self, index):
        return self.relaties.iloc[index]
    
    def relatiesMetScore(self, score):
        relaties = []

        for i in range(len(self.relaties)):
            if (self.relaties.iloc[i] == score):
                relaties.append((i, score))

        return relaties
            

    # groepen
    def groepenAlsArray(self):
        groepen = []

        for item in self.groepen:
            groepen.append(item)

        return groepen

    def groepMetIndex(self, index):
        return self.groepen.iloc[index]

    def groepMetScore(self, score):
        groepen = []

        for i in range(len(self.groepen)):
            if (self.groepen.iloc[i] == score):
                groepen.append((i, score))

        return groepen


class Leidingsploeg:
    def __init__(self):
        self.leiding = []
        self.leidingDict = {}
        self.groepNamen = {
            'Speelclub': 0,
            'Pimpel': 1,
            'Rakwi': 2,
            'Tito': 3,
            'Keti': 4,
            'Aspi': 5
        }
        self.groepen = []

        self._maakLeidingsploeg()
        self._maakLeidingDict()

    def _nieuweLeiding(self, i, p, g, ev):
        naam = p.iloc[i].iloc[0] # naam van persoon is het eerste item uit de rij met de index van de persoon
        relaties = p.iloc[i].iloc[1:] # de relaties is alles behalve dat eerste item
        groepen = g.iloc[i].iloc[1:] # de scores voor groepen beginnen ook eerst met de naam, score voor groepen is dus alles na de eerste cell
        eigenVoorkeur = ev.iloc[i].iloc[1:] # zie hierboven

        return Leiding(i, naam, relaties, groepen, eigenVoorkeur) # return het leiding object

    def _maakLeidingsploeg(self):
        xls = pd.ExcelFile(FILENAME) # open de file
        personen = pd.read_excel(xls, 0) # lees de eerste (index 0) sheet (das dus die met personen normaal)
        groepen = pd.read_excel(xls, 1) # lees de tweede (index 1) sheet (das die met de groepen normaal)
        eigenVoorkeur = pd.read_excel(xls, 2) # lees de derde (index 2) sheet (das die met de eigen voorkeur van leidingsploegje)

        for i in range(0, personen.index.stop):
            self.leiding.append(self._nieuweLeiding(i, personen, groepen, eigenVoorkeur)) # voeg elke leiding toe aan de array met alle leiding

    def _maakLeidingDict(self):
        leidingList = [] # maak de array voor de namen (nog wel leeg)
        indexList = list(range(len(self.leiding))) # maak de array met indexen (al wel gevult)

        for i in self.leiding: # vul de array met namen
            leidingList.append(i.naam)

        self.leidingDict = dict(zip(leidingList, indexList)) # voeg indexen toe aan de namen met de namen als key

class LeidingsGroep(): # Class voor elke groep makkelijk te kunnen aanspreken
    def __init__(self, index, naam):
        self.index = index
        self.naam = naam
        self.score = 0
        self.leiding = []

def test():
    xls = pd.ExcelFile(FILENAME)
    personen = pd.read_excel(xls, 0)
    groepen = pd.read_excel(xls, 1)
    eigenVoorkeur = pd.read_excel(xls, 2)

    namen = []; # voor elke naam in de personen lijst, voeg hier iemand toe in die volgorde

    print(personen)
    print(type(personen))

    print('\n=============================\n')

    print(personen.index)
    print(personen.index.stop)
    print(personen.columns)
    print(type(personen.columns))
    print(personen.keys())

    print('\n=============================\n')

    for i in range(0, personen.index.stop):
        #print(personen[i])
        print(type(personen.iloc[i])) # pandas.core.series.series object van gegeven scores aan personen
        print(personen.iloc[i].iloc[0]) # naam van persoon
        print(personen.iloc[i].iloc[1:]) 
        print(personen.iloc[i].iloc[3]) # waarde van persoon 3 (eerste persoon zit op index 1)

        print(groepen.iloc[i])

        print('\n=============================\n')

def main():
    L = Leidingsploeg()
    print(L.leiding[L.leidingDict["Lode"]].relatiesAlsArray())

if __name__ == '__main__':
    main()