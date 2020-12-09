def get_lines():    
    input_file = open('8_input.txt', 'r') 
    lines = input_file.readlines()
    all_lines = [each.strip() for each in lines]

    return all_lines