from functools import lru_cache

def get_lines():    
    input_file = open('10_input.txt', 'r') 
    lines = input_file.readlines()
    all_lines = [int(each.strip()) for each in lines]

    return all_lines

lines = get_lines()
lines.sort()

diffs = {
    '1': 0,
    '2': 0,
    '3': 1  #always
}

past_val = 0

for ad in lines:
    diff = ad - past_val
    diffs[str(diff)] += 1
    past_val = ad

print(diffs['1'] * diffs['3'])

'''
    PART TWO
'''
def find_possibles( i , cur_val ):
    if len(lines) - i -1 == 1:  # IF ONE NUMBER
        return [( each,lines.index(each) ) for each in lines[i+1:i+2] if each - cur_val < 4 ]
    elif len(lines) - i -1 == 2:    # IF TWO NUMBERS
        return [( each,lines.index(each) ) for each in lines[i+1:i+3] if each - cur_val < 4 ]
    elif len(lines) - i -1 > 2:   # IF THREE NUMBERS
        return [( each,lines.index(each) ) for each in lines[i+1:i+4] if each - cur_val < 4 ]
    else:
        return None
    
cur_val = 0

@lru_cache(maxsize=None)
def find_paths(i,cur_val):
    if cur_val == lines[-1]:    #REACHED FINAL VALUE
        return 1

    possibles = find_possibles(i,cur_val)   #POSSIBLE GO VALUES AND THEIR INDECES IN (VAL, IND) FORMAT

    if not possibles:   # IF STUCK, CAN'T GO FURTHER
        return 0
        
    sums = 0    
    for each in possibles:
        val = each[0]
        res = find_paths(each[1],val)
        sums += res
    return sums

print( find_paths(-1,cur_val) )
