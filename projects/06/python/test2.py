import symb

path = 'C:\\Users\\Pgeltman\\Documents\\My Special Projects\\nand2tetris\\projects\\06\\max\\Max.asm'

prog = open(path, 'r')

symDic = symb.id(prog)

print(symDic)
