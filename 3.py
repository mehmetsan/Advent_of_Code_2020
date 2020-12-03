input_file = open('3_input.txt', 'r') 
lines = input_file.readlines()
all_lines = [each.strip() for each in lines]

def hit( x, y ):
    if all_lines[y][x] == '#':
        return True
    return False

'''
    PART ONE
'''

collision_count = 0
goal_y = len(all_lines)
width = len(all_lines[0])
coor = (0,0)
slope = (3,1)

while( coor[1] < goal_y ):
    if coor[0] >= width:
        coor = (coor[0] - width , coor[1])     
    if hit( coor[0], coor[1] ):
        collision_count += 1
    coor = (coor[0] + slope[0] , coor[1] + slope[1] )

print( collision_count)

'''
    PART TWO
'''

slopes =[
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

goal_y = len(all_lines)
width = len(all_lines[0])
result = 1

for slope in slopes:
    coor = (0,0)
    collision_count = 0
    while( coor[1] < goal_y ):
        if coor[0] >= width:
            coor = (coor[0] - width , coor[1])     
        if hit( coor[0], coor[1] ):
            collision_count += 1
        coor = (coor[0] + slope[0] , coor[1] + slope[1] )
    result *= collision_count

print( result )