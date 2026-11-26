class Etudiant:
    def __init__(self, nom, prenom, matricule):
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule

    def afficher(self):
        print(f"{self.nom} {self.prenom} - {self.matricule}")


class GestionEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def supprimer_etudiant(self, matricule):
        self.etudiants = [
            e for e in self.etudiants
            if e.matricule != matricule
        ]

    def afficher_etudiants(self):
        for etudiant in self.etudiants:
            etudiant.afficher()