
def main() : 
    '''DAY 7:
        - 
    '''

    #TODO :
    # - Generate a Tachyon.
    # - Check y+1 to see if it's a splitter '^' or an empty space '.'
    #   - if it's a splitter '^' : generate a Tachyon in the direct left (x-1) and right (x+1)
    #       - if there's already a Tachyon present, ignore FOR NOW (I kinda guess i'll need to take account for it.)
    #       - count that as a split (Solution part one)
    #   - if it's an empty space '.' : rewrote the Tachyon (it continues.)


    global Y_MAX     
    global X_MAX
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

    for y in range(0, Y_MAX) : 
        for x in range(0, X_MAX) :
            if(input[y][x] == 'S') :
                generateTachyon(x, y, input, 'S')
            elif(input[y][x] == '^') :
                if input[y-1][x] == '|' :
                    solution_part_one += 1
                    print(f'Solution n°1:{solution_part_one} @ : x:{x} / y:{y}')
                    generateTachyon(x,y,input,'^')
            elif(input[y][x] == '|') :
                generateTachyon(x,y,input)
    print_matrice(input)
    print(f'Solution part one : {solution_part_one}')
            

                
def generateTachyon(x:int, y:int, input:list, symbol='|')->None:
    '''
        Generate a Tachyon on the line y+1 if y < Y_MAX.
    
    :param x: position X where the function was called.
    :type x: int
    :param y: position Y where the function was called.
    :type y: int
    :param input: the input we need to modify at input[y+1].
    :type input: list
    '''
    match symbol :
        case '.':
            if(x < X_MAX and y < Y_MAX) :
                if (input[y+1][x] == '.') :
                    input[y+1][x] = '|'
                else :
                    print(f"There's something below x:{x}, y:{y} (@: x:{x}, y:{y+1})")
            else : 
                print("or it's the end of the line")
        case 'S':
            if(x < X_MAX and y < Y_MAX) :
                if(input[y+1][x] == '.') :
                    input[y+1][x] = '|'
                # else : print(f"There's something below x:{x}, y:{y} (@: x:{x}, y:{y+1})")
            # else : print("or it's the end of the line")
        case '^':
            if(x>0):
                if(input[y][x-1] == '.') :
                    input[y][x-1] = '|'
                    generateTachyon(x-1,y,input)
                # elif input[y][x-1] == '|':  print("There's a Tachyon already, here.")
            if(x<X_MAX-1):
                if(input[y][x+1] == '.') :
                    input[y][x+1] = '|'
                # elif input[y][x+1] == '|': print("There's a Tachyon already, here.")
                
            
        case '|':
            if(x < X_MAX and y < Y_MAX-1) :
                if(input[y+1][x] == '.') :
                    input[y+1][x] = '|'
                # else : print(f"There's something below x:{x}, y:{y} (@: x:{x}, y:{y+1})")
            # else : print("it's the end of the line")
        # case _: print('Your Tachyon board need some cleaning, something is in the way.')


    

def print_matrice(input):
    for y in range(0, Y_MAX):
        for x in range(0, X_MAX):
            print(str(input[y][x]),end='')
        print('')

if __name__ == "__main__" : 
    main()