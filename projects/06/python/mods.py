#MISC ASSEMBLER FUNCTIONS AND WHAT NOT


def first(line):
    j = 0
    for letter in line:
        if letter != ' ':
            k = letter
            break
        j += 1

    return j

def last(line):
    started = False
    j = 0
    for letter in line:

        if letter != ' ':
            started = True
        elif (letter == ' ' or letter == ')')and started == True:
            break

        j += 1

    return min(j, len(line)-1)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
