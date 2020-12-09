def get_lines():    
    input_file = open('9_input.txt', 'r') 
    lines = input_file.readlines()
    all_lines = [int(each.strip()) for each in lines]

    return all_lines

lines = get_lines()
the_num = 0
'''
    PART ONE
'''
def iterate(i, lines):
    for reverse in range(1,26):
        inspect = lines[i-reverse]

        if (cur_no - inspect) in lines[i-25 : i]:
            if (cur_no - inspect) != inspect:
                return True
    return False

for i in range(25, len(lines)):
    cur_no = lines[i]
    if not iterate(i, lines):
        print(cur_no, i)
        the_num = cur_no
        break
        
'''
    PART TWO
'''

def iterate_new(lines, num):
    for i in range(len(lines)):
        summ = 0
        index = i
        while summ < num:
            summ += lines[index]
            index += 1
        if summ == num:
            interval = lines[i:index]
            return max(interval) + min(interval)
    
print(iterate_new(lines,the_num ))    
