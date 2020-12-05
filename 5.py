input_file = open('5_input.txt', 'r') 
lines = input_file.readlines()
all_lines = [each.strip() for each in lines]
mults = []

'''
    PART ONE
'''  

for ticket in all_lines:
    row_data = ticket[:7]
    col_data = ticket[7:]

    row_no = [i for i in range(128)]
    col_no = [i for i in range(8)]

    for each in row_data:
        length = int( len( row_no ) / 2 )
        if each == 'F':
            row_no = row_no[:length]
        else:
            row_no = row_no[length:]
    row_no = row_no[0]

    for each in col_data:
        length = int( len( col_no ) / 2 )
        if each == 'L':
            col_no = col_no[:length]
        else:
            col_no = col_no[length:]
    col_no = col_no[0]

    mults.append( row_no * 8 + col_no )

print( max(mults) )

'''
    PART TWO
'''

mults.sort()
poss = []
for i in range( 1, len( mults) -1 ):
    if mults[i] == mults[i-1] + 1 and mults[i] == mults[i+1] - 1:
        pass
    else:
        poss.append(mults[i])

missing_id_val = int( (poss[0] + poss[1]) /2 ) 
print( missing_id_val )


