#Hack assembler
print("hack assembler".upper())

#input the asm file location
#filepath = input("Filepath to ASM file: ")

#hard coded filepaths
path = 'C:\\Users\\Pgeltman\\Documents\\My Special Projects\\nand2tetris\\projects\\06\\'

projNo = int(input("What project should I assemble (1 - 3): "))

if projNo == 1 or projNo == False:
    project='add\\Add.asm'
    projName = "Add"
elif projNo == 2:
    project='max\\Max.asm'
    projName = "Max"
elif projNo == 3:
    project='pong\\Pong.asm'
    projName = "Pong"

filepath = path + project

#open the asm
prog = open(filepath, 'r')

line_count = 1

for line in prog:

    #first real character
    j = 0
    for letter in line:
        if letter != ' ':
            k = line[j]
            break
        elif j == len(line):
            line_type = "blank"
        j += 1

    #comments
    if (k == '/'):
        line_type = 'comment'

    #a instructions
    elif (k == '@'):

        #takes the rest of the line after the '@'
        address = line[j+1:len(line)-1]

        line_type = address

    #identify labels
    elif (k == '('):
        line_type = 'label'

    #identify c instruction
    elif (k == '0') or (k == 'D') or (k == 'M'):
        line_type = 'c ins'

    else:
        line_type = 'blank'

    print ('%d : "%s"' % (line_count, line_type))

    line_count += 1

end = input("Done.")
