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
        
        '''for every element of the grid, check if a roll is considered moveable. 
            if it is, replace the "@" by "x" and add it to the counter of solution 2'''
        for i in range(0,len(input2)) :
            for j in range(0,len(input2[0])) :
                if isEmptyAround(input2, i, j, 4):
                    input2[i][j] = 'x'
                    solution_part_two +=1
        
        '''if the counter is different than the last iteration's counter of moveable object,
            change the 'x' by a dot a redo an iteration as a last check.
            if not, then we leave the loop. We got our solution 2. '''
        if(solution_part_two != previous_step):
            for i in range(0,len(input2)) :
                for j in range(0,len(input2[0])) :
                    if input2[i][j] == 'x' :
                        input2[i][j] = '.'
            previous_step = solution_part_two 
        else:
            previous_step+=1
            
    print(f"Solution N°1 : {solution_part_one}")
    print(f"Solution N°2 : {solution_part_two}")

            



def isEmptyAround(map:list, x, y, thresold=0)->bool :
    # a case is surrounded by the position (1-9) as : 
    # 1 2 3
    # 4 X 6
    # 7 8 9

    thresoldEmptyAround = 0
    if map[x][y]=='.' or map[x][y]=='x': # the current position(x,y) is not a @, so we don't need to check it.
        return False
    
    for i in range(x-1, x+2):
        if i<0: # that means we're on the first line of the grid (ignoring position 1,2,3)
            next
        elif i>=len(map): # that means we're on the last line of the grid. (ignoring position 7,8,9)
            next
        else:
            for j in range(y-1, y+2):
                if i == x and j == y : # we don't have to check ourselves. 
                    next
                elif j<0 : # we are on the first column (ignoring check position 1,4,7)
                    next
                elif j>=len(map[0]): # we are on the last column (ignoring check position 3,6,9)
                    next
                else:
                    if map[i][j] != '.':
                        thresoldEmptyAround+=1

    return thresoldEmptyAround < thresold

if __name__ == "__main__":
    main()