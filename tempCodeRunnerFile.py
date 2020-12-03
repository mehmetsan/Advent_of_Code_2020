input_file = open('2_input.txt', 'r') 
lines = input_file.readlines()


all_lines = [each.strip() for each in lines]
all_lines[0]

policies  = [( int( each.split(' ')[0].split('-')[0] ), int( each.split(' ')[0].split('-')[1] ) ) for each in all_lines]
letters   = [each.split(' ')[1][0] for each in all_lines]
passwords = [each.split(' ')[-1] for each in all_lines]

valid_pass = 0
for i in range( len(all_lines) ):
    count = 0
    for letter in passwords[i]:
        if letter == letters[i]:
            count += 1
    if( policies[i][1] >= count >= policies[i][0] ):
        valid_pass += 1
print(valid_pass)

'''
    PART TWO
'''

correct_pass = 0
for i in range( len(all_lines) ):
    present = 0
    ind1 = policies[i][0] -1
    ind2 = policies[i][1] -1
    letter = letters[i]
    print( ind1, ind2, letter, passwords[i])
    if passwords[i][ind1] == letter:
        present += 1
    if passwords[i][ind2] == letter:
        present += 1
    if present == 1:
        correct_pass +=1
print(correct_pass)
