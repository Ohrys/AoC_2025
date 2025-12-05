def main() :
    """DAY 5 :
        - Find in a list of ID tranches, all the ID that are inclusive to a range. 
        - Return the number of IDs that satisfy that conditions.
    """

    input = []
    solution_part_one = 0
    solution_part_two = 0

    with open('./Énoncé/05-12.txt', 'r') as file : 
        enonce = file.readlines()

    for line in enonce : 
        line = line.strip('\n')
        input.append(line)

    # input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32".split('\n')


    separator = input.index('')
    ranges_str = input[:separator]
    ids_str = input[separator+1:]

    ranges = []
    for range in ranges_str : 
        tuple1, tuple2 = range.split("-")
        if(tuple1<=tuple2):
            ranges.append((int(tuple1), int(tuple2)))
        elif(tuple2<tuple1):
            ranges.append((int(tuple2), int(tuple1)))


    id_in_range = False
    ids_valid_part_one = []
    for id_str in ids_str : 
        id = int(id_str)

        for range in ranges :
            lower_bound = getLowerBounds(range)
            higher_bound = getHigherBounds(range)
            if id >= lower_bound and id <= higher_bound : 
                id_in_range = True
                break
        
        if id_in_range :
            ids_valid_part_one.append(id_str)
        id_in_range = False

    solution_part_one = len(ids_valid_part_one)
    print(f"Solution Part One : {solution_part_one}")

    # --- IF YOU WANT TO HAVE FUN ... I NEVER ENDED THE EXECUTION OF THAT SOLUTION. 
    # ids_part_two = []
    # print("Creating all the IDs ...")
    # for r in tranches : 
    #     lower_bound = int(r[0])
    #     higher_bound = int(r[1])
    #     for i in range(lower_bound, higher_bound+1):
    #         ids_part_two.append(i)
    # print("COMPLETED.")
    # print("Triming unique values ...")
    # ids_valid_part_two = list(set(ids_part_two))
    # print("COMPLETED.")
    # solution_part_two = len(ids_valid_part_two)
    # print(f"Solution Part Two : {solution_part_two}")

    
    new_ranges = fuseRanges(ranges)


    for range in new_ranges : 
        solution_part_two += getHigherBounds(range) - getLowerBounds(range) + 1
    print(f'Solution Part Two : {solution_part_two}')


def fuseRanges(ranges:list)->list:
    
    old_ranges = []
    new_ranges = ranges
    while old_ranges != new_ranges :
        new_ranges.sort(key=getLowerBounds)
        old_ranges = new_ranges.copy()
        
        for i in range(len(new_ranges)-1):
            if getHigherBounds(new_ranges[i]) >= getLowerBounds(new_ranges[i+1])-1:
                if getHigherBounds(new_ranges[i]) >= getHigherBounds(new_ranges[i+1]):
                    del(new_ranges[i+1])
                    break
                else :
                    new_ranges[i] = (getLowerBounds(new_ranges[i]), getHigherBounds(new_ranges[i+1]))
                    del(new_ranges[i+1])
                    break
            else:
                continue
    
    return new_ranges


def getLowerBounds(e)->int : 
    return int(e[0])


def getHigherBounds(e)->int : 
    return int(e[1])
        



if __name__ == "__main__":
    main()