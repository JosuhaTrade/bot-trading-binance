from tkinter import *
from interface_graphique import *
#from simulation import *


def executer_simulation():
    # Récupération des paramètres de la simulation depuis l'interface graphique
    periode = int(periode_entry.get())
    stop_loss = float(stop_loss_entry.get())
    take_profit = float(take_profit_entry.get())
    montant = float(montant_entry.get())
    taux_marge = float(taux_marge_entry.get())

    # Lancement de la simulation
    resultats = simuler_marche(periode, stop_loss, take_profit, montant, taux_marge)

    # Affichage des résultats de la simulation dans l'interface graphique
    afficher_resultats(resultats)


# Création de la fenêtre principale de l'interface graphique
root = Tk()
root.title("Simulateur de trading")

# Création des labels et des champs de saisie pour les paramètres de la simulation
periode_label = Label(root, text="Période (en heures) : ")
periode_label.grid(row=0, column=0)
periode_entry = Entry(root)
periode_entry.insert(0, "24")
periode_entry.grid(row=0, column=1)

stop_loss_label = Label(root, text="Stop loss : ")
stop_loss_label.grid(row=1, column=0)
stop_loss_entry = Entry(root)
stop_loss_entry.insert(0, "0.05")
stop_loss_entry.grid(row=1, column=1)

take_profit_label = Label(root, text="Take profit : ")
take_profit_label.grid(row=2, column=0)
take_profit_entry = Entry(root)
take_profit_entry.insert(0, "0.1")
take_profit_entry.grid(row=2, column=1)

montant_label = Label(root, text="Montant initial : ")
montant_label.grid(row=3, column=0)
montant_entry = Entry(root)
montant_entry.insert(0, "1000")
montant_entry.grid(row=3, column=1)

taux_marge_label = Label(root, text="Taux de marge : ")
taux_marge_label.grid(row=4, column=0)
taux_marge_entry = Entry(root)
taux_marge_entry.insert(0, "10")
taux_marge_entry.grid(row=4, column=1)

# Création du bouton pour lancer la simulation
executer_button = Button(root, text="Exécuter la simulation", command=executer_simulation)
executer_button.grid(row=5, column=0, columnspan=2)

# Création du label pour afficher les résultats de la simulation
resultats_label = Label(root, text="")
resultats_label.grid(row=6, column=0, columnspan=2)

# Lancement de la boucle principale de l'interface graphique
root.mainloop()
