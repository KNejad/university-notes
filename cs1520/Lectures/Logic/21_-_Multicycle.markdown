# 21 - Multicycle
Created Friday 01 April 2016

#single-cycle, multi-cycle and pipelined processors materials will not be in the exam.  

Compared to Single Cycle:
-------------------------
+ higher clock speed
+ simpler instructions run faster
+ reuse expensive hardware on multiple cycles
-  sequencing overhead paid many times


STEP 1: Fetch instruction:
--------------------------
The instruction is stored in an Instruction register
IRWrite is asserted when updating a new instruction.


STEP 2a: Read source operands from RF:
--------------------------------------
Read the source register (rs field), Instr25:21, into RD1
The value of RD1 is stored in a register A


STEP 2b: Sign-extend the immediate
----------------------------------
The offset Instr15:0 is signed extended to be 32 bits
	



