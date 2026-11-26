class Etudiant:
    def __init__(self, nom, prenom, matricule):
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Matricule : {self.matricule}")