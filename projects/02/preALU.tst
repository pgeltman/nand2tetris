load PreALU.hdl,
output-file preALU.out,
compare-to preALU.cmp,
output-list in%B1.1.1 z%B1.1.1 n%B1.1.1 out%B1.1.1;

set in 0,
set z 0,
set n 0,
eval,
output;

set in 0,
set z 0,
set n 1,
eval,
output;

set in 0,
set z 1,
set n 0,
eval,
output;

set in 0,
set z 1,
set n 1,
eval,
output;

set in 1,
set z 0,
set n 0,
eval,
output;

set in 1,
set z 0,
set n 1,
eval,
output;

set in 1,
set z 1,
set n 0,
eval,
output;

set in 1,
set z 1,
set n 1,
eval,
output;
