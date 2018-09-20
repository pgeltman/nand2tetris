import fun, classes

print("virtual machine".upper())

#project folder path
path = '/Users/ggeltman/Documents/GitHub/nand2tetris/projects/07/'

#input prokect number
#projNo = int(input("What project should I compile (1 - 5): "))

projNo = 1

if projNo == 1 or projNo == False:
    subfolder='MemoryAccess'
    project= 'BasicTest'

elif projNo == 2:
    subfolder='MemoryAccess'
    project = 'PointerTest'

elif projNo == 3:
    subfolder='MemoryAccess'
    project = 'StaticTest'

elif projNo == 4:
    subfolder='StackArithmetic'
    project = 'SimpleAdd'

elif projNo == 5:
    subfolder='StackArithmetic'
    project = 'StackTest'

basicPath = '%s/%s/%s/%s' % (path, subfolder, project, project)

vmPath = '%s.vm' % (basicPath)
outputPath = '%s.out' % (basicPath)


#open the vm file
vm = open(vmPath, 'r')

#open the output
output = open(outputPath, 'w+')

#main loop through the program
for line in vm:

    classes.test()

vm.close()
output.close()

end = input("Done.")
