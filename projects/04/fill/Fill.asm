// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.



(init)

  //keyIsPressed = true;
  @0
  D=A-1
  @keyIsPressed
  M=D

  //maxRAM = 24576
  @24576
  D=A
  @maxRAM
  M=D

  //screenRAM = 16384
  @16384
  D=A
  @screenRAM
  M=D

  //Loop{
  (beg)

    //maxCheck = maxRAM //just a reset
    @maxRAM
    D=M
    @maxCheck
    M=D

    //D = keyIsPressed
    @keyIsPressed
    D=M


    //address(screenRAM) = keyIsPressed
    @screenRAM
    A=M
    M=D

    //D = screenRam
    D=A

    //screenRAM++
    @screenRAM
    M=D+1

    //D = screenRAM
    D=M

    //maxCheck = maxCheck - screenRAM
    @maxCheck
    M=M-D

    //D = maxCheck
    D=M

    //if maxCheck > 0 then jump to init
    @init
    D;JEQ

    //else, go back to beg
    @beg
    0;JMP
