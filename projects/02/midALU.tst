load MidALU.hdl,
output-file MidALU.out,
compare-to MidALU.cmp,
output-list x%B1.1.1 y%B1.1.1 car%B2.1.2 f%B1.1.1 no%B2.1.2 out%B2.1.2 carry%B1.1.1;

set x 0, set y 0, set car 0, set f 0, set no 0, eval, output;
set x 0, set y 0, set car 0, set f 0, set no 1, eval, output;
set x 0, set y 0, set car 0, set f 1, set no 0, eval, output;
set x 0, set y 0, set car 0, set f 1, set no 1, eval, output;
set x 0, set y 0, set car 1, set f 0, set no 0, eval, output;
set x 0, set y 0, set car 1, set f 0, set no 1, eval, output;
set x 0, set y 0, set car 1, set f 1, set no 0, eval, output;
set x 0, set y 0, set car 1, set f 1, set no 1, eval, output;
set x 0, set y 1, set car 0, set f 0, set no 0, eval, output;
set x 0, set y 1, set car 0, set f 0, set no 1, eval, output;
set x 0, set y 1, set car 0, set f 1, set no 0, eval, output;
set x 0, set y 1, set car 0, set f 1, set no 1, eval, output;
set x 0, set y 1, set car 1, set f 0, set no 0, eval, output;
set x 0, set y 1, set car 1, set f 0, set no 1, eval, output;
set x 0, set y 1, set car 1, set f 1, set no 0, eval, output;
set x 0, set y 1, set car 1, set f 1, set no 1, eval, output;
set x 1, set y 0, set car 0, set f 0, set no 0, eval, output;
set x 1, set y 0, set car 0, set f 0, set no 1, eval, output;
set x 1, set y 0, set car 0, set f 1, set no 0, eval, output;
set x 1, set y 0, set car 0, set f 1, set no 1, eval, output;
set x 1, set y 0, set car 1, set f 0, set no 0, eval, output;
set x 1, set y 0, set car 1, set f 0, set no 1, eval, output;
set x 1, set y 0, set car 1, set f 1, set no 0, eval, output;
set x 1, set y 0, set car 1, set f 1, set no 1, eval, output;
set x 1, set y 1, set car 0, set f 0, set no 0, eval, output;
set x 1, set y 1, set car 0, set f 0, set no 1, eval, output;
set x 1, set y 1, set car 0, set f 1, set no 0, eval, output;
set x 1, set y 1, set car 0, set f 1, set no 1, eval, output;
set x 1, set y 1, set car 1, set f 0, set no 0, eval, output;
set x 1, set y 1, set car 1, set f 0, set no 1, eval, output;
set x 1, set y 1, set car 1, set f 1, set no 0, eval, output;
set x 1, set y 1, set car 1, set f 1, set no 1, eval, output;
