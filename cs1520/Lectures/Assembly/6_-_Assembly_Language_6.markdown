# 6 - Assembly Language 6
Created Friday 05 February 2016

Two restrictions on the use of the segment registers with the mov instruction:
------------------------------------------------------------------------------
You may not specify cs as the destination operand
Only one of the operands can be a segment register

You cannot move data from one segment register to another with a single mov instruction. To copy the value of cs to ds, you'd have to use some sequence like: 
mov ax, cs 
mov ds, ax


The addressing modes provided by the 8086 family include:
---------------------------------------------------------
Register Indirect Addressing Mode: mov al, [bx]
Displacement-only (or direct): Consists of a 16 bit constant that specifies the address of the target location (eg mov al,ds) 
Base plus indexed:  mov al, [bx][si]
Indexed Addressing Mode: mov al, disp[bx]
Displacement plus base plus indexed: mov al, disp[bx][si]

