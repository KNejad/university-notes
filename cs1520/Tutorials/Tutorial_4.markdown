# Tutorial 4
Created Monday 15 February 2016

1) Suppose bp contains 1234h, bx contains 2456h, si contains 128h, and di contains 15h.
---------------------------------------------------------------------------------------

### mov al,10h[bx+si], what address does AL load from ?
2456h+0128h+10h=258Eh

### mov ch,125h[bp+di], What address does CH  load from ?
1234h+15h+125h= 136Eh

### mov bx,cs:2[bx][di],  What addresses does BX load from?
2h+2456h+15h=246Dh 246Eh


2) The following is a high level language program that sums the contents of the array into total
------------------------------------------------------------------------------------------------
int total = 0;
for (int i=0; i<numX, i++){
total += X[i];
}

We now translate it into 8086 assembly language  (code fragment example):

X		DW	; comment 1: First element of the array  
DW	; comment 2: Second element of the array 

. . .			etc.
numX		DW	;number of elements in the array
….
….
MOV AX, 0		;initialise sum
LEA DI, X		;initialise array, LEA means load effective address
MOV CX, numX	; comment 3: put the value of numX into CX
CheckForDone:
  CMP CX, 0		; comment 4: compare CX with 0 
  JE	DONE
  ADD AX, [DI]	; comment 5: add the value of DI to AX
  ADD DI, 2		; comment 6: increment DI by 2
  SUB CX, 1		; comment 7: remove 1 from cx
  JMP CheckForDone
DONE: …


### a) What type of addressing mode is the above code?
Indirect addressing mode


### b) Give the seven comments for the above code (i.e., comment 1, 2, 3, … 7)

[Optional: you can choose to do or not to do the two questions]

### c)Change the above code to use “indexed addressing mode”.


### D) Change the above code to use “based-indexed addressing mode”.


