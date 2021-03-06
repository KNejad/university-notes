# Assembly Code
Created Friday 22 January 2016

Assembly compiler online: <http://www.tutorialspoint.com/compile_assembly_online.php>
Using TASM assembly language.

DATA:
-----
All data goes in the .data part of the program
charname db ‘y’  ;A character variable initialized to ‘y’
stringname db ‘Enter the color:’, 0 ;A string, terminated by the NULL character
numname dw 4000 ;num is 16 bit, initialized to 4000
largename dd 80000 ;large is 32 bit, initialized to 80000
i db 20 ;i  is initialized to 20
k db ? ;k is undefined


Conditional Statements:
-----------------------
cmp ax, bx ;compare ax and bx and store the result in compare flag
je eq_lab ;if ax==bx, go to eq_lab


### Jump Instructions:
![](./Assembly_Code/pasted_image001.png)


Stacks:
-------
push ax;the value of ax stored on the stack
pop ax;transfers the data from the top of the stack to ax


mathematical operations:
------------------------
mul bl ;multiply bl * al giving result in ax.
div bl;divide ax by value in bl. result in al, remainder in ah
add ax, 2 ;add 2 to the contents of ax
sub ax,5 ;subtracts 5 from dxs
shr ;shift the bits one step to the right 
sar ;shift arithmetic right (keeps the sign)
shl ; shift left
dec dx ;decreases dx by 1
inc dx ;increments dx by 1


Terminate Program:
------------------
mov ax, 4c00h
int 21h


Macros:
-------
CR equ 13
samplemacro[parameter-list]
;text (body) of macro may be one
; or many lines
endm


I/O Actions:
------------
MOV AH, 2                    ; carriage return
MOV DL, 0DH          
INT 21H

MOV DL, 0AH                  ; line feed
INT 21H

MOV AH, 1                    ; read a character
INT 21H

MOV AH, 2                    ; display the character stored in CL   
MOV DL, CL
INT 21H


Graphical Mode:
---------------
INT 10h ;switch between graphical mode and text mode
![](./Assembly_Code/pasted_image.png)


### Colours:
0 Black  
1 Blue 
2 Green 
3 Cyan 
4 Red 
5 Magenta 
6 Brown 
7 Light Gray 
8 Dark Gray 
9 Light Blue 
A Light Green 
B Light Cyan 
C Light Red 
D Light Magenta 
E Yellow 
F White



