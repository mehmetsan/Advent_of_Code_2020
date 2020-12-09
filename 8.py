def get_lines():    
    input_file = open('8_input.txt', 'r') 
    lines = input_file.readlines()
    all_lines = [each.strip() for each in lines]

    return all_lines

class Command():
    def __init__(self, comm=''):
        self.command = comm
        self.count = 0
    def change(self):
        cur_comm = self.command
        temp = 'nop' + cur_comm[3:]
        self.command = temp
    def change_to_jmp(self):
        cur_comm = self.command
        temp = 'jmp' + cur_comm[3:]
        self.command = temp

all_lines = get_lines()


'''
    PART ONE
'''

commands = [Command(comm=each) for each in all_lines]
accumulator = 0
i= 0
cont = True

while cont:
    if commands[i].count == 0:
        if commands[i].command[0] == 'a':
            if commands[i].command[4] == '+':
                accumulator += int(commands[i].command[5:])
            else:
                accumulator -= int(commands[i].command[5:])
        elif commands[i].command[0] == 'j':
            if commands[i].command[4] == '+':
                i += int(commands[i].command[5:])
            else:
                i -= int(commands[i].command[5:])
            i -= 1 # FOR FOR LOOP
        else:
            pass
        commands[i].count += 1
        i += 1 #IMITATE FOR LOOP

    else:
        cont = False
print(accumulator)
'''

'''
    PART TWO
'''


def test_output( comms):
    commands = comms
    accumulator = 0
    i= 0

    cont = True
    while i < len(commands):
        if commands[i].count == 0:
            if commands[i].command[0] == 'a':
                if commands[i].command[4] == '+':
                    accumulator += int(commands[i].command[5:])
                else:
                    accumulator -= int(commands[i].command[5:])
            elif commands[i].command[0] == 'j':
                if commands[i].command[4] == '+':
                    i += int(commands[i].command[5:])
                else:
                    i -= int(commands[i].command[5:])
                i -= 1 # FOR FOR LOOP
            else:
                pass
            commands[i].count += 1
            i += 1 #IMITATE FOR LOOP

        else:

            return False
    return accumulator

comms_origin = [Command(comm=each) for each in all_lines]

jump_indeces = []
for i in range(len(all_lines)):
    if (all_lines[i][0]=='j'):
        jump_indeces.append(i)


for case in jump_indeces:

    comms = [Command(comm=each) for each in all_lines]
    comms[case].change()
    result = test_output(comms)

    if result:
        print(result)
        break


