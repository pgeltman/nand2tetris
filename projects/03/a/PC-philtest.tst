// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/03/a/PC.tst

load PC.hdl,
output-file PC.out,
//compare-to PC.cmp,
output-list time%S1.4.1 in%D1.6.1 reset%B2.1.2 load%B2.1.2 inc%B2.1.2 out%D1.6.1;

set in 0,
set reset 0,
set load 0,
set inc 1,
tick,
output;

tock,
output;

set inc 1,
tick, output;
tock, output;
tick, output;
tock, output;
tick, output;
tock, output;
tick, output;
tock, output;
set inc 0,
tick, output;
tock, output;
tick, output;
tock, output;
tick, output;
tock, output;
tick, output;
tock, output;
