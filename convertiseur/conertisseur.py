# Ce dictionnaire donne la valeur de 1 euro dans chaque devise
taux = {
    # 1 euro vaut 1 euro
    "EUR": 1,
    # 1 euro vaut 655,957 FCFA (taux fixe officiel)
    "XAF": 655.957,
    # 1 euro vaut environ 1,15 dollar (EXEMPLE à mettre à jour)
    "USD": 1.15,
    # 1 euro vaut environ 0,87 livre sterling (EXEMPLE à mettre à jour)
    "GBP": 0.87,
# L'accolade fermante termine le dictionnaire
}

# Fonction qui convertit un montant d'une devise vers une autre
def convertir(montant, devise_depart, devise_arrivee):
    # On convertit d'abord le montant en euros
    montant_en_euros = montant / taux[devise_depart]
    # Puis on convertit ces euros dans la devise d'arrivée
    resultat = montant_en_euros * taux[devise_arrivee]
    # On renvoie le résultat arrondi à 2 chiffres après la virgule
    return round(resultat, 2)

# On demande le montant à convertir
reponse = input("Montant : ")
# On transforme le texte tapé en nombre à virgule
montant = float(reponse)
# On demande la devise de départ
devise_depart = input("Devise de départ (EUR, XAF, USD, GBP) : ")
# On demande la devise d'arrivée
devise_arrivee = input("Devise d'arrivée (EUR, XAF, USD, GBP) : ")
# On appelle la fonction avec les trois informations et on garde le résultat
resultat = convertir(montant, devise_depart, devise_arrivee)
# On affiche le résultat
print(montant, devise_depart, "=", resultat, devise_arrivee)