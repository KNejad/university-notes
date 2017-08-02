# 4 - Assembly Language 4
Created Friday 29 January 2016

The cmp (compare) instruction modifies the flag register

![](./4_-_Assembly_Language_4/Screenshot from 2016-01-29 10-36-38.png)

To calculate the effective address of the memory, BIU uses the following formula:
Effective Address = Starting Address of Segment + Offset

To find the starting address of the segment, BIU appends the contents of Segment Register with 0H. Then, it adds offset to it.


Question:
---------
The contents of the following registers are:
CS = 1111 H
DS = 3333 H
SS = 2526 H
IP = 1232 H
SP = 1100 H
DI = 0020 H
Calculate the corresponding physical addresses for the address bytes in CS, DS and SS.
	
![](./4_-_Assembly_Language_4/pasted_image001.png)

