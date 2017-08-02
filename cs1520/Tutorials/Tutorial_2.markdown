# Tutorial 2
Created Monday 01 February 2016

1) Explain the operation of the push and pop instructions and their effect on the stack pointer
-----------------------------------------------------------------------------------------------
push puts an item in top of the stack 
pop takes the top item from the stack


2) What is the difference between the following instructions?
-------------------------------------------------------------

### cmp ax, bx
bx is the address


### cmp ax, [bx]
[bx] is the content of the address bx


3)What are the contents of the ax and bx registers?:
----------------------------------------------------
mov ax, 0Ah
mov bx, 23h
push bx
push ax
pop ax
pop bx
 
ax: 0Ah 
bx: 23h

4)What are the contents of the ax and bx registers?:
----------------------------------------------------
mov ax, 0Ah
mov bx, 23h
push ax
mov ax, bx
pop bx
 
ax:23h
bx:0Ah

5) Write a code fragment to sum the sequence 2,4,6,8,…,18,20,22,24. The result should be stored in a variable called sum.
-------------------------------------------------------------------------------------------------------------------------
	
	
sum db 0
mov ax 2
L2:
add sum. ax
add ax, 2
cmp ax, 24 
jl L2
	



6) Write instructions to evaluate the arithmetic expression 5+ (6-2) leaving the result in ax using (a) one register, (b) two registers, and (c) three registers
----------------------------------------------------------------------------------------------------------------------------------------------------------------

### a)
mov ax 6
sub ax 2
add ax 5

### b)
mov ax 5
mov cx 6
sub cx 2
add ax cx

### c)
mov ax 5
mov bx 6
mov cx 2
sub bx cx
add ax bx

7) Write a program to convert a single digit number 5 to its character equivalent '5' (given ascii code of character '5' is 53d, ascii code of '0' is 48)
---------------------------------------------------------------------------------------------------------------------------------------------------------

mov ax number
add ax 48

8) Specify the instructions and masks you would use to
------------------------------------------------------

### (a) set bits 2,3 and 4 of the ax register
or ax 1110b

### (b) clear bits 4 and 7 of the bx register
and ax 1111111110110111b

9) How would al be affected by the following instructions:
----------------------------------------------------------

### (a) and al, 00fh:
Will keep the 4 smallest bits

### (b) and al, 0f0h:
Will keep bits 5,6,7,8 as is and change everything else

### (c) or al, 00fh:
Will make 4 smallest bits 1 and keep everything else the same

### (d) or al, 0f0h:
Will make bits 5,6,7,8 a 1 and keep everything else the same

