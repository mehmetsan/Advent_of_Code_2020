import string

input_file = open('6_input.txt', 'r') 
lines = input_file.readlines()
all_lines = [each.strip() for each in lines]
all_lines.append(' ')

'''
    PART ONE
'''
groups = []
group_inputs = []
new_group = True
count = 0

for line in all_lines:
    if new_group:
        group_inputs = []

    if not line.strip(): # EMPTY LINE
        prep = list(set(group_inputs))
        prep.sort()
        groups.append( prep )
        count += len( prep )

        new_group = True
    else:               # NON-EMPTY LINE
        if new_group == True:
            new_group = False

        for each in line:
            group_inputs.append(each)

print( count )

'''
    PART TWO
'''
def reset_dict():
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    alphabet_set = {}
    for each in alphabet_list:
        alphabet_set[each] = 0
    return alphabet_set

groups = []
group_inputs = {}
new_group = True
people_count = 0
count = 0


for line in all_lines:
    if new_group:
        group_inputs = reset_dict()
        people_count = 0


    if not line.strip(): # EMPTY LINE
        commons = []
        for key in group_inputs.keys():
            if group_inputs[key] == people_count:
                commons.append(key)
        count += len(commons)
        new_group = True
    else:               # NON-EMPTY LINE
        if new_group == True:
            new_group = False

        people_count += 1
        for each in line:
            group_inputs[each] += 1

print( count )