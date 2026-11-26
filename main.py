from etudiant import Etudiant
from note import Note

def afficher_message():
    print("Bienvenue dans la gestion des étudiants et des notes")

etudiant1 = Etudiant("Ali", "Ahmed", "E001")
note1 = Note("Python", 16)

afficher_message()

etudiant1.afficher()
note1.afficher()