'''
    PART ONE
'''
def find_mult( all_lines ):
    for line in all_lines:
        for num in all_lines:
            if( line + num == 2020 ):
                return line, num, line * num

input_file = open('1_input.txt', 'r') 
lines = input_file.readlines()

all_lines = [int(each.strip()) for each in lines]


print( find_mult(all_lines))

'''
    PART TWO
'''
def find_multiplication( all_lines ):
    for line in all_lines:
        for num in all_lines:
            for each in all_lines:
                if( line + num + each == 2020 ):
                    return line, num, each, line * num * each
            
print( find_multiplication(all_lines))