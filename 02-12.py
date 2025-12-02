def main() :
    """Jour 2 :
        - nous avons une liste de range d'ID valides (numériques)
        - un ID invalide est un ID possédant des zéros précédent le nombre (e.g : 0101)
        - Un ID contenant _uniquement_ une suite doublé de nombre : (e.g : 11, 2020, 185185)

        - Un ID valide peut être toutes autres valeurs (e.g : 18185, 1234, 12, 10)
        
        --- PART 2 ---
        - Un ID Invalide est un ID possédant _uniquement_ une suite se répétant au moins 2 fois : (eg. 123123123 (3*123), 1111111 (7*1))

        => Trouvez les valeurs d'ID invalides, la solution est la somme des ID invalides de la liste.

    """ 
    # TODO :
    #   - 1. Définir le problème ✅
    #   - 2. Prendre exemple énoncé. ✅
    #   - 3. Isoler les valeurs invalides. ✅ 
    #   - 4. Utiliser Input du challenge. ✅

    with open("./Énoncé/02-12.txt", 'r') as file :
        enonce = file.read()

    # enonce = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    solution_part_one = 0
    solution_part_two = 0

    enonce = enonce.split(",")
    ranges = []
    for r in enonce :
        tuple1, tuple2 = r.split("-")
        ranges.append((int(tuple1), int(tuple2)))
    
    
    for r in ranges :
        tuple1 = r[0]
        tuple2 = r[1]
        my_range = range(tuple1, tuple2+1, 1)
        for id in my_range :
            if isInvalidPartOne(id) : 
                solution_part_one += id
            elif isInvalidPartTwo(id) :
                solution_part_two += id
    print(f"Solution n°1 : {solution_part_one}")
    print(f"Solution n°2 : {solution_part_one + solution_part_two}")


def isInvalidPartOne(id) -> bool:
    """
        On s'assure que la taille de l'ID est divisible par 2.
        - Si oui :
            on stocke le "milieu" de l'ID et on compare la première partie à la deuxième partie. Si égal, l'ID est invalide.
    """
    str_id = str(id)
    if len(str_id)%2 == 0 :
        mid_length = int(len(str_id)/2)
        return str_id[:mid_length] == str_id[mid_length:]

def isInvalidPartTwo(id) -> bool:
    """
        - On decoupe l'id en des morceaux de 1 jusqu'à des morceaux faisant la taille de l'ID.
            - Pour chaque morceaux, on vérifie que sa taille découpe de façon ENTIÈRE l'ID. 
                - Si oui :
                    On stocke le nombre de découpage_entier effectué. On le compare ensuite au résultat de str.count() de la substring de ce découpage sur l'ID. 
                    La valeur est pertinente que si le découpage entier n'est pas de la taille de l'ID (decoupage_entier > 1)
                - Si non : 
                    On passe au découpage suivant. 
    """
    str_id = str(id) 
    result = False
    for decoupage in range(1,len(str_id)+1,1) :
        if len(str_id)%decoupage == 0 :
            decoupage_entier = int(len(str_id)/decoupage)
            result = (str_id.count(str_id[:decoupage]) == decoupage_entier) and (decoupage_entier > 1) or result
    return result
            
if __name__ == "__main__" :
    main()