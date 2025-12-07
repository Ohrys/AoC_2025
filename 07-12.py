
def main() : 
    '''DAY 7:
        - A Tachyon is generated and split against splitter in two tachyon. How many tachyron reach the end. 
        - When a Tachyon is splitted it generate an alternative timeline. How many timeline exists at the end. 
    '''

    #TODO :
    # - Generate a Tachyon.
    # - Check y+1 to see if it's a splitter '^' or an empty space '.'
    #   - if it's a splitter '^' : generate a Tachyon in the direct left (x-1) and right (x+1)
    #       - if there's already a Tachyon present, ignore FOR NOW (I kinda guess i'll need to take account for it.)
    #         PART 2 : If there's a Tachyon present, add the value of the tachyon coming and the one already there together.
    #       - count that as a split (Solution part one)
    #   - if it's an empty space '.' : rewrote the Tachyon (it continues.)


    global Y_MAX     
    global X_MAX
    global solution_part_two
    global input
    with open('./Énoncé/07-12.txt', 'r') as file :
    # with open('./Énoncé/Sample-07-12.txt','r') as file :
        input_str = file.readlines()


    input = []
    solution_part_one = 0
    solution_part_two = 0

    for line in input_str : 
        input_str = line.replace('\n','');
        input.append(list(input_str))

    
    Y_MAX = len(input)    
    X_MAX = len(input[0])

    for y in range(0,Y_MAX):
        for x in range(0,X_MAX):
            input[y][x]=(input[y][x],0)

    for y in range(0, Y_MAX) : 
        for x in range(0, X_MAX) :
            if(input[y][x][0] == 'S') :
                generateTachyon(x, y, 'S')
            elif(input[y][x][0] == '^') :
                if input[y-1][x][0] == '|' :
                    solution_part_one += 1
                    generateTachyon(x, y, '^')
            elif(input[y][x][0] == '|') :
                generateTachyon(x,y)
        # print_line_matrice(y) (to check by line)
    print_matrice()

    for x in range(0,X_MAX):
        solution_part_two+=input[-1][x][1]
    
    print(f'Solution part one : {solution_part_one}')
    print(f'Solution part two : {solution_part_two}')
            

                
def generateTachyon(x:int, y:int, symbol='|')->None:
    '''
        Generate a Tachyon on the line y+1 if y < Y_MAX.
    
    :param x: position X where the function was called.
    :type x: int
    :param y: position Y where the function was called.
    :type y: int
    :param input: the input we need to modify at input[y+1].
    :type input: list
    '''

    global solution_part_two
    global input
    
    match symbol :
        case 'S':
            if(x < X_MAX and y < Y_MAX) :
                if(input[y+1][x][0] == '.') :
                    input[y+1][x] = ('|',1)

        case '^':
            if( x < X_MAX and y < Y_MAX):
                # if there's a tachion or not, we add the value to the value of the position where it'll be created.
                input[y][x-1] = ('|', input[y-1][x][1]+input[y][x-1][1])
                # since we're editing a position already checked (x-1), we call back generate to follow that Tachyon too.
                generateTachyon(x-1,y)
                input[y][x+1] = ('|', input[y-1][x][1]+input[y][x+1][1])
            
            
        case '|':
            if(x < X_MAX and y < Y_MAX-1) :
                if(input[y+1][x][0] == '.') :
                    input[y+1][x] = ('|',input[y][x][1])
                elif(input[y+1][x][0] == '|'):
                    # since in the case of a splitter we add the value already present and the value coming
                    # we don't need to add the value there even if there was something there. 
                    input[y+1][x] = ('|',input[y][x][1])




def print_cell(x, y,end="\n"):
    global input
    print(input[y][x],end=end)

def print_line_matrice(y):
    global input
    counter = 0
    for x in range(0, X_MAX):
        print(str(input[y][x][0]), end='')
        counter += input[y][x][1]
    print('\t\t\t', end='')

    # To see the cumulative value of each tachyon per line.
    print(counter, end='')
    
    # To see value of each tachyon
    # for x in range(0, X_MAX):
    #     if(input[y][x][1]==0) : print(input[y][x][0],end='')
    #     else : print(str(input[y][x][1]), end='')
    print()


def print_matrice():
    for y in range(0, Y_MAX):
        print_line_matrice(y)

if __name__ == "__main__" : 
    main()