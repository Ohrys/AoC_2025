def main():
    ''' Jour 1 :
    - Nous avons des cadrans de 0 à 99
    - Les cadrans commencent à 50. 
    - Si une instructions vaut LX on tourne dans le sens anti-horaire 3 fois.
    50 donnera donc : L3 = 47. 
    - Si une intructions vaut RX on tourne dans le sens horaire.
    50 donnera donc : R4 = 54.
    - Si cadrans vaut 0 et L1 on passe à 99.
    - Si cadran vaut 99 et R1 on passe à 0. 
    '''


    with open('./Énoncé/01-12.txt', 'r') as f:
       enonce = f.readlines()

    # enonce = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    valeur = 50
    solution = 0
    solution_deux = 0

    # On transforme l'énoncé en liste de tuples de la forme (L/R, valeur)
    for i, ligne in enumerate(enonce) :
        ligne = ligne.replace("\n","")
        enonce[i] = (ligne[0],int(ligne[1:]))

    # on soustrait dans le sens horaire (L) ou on additionne dans le sens anti-horaire (R) les valeurs de l'énoncé modulo 100 pour les valeurs hors intervalle.
    for sens, valeur_enonce in enonce :
        if sens == "L" : 
            if valeur == 0 :
                valeur = 100 # Pour éviter de recompter le 0, on réajuste la valeur pour la soustraction. 
            valeur = valeur - (valeur_enonce%100)     
            solution_deux += valeur_enonce//100 # Compte le nombre de tour par zéro
        else :
            if valeur == 100 :
                 valeur = 0 # Pour éviter de recompter le 100, on réajuste la valeur pour l'addition.  
            valeur = valeur + (valeur_enonce%100)
            solution_deux += valeur_enonce//100 # Compte le nombre de tour par zéro

        if valeur <= 0 : 
            if valeur < 0 : 
                 valeur = 100 - abs(valeur)
                 solution_deux +=1
            else : 
                 solution+=1

        elif valeur >= 100 : 
            if valeur > 100 : 
                 valeur = abs(valeur)-100
                 solution_deux +=1
            else : 
                 solution+=1 

    solution_deux = solution_deux + solution
    print(solution, solution_deux)
    
    

if __name__ == "__main__" :
        main()