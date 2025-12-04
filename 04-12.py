def main():
    '''DAY 4 : 
        - Find when a roll '@' in a map is surrounded by less than X others rolls. 
            If so, he's movable. (and counted as so)
        - If it's movable, move it. Check the new map to see if new rolls move. 
            Do so until no more rolls move (each rolls moveable is counted)
    '''
    input1 = []
    input2 = []
    solution_part_one = 0
    solution_part_two = 0
    with open('./Énoncé/04-12.txt', 'r') as file : 
        f = file.readlines()
    # f = "..@@.@@@@.\n"+"@@@.@.@.@@\n"+"@@@@@.@.@@\n"+"@.@@@@..@.\n"+"@@.@@@@.@@\n"+".@@@@@@@.@\n"+".@.@.@.@@@\n"+"@.@@@.@@@@\n"+".@@@@@@@@.\n"+"@.@.@@@.@."
    # f= f.split('\n')

    for line in f :
        line = line.strip('\n')
        input1.append(list(line))
        input2.append(list(line))


    for i in range(0,len(input1)) :
        for j in range(0,len(input1[0])) :
            if isEmptyAround(input1, i, j, 4):
                input1[i][j] = 'x'
                solution_part_one +=1

    previous_step = -1
    while previous_step <= solution_part_two : 
        for i in range(0,len(input2)) :
            for j in range(0,len(input2[0])) :
                if isEmptyAround(input2, i, j, 4):
                    input2[i][j] = 'x'
                    solution_part_two +=1
        

        if(solution_part_two==previous_step):
            previous_step+=1
        else:
            for i in range(0,len(input2)) :
                for j in range(0,len(input2[0])) :
                    if input2[i][j] == 'x' :
                        input2[i][j] = '.'
            previous_step = solution_part_two 

    print(f"Solution N°1 : {solution_part_one}")
    print(f"Solution N°2 : {solution_part_two}")

            



def isEmptyAround(map:list, x, y, thresold=0)->bool :
    '''TODO
        - check from given position each character around in the provided array and if below thresold return true.
    '''
    thresoldEmptyAround = 0
    if map[x][y]=='.' or map[x][y]=='x':
        return False
    for i in range(x-1, x+2):
        if i<0:
            next
        elif i>=len(map):
            next
        else:
            for j in range(y-1, y+2):
                if i == x and j == y : 
                    next
                elif j<0 :
                    next
                elif j>=len(map[0]):
                    next
                else:
                    if map[i][j] != '.':
                        thresoldEmptyAround+=1

    return thresoldEmptyAround < thresold

if __name__ == "__main__":
    main()