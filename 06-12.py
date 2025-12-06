def main():
    """DAY 6 :
        - We have to operate on various numbers given by multiples array of numbers. The last array, composed of operators is the operation we need to do on those numbers.
    """

    raw_input = []
    solution_part_one = 0
    solution_part_two = 0
    with open('./Énoncé/06-12.txt','r') as file :
        raw_input = file.read()

    # raw_input = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
    input_part_one = cleanInputPartOne(raw_input)
    input_part_two = cleanInputPartTwo(raw_input)
    
    

    nb_operations = len(input_part_one[0]) 
    nb_numbers = len(input_part_one)
    for current_operation in range(nb_operations) :
        pending_operation = []
        for i in range(nb_numbers) : 
            pending_operation.append(input_part_one[i][current_operation])
        
        result_part_one = doOperation(pending_operation)
        solution_part_one += result_part_one
    print(f"Solution part 1 : {solution_part_one}")

    for operation in range(len(input_part_two)-1):
        pending_operation = []
        for number in range(len(input_part_two[operation])):
            pending_operation.append(input_part_two[operation][number])
        pending_operation.append(input_part_two[-1][operation])
        result_part_two = doOperation(pending_operation)
        solution_part_two+= result_part_two
    
    print(f"Solution part 2 : {solution_part_two}")



def doOperation(operation:list)->int:
    '''
    Receive a list of str as an operation and return the result.
    
    :param operation: An operation in the form of ['number1','number2',...,'operator']
    :type operation: list
    :return: the results of the operation as asked in part one
    :rtype: int
    '''
    operator = operation.pop()
    result_part_one = 0
    match operator :
        case '*':
            result_part_one = 1
            for number in operation :
                result_part_one *= int(number)
        case '+':
            result_part_one = 0
            for number in operation :
                result_part_one += int(number)
        case _:
            'Operator not recognized...'
            return 0
    return result_part_one

def cleanInputPartTwo(raw_input:str)->list:
    '''
    Create a double array as [[numbers #1],[numbers2], ...,[operators]] and trim the output to only have numbers and operators.
    
    :param raw_input: the differents numbers and a line of operators separated by a '\\n'.
    :type raw_input: str
    :return: a list of lists of numbers and ended by a list of operators. ([[numbers #1],[numbers2], ...,[operators]])
    :rtype: list
    '''
    
    raw_input = raw_input.split('\n')
    input = []

    operator_and_size = raw_input.pop()
    
    widths = []; width = 1
    for key,char in enumerate(operator_and_size[1:]) :
        if char != ' ':
            widths.append(width)
            width=1
        elif key == len(operator_and_size[1:])-1:
            widths.append(width+2) # +1 because we check on len of the string. +1 because [x:] don't include second boundarie.
            width=1
        else :
            width+=1


    operators = []
    operator_and_size.split(' ')
    for operator in operator_and_size : 
        if operator != ' ': operators.append(operator)

    operators.reverse()
    
    for raw_line in raw_input :
        numbers=[]
        previous_width = 0
        for width in widths:
            if previous_width==0:
                number=raw_line[0:width-1]
            else:
                number=raw_line[previous_width:previous_width+width-1]
            numbers.append(number)
            previous_width+=width
        input.append(numbers)

    input=readingTopBottom(input)

    new_input =[]
    for line in input :
        new_line=[]
        for number in line : 
            new_number = number.replace(' ','')
            new_line.append(new_number)
        new_input.append(new_line)

    input = new_input.copy()
    input.append(operators)

    return input

def readingTopBottom(operation:list)->list:
    '''
    Read 1 digit from each number to compose the new number
    
    :param operation: a list of (str) numbers.
    :type operation: list
    :return: a list of newly composed (str) numbers
    :rtype: list
    '''
    new_operation = []
    #[['123', '328', ' 51', '64 '], [' 45', '64 ', '387', '23 '], ['  6', '98 ', '215', '314']]
    while operation[0]!=[]:
        numbers = []
        for line in operation : 
                numbers.append(line.pop())

        size_numbers = len(numbers[0])
        new_numbers = []
        for i in range(0,size_numbers): 
            new_number = ''
            new_digit = ''
            for i in range(0,len(numbers)) :
                
                if(numbers[i] != ''):
        
                    new_digit, numbers[i] = str(numbers[i][-1]), numbers[i][:-1]
                    new_number += str(new_digit)
        
                else:
                    continue
            new_numbers.append(new_number)
        new_operation.append(new_numbers)
    
    return new_operation

def cleanInputPartOne(raw_input:str)->list:
    '''
    Create a double array as [[numbers #1],[numbers2], ...,[operators]] and trim the output to only have numbers and operators.
    
    :param raw_input: the differents numbers and a line of operators separated by a '\n'.
    :type raw_input: str
    :return: a list of lists of numbers and ended by a list of operators. ([[numbers #1],[numbers2], ...,[operators]])
    :rtype: list
    '''
    
    raw_input = raw_input.split('\n')
    input = []
    for raw_line in raw_input :
        raw_line = raw_line.split(' ')
        trimmed_line = []
        for e in raw_line : 
            if e != '':
               trimmed_line.append(e)
        input.append(trimmed_line)
    return input

if __name__ == "__main__":
    main()