def main() : 
    """DAY 3 :
        - On a numerical string(array), find the highest X combinations of digits (read from left to right). (e.g : 125547, the highest combinations of 2 digits is 55.)
    """

    with open("./Énoncé/03-12.txt", 'r') as fichier :
        input = fichier.readlines()
    
    # input = '987654321111111\n811111111111119\n234234234234278\n818181911112111'.split('\n')
    solution_part_one = 0
    solution_part_two = 0

    
    for line in input :
        line = line.strip('\n')
        solution_part_one += highestCombinationLine(line, 2)
        solution_part_two += highestCombinationLine(line, 12)
       

    print(f'Solution Part one : {solution_part_one}')  
    print(f'Solution Part two : {solution_part_two}')
        

def highestCombinationLine(line:str, buffer:int) -> int :
    """
    Docstring pour highestCombinationLine
    
    :param line: array of digits
    :type line: str
    :param buffer: size of the combination of digits required
    :type buffer: int
    :return: the highest value obtainable by combining [buffer] digits of the provided array [line] without reorganizing them
    :rtype: int
    """
    index_voltage = 0
    solution_str=''
    solution = 0
    while(buffer>0):
        # sub_line is the array of digits defined like this : [previous highest_voltage index : index of last digit - size of the remaining space of the buffer]
        # That's to allow us to find the highest number while being sure to provide enough remaining digit for the buffer to find the next highest one on that line AND complete the buffer.
        sub_line = line[index_voltage:len(line)-buffer+1]
    
        highest_voltage_str, indexSubString_highest_voltage = HighestInSubString(sub_line)
        index_voltage += indexSubString_highest_voltage+1 # position in the substring +1 because we don't want to check that value again in the next iteration. 
        solution_str += highest_voltage_str
        buffer-=1
    
    solution += int(solution_str)
    return solution


def HighestInSubString(substring:str) -> tuple[str, int]: 
    """
    Docstring pour HighestInSubString
    
    :param substring: sub array of the main array.
    :type substring: str
    :return: Find in the provided array the highest number and return its value (str) and its position in the substring
    :rtype: tuple[str, int]
    """
    highest_voltage = 0
    indexSubString_highest_voltage = 0
    highest_voltage_str=''
    for i in range(0, len(substring)) : 
        voltage = int(substring[i])
        voltage_str = str(voltage)
        if voltage > highest_voltage : 
            highest_voltage = voltage
            highest_voltage_str = voltage_str
            indexSubString_highest_voltage = i
    return highest_voltage_str, indexSubString_highest_voltage


if __name__ == "__main__" :
    main()