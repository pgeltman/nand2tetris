// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

//clear the result
@R2
M=0

//clear the working result
@R3
M=0

//jump to the end if r1 = 0
@R1
D=M
@18 //last line of code + 1
D;JLE

//save input1 into d register
@R0
D=M

//Save the result of d+m into the m
@R3
M=D+M

//decrement input2 as countdown
@R1
M=M-1

//Load R1 into d
@R1
D=M

@8 //or the begging of the loop (line 24)
D;JGT

//set d to the working output
@R3
D = M

//set the final output to d
@R2
M = D
