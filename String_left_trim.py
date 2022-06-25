def string_left_trim(string, val = ' '):
    result = ''
    stop = False
    for char in range(len(string)):
        if (string[char] == val and stop == False):
            continue
        else:
            stop = True
        result += string[char]
    return result
    
print(string_left_trim('++++++++++String', '+'))