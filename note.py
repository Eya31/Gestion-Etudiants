class Note:
    def __init__(self, matiere, valeur):
        self.matiere = matiere
        self.valeur = valeur

    def afficher(self):
        print(f"Matière : {self.matiere}")
        print(f"Note : {self.valeur}")