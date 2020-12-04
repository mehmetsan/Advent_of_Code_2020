input_file = open('4_input.txt', 'r') 
lines = input_file.readlines()
all_lines = [each.strip() for each in lines]
all_lines.append(' ')   # NEED 1 MORE LINE FOR THE INPUT FILE FORMAT

'''
    PART ONE
'''
# INITIALIZATION
new_passport = True
req = []
count = 0

for line in all_lines:
    if new_passport:
        req  = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    if not line.strip(): # EMPTY LINE
        if len(req) == 0 or ( len(req) == 1 and req[0] == 'cid' ):
            count += 1
        new_passport = True
    else:               # NON-EMPTY LINE
        if new_passport == True:
            new_passport = False

        for each in line.split(' '):
            req.remove( each.split(':')[0] )


print( count )

'''
    PART TWO
'''
# INITIALIZATION
new_passport = True
req = []
count = 0

passport = {}
import re

regex_hair = '^#[a-f0-9]{6}$'
regex_pid = '^[0-9]{9}$'



for line in all_lines:
    if new_passport:
        passport = {}
        req  = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    if not line.strip(): # EMPTY LINE
        new_passport = True
        if len(req) == 0 or ( len(req) == 1 and req[0] == 'cid' ):
            # VALIDATON
            if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
                continue
            if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
                continue
            if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
                continue
            if passport['hgt']:
                if passport['hgt'][-2] == 'c':
                    if int(passport['hgt'][0:-2]) < 150 or int(passport['eyr'][0:-2]) > 193:
                        continue
                elif passport['hgt'][-2] == 'i':
                    if int(passport['hgt'][0:-2]) < 59 or int(passport['eyr'][0:-2]) > 76:
                        continue
            if not re.match(regex_hair, passport['hcl']):
                continue
            if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                continue

            if not re.match(regex_pid, passport['pid']):
                continue
            count += 1
    else:               # NON-EMPTY LINE
        if new_passport == True:
            new_passport = False

        for each in line.split(' '):
            req.remove( each.split(':')[0] )
            data = ( each.split(':')[0], each.split(':')[1])
            passport[data[0]] = data[1]

print( count )
