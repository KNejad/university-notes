# Practical 9
Created Monday 21 March 2016

Introduction
The 8086 microprocessor provided eight 16-bit registers. It could separately access the upper and lower eight bits of some of these registers. When the 32-bit 80386 was introduced, the registers were extended to 32 bits. These registers are called EAX, ECX, EDX, EBX, ESP, EBP, ESI, and EDI. For backward compatibility, the bottom 16 bits and some of the bottom 8-bit portions are also usable, as shown in the figure below.

![](./Practical_9/pasted_image.png)



Table 1 lists the combinations of operand locations in x86.
![](./Practical_9/pasted_image001.png)
Table 1. Operand Locations

x86 has a 32-bit memory space that is byte-addressable. x86 also supports a much wider variety of memory addressing modes. Memory locations are specified with any combination of a base register, displacement, and a scaled index register. The displacement can be an 8-, 16-, or 32-bit value. The scale multiplying the index register can be 1, 2, 4, or 8. The scaled index provides an easy way to access arrays or structure of 2-, 4-,or 8-byte element without having to issue a sequence of instructions to generate the address.
Table 2 illustrates these combinations.
![](./Practical_9/pasted_image002.png)
Table 2. Memory addressing mode


x86 instructions can operate on 8-, 16-, or 32-bit data. Table 3 illustrates these variations.
![](./Practical_9/pasted_image003.png)




Question 1
Consider the following code, and determine the values of the specified registers:
.data
Val1 dd 12345678h
.code
;assume ESP=0200h
Push val1 			;ESP=202h
Mov EAX , 20h
Mov EBX , 30h
Add EBX , EAX
Push EBX
Push EAX 			;ESP=206h
Call Quizp 		;EIP=?
;ESP=206h
Mov ah,4ch
Int 21h
Quizp PROC
;assume EBP=5
Push EBP 			;ESP=208h
Mov EBP , ESP
Mov ECX , [EBP + 8]	 ;213h
Mov EDX, [EBP + 16] 	;EDX=223h
Mov EBX, [EBP + 12] 	;EBX=214h
Pop EBP 			;ESP=206h
Ret 12 			;ESP=206h , ;EBP=208h
Quizp ENDP
END




Question 2 
If SS=0200h and SP=0100h,
what will be the value of SP,AX and EBX after executing the following code?

POP AX
POP EBX

Data stored in the stack segment is shown in the table below:

Value of SP 		Value stored
107h 			8Bh
106h 			54h
105h 			8Fh
104h 			78h
103h 			6Dh
102h 			2Ah
101h 			12h
100h 			4Ah
0FFh 			5Bh
0FEh 			8Ch
0FDh 			9Fh
0FCh 			85h
0FBh 			43h
0FAh 			2Dh
0F9h 			Ach


SP=0FCh
AX=8Ch
EBX==85


