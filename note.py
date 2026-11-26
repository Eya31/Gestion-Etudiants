class Note:
    def __init__(self, matiere, valeur):
        self.matiere = matiere
        self.valeur = valeur

    def afficher(self):
        print(f"{self.matiere} : {self.valeur}")


class GestionNotes:
    def __init__(self):
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def afficher_notes(self):
        for note in self.notes:
            note.afficher()

    def calculer_moyenne(self):
        if not self.notes:
            return 0

        return sum(n.valeur for n in self.notes) / len(self.notes)