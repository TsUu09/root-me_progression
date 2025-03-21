import os
from datetime import datetime

# Chemin du fichier Markdown
FICHIER_MARKDOWN = "Progression.md"

# 📌 Fonction pour ajouter un challenge
def ajouter_challenge(categorie, challenge, statut, note):
    # 📅 Récupérer la date du jour
    date_aujourd_hui = datetime.today().strftime("%Y-%m-%d")
    
    # 📂 Vérifier si le fichier existe
    if not os.path.exists(FICHIER_MARKDOWN):
        print(f"⚠️ Le fichier {FICHIER_MARKDOWN} n'existe pas. Création en cours...")
        with open(FICHIER_MARKDOWN, "w", encoding="utf-8") as f:
            f.write("# 🚀 Suivi de ma progression Root-Me\n\n")
            f.write("## 📊 Progression des Challenges\n\n")
            f.write("| Date       | Catégorie       | Challenge         | Statut     | Notes / Apprentissage |\n")
            f.write("|------------|----------------|-------------------|------------|------------------------|\n")

    # 📌 Lire le fichier et trouver où insérer la nouvelle ligne
    with open(FICHIER_MARKDOWN, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    index_table = next((i for i, ligne in enumerate(lignes) if "| Date" in ligne), None)

    if index_table is None:
        print("❌ Impossible de trouver la table des challenges. Vérifie le format du fichier.")
        return

    # 📌 Construire la ligne à ajouter
    nouvelle_ligne = f"| {date_aujourd_hui} | {categorie} | {challenge} | {statut} | {note} |\n"

    # 📌 Insérer après l'en-tête du tableau
    lignes.insert(index_table + 2, nouvelle_ligne)

    # 📌 Réécrire le fichier avec la nouvelle entrée
    with open(FICHIER_MARKDOWN, "w", encoding="utf-8") as f:
        f.writelines(lignes)

    print(f"✅ Challenge '{challenge}' ajouté avec succès !")

# 🏁 Exemple d'utilisation
if __name__ == "__main__":
    categorie = input("Catégorie : ")
    challenge = input("Nom du challenge : ")
    statut = input("Statut (✅ Terminé / 🔄 En cours / ⏳ À faire) : ")
    note = input("Note ou commentaire : ")

    ajouter_challenge(categorie, challenge, statut, note)

