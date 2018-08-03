import mods, cIns
print("hack assembler".upper())

#hard coded filepaths
path = 'C:\\Users\\Pgeltman\\Documents\\My Special Projects\\nand2tetris\\projects\\06\\'

projNo = int(input("What project should I assemble (1 - 4): "))

if projNo == 1 or projNo == False:
    folder='add\\'
    project= "Add"
elif projNo == 2:
    folder='max\\'
    project = "MaxL"
elif projNo == 3:
    folder='pong\\'
    project = "PongL"
elif projNo == 4:
    folder='rect\\'
    project = "RectL"

asm = path + folder + project + '.asm'
hack = path + folder + project + '.hack'


#open the asm
progAsm = open(asm, 'r')

#open the hack
progHack = open(hack, 'w+')

line_count = 1

#main loop through the program
for line in progAsm:

    out = 'no output'
    line_type = 'blank'

    #determine the indext of the first real character (i.e. not a blank space)
    f = mods.first(line)
    first = line[f]

    #determin the index of the last real character (i.e. not a comment)
    l = mods.last(line)
    last = line[l]

    #comments
    if first == '/':
        line_type = 'comment'

    #a instructions
    elif first == '@':

        line_type = 'a ins'

        #takes the rest of the line after the '@'
        address = line[f+1:l]

        if mods.is_number(address) == True:

            #convert to integer
            address = int(address)

            #convert to binary
            address = int(f"{address:b}")

            #make it 16 digits
            address = "%016d" % address

            out = address

        else:
            address = "XXX"
            out = address
    #identify labels
    elif first == '(':
        line_type = 'label'

    #identify c instruction
    elif (first == '0') or (first == 'D') or (first == 'M') or (first == 'A'):
        line_type = 'c ins'
        decode = str(cIns.decode(line[f:l]))
        out = "111" + decode

    print ('%d : "%s" : %s' % (line_count, line[f:l], out))

    if out != 'no output':
        progHack.write(out + '\n')

    line_count += 1

progAsm.close()
progHack.close()

end = input("Done.")
