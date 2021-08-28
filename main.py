import pandas as pd

NG_FILENAME = "./testdata/naam_groepen.xlsx"
NN_FILENAME = "./testdata/naam_naam.xlsx"

class Leider:
    def __init__(self, name, groups):
        self.name = name
        self.groups = groups
        self.relations = []

    def newRelation(self, other, score):
        self.relations.append([other, score])

#Leider("Lode", [0, 1, 2, 3, 4, 5])


ng_df = pd.read_excel(NG_FILENAME)
ng_df = ng_df.to_numpy()

nn_df = pd.read_excel(NN_FILENAME)
nn_df = nn_df.to_numpy()

leidingsploeg = []

for persoon in ng_df:
    naam = persoon[0]
    groepen = []
    for i in range(0,6):
        groepen.append(persoon[i+1])
    leidingsploeg.append(Leider(naam, groepen))

for i in range(0, len(leidingsploeg)):
    for j in range(0, len(leidingsploeg)):
        leidingsploeg[i].newRelation(leidingsploeg[j], nn_df[i][j+1])

    #for relation in leidingsploeg[i].relations:
    #    print(f"{leidingsploeg[i].name} --> {relation[0].name}: {relation[1]}")