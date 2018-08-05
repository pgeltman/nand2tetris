import mods
#symbol resolution modules

def id(program):

    #starting number for variables
    var_pos = 16

    #starting number for labels
    num = 0

    symDic = {'SP' : 0 , 'LCL' : 1 , 'ARG' : 2 , 'THIS' : 3 , 'THAT' : 4 , 'R0' : 0 , 'R1' : 1 , 'R2' : 2 , 'R3' : 3 , 'R4' : 4 , 'R5' : 5 , 'R6' : 6 , 'R7' : 7 , 'R8' : 8 , 'R9' : 9 , 'R10' : 10 , 'R11' : 11 , 'R12' : 12 , 'R13' : 13 , 'R14' : 14 , 'R15' : 15 , 'SCREEN' : 16384 , 'KBD' : 24576}

    for line in program:

        #determine the indext of the first real character (i.e. not a blank space)
        f = mods.first(line)
        first = line[f]

        #determin the index of the last real character (i.e. not a comment)
        l = mods.last(line)

        if first == '(':

            #takes the rest of the line after the '@'
            word = line[f+1:l-1]

            #check if it's in the table
            if word not in symDic:
                symDic[word] = num

        if first == '@':

            #takes the rest of the line after the '@'
            word = line[f+1:l]

            if mods.is_number(word) == False:

                #check if it's in the table
                if word not in symDic:
                    symDic[word] = var_pos
                    var_pos += 1

    if first == '@' or first == '(' or first == '0' or first == 'A' or first == 'M' or first =='D':
        num += 1

    return symDic
