# Tutorial 9
Created Monday 21 March 2016

1) Explain why a designer might choose to use a ripple-carry adder instead of a carry-lookahead adder.
------------------------------------------------------------------------------------------------------

Less resources required. Cheaper to build.

2) Design a ‘not equal’ comparator for 32-bit numbers. Sketch the schematics.
-----------------------------------------------------------------------------
![](./Tutorial_9/pasted_image001.png)


3) Design 4-bit left rotators. Sketch a schematic of your design
----------------------------------------------------------------
![](./Tutorial_9/pasted_image003.png)

4) The funnel shifter in the following figure can perform any N-bit shift or rotate operation. It shifts a 2N-bit input right by k bits. The output Y is the N least significant bit of the result. The most significant N bits of the input are called B and the least significant N bits are called C. By choosing appropriate values of B, C and k, the funnel shifter can perform any type of shift or rotate.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![](./Tutorial_9/pasted_image.png)

### (a) Explain what these values should be in terms of A, shamt, and N for logical right shift of A by shamt.

### (b) Explain what these values should be in terms of A, shamt, and N for arithmetic right shift of A by shamt.

5) Express the following base 10 numbers in 16-bit fixed point two's complement format with 8 integer bits and 8 fraction bits. Express your answer in hexadecimal.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

### (a) -13.5625
Binary: 00001101.10010000
Two's complement: 11110010.01110000
Hex: f270


### (b) 42.3125
Binary: 00101010.01010000
Two's Complement: Positive number does not need twos complement
Hex: 2a50


### (c) -17.15625
Binary: 00010001.00101000
Two's Complement: 11101110.11011000
Hex: eed8
	

6) Convert the following two’s complement binary fixed-point numbers to base 10. The implied binary point is explicitly shown to aid in your interpretation:
------------------------------------------------------------------------------------------------------------------------------------------------------------

### (a) 0101.1000
5.5

### (b) 1111.1111
0000.0001
-0.0625

