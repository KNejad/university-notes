# 17 - Adders
Created Tuesday 15 March 2016


Half Adder:
-----------
![](./17_-_Adders/pasted_image.png)


Full Adder:
-----------
![](./17_-_Adders/pasted_image001.png)
	
	

Multi-Bit Adders:
-----------------
Ripple-carry (slow): Time delay  t~ripple~ = N * t~FA~ where t~FA~ is the delay of a full adder and N the number of adders
Carry-lookahead (fast): Carry-lookahead adders are faster for large adders but require more hardware.(Usually arranged in blocks of 4.)
![](./17_-_Adders/pasted_image003.png)
![](./17_-_Adders/pasted_image002.png)
Same symbol as Full Adder but has /N at A B and S


How Carry-lookahead Works:
--------------------------
The carry lookahead adder (CLA) solves the carry delay problem by calculating the carry signals in advance, based on the input signals.
It is based on the fact that a carry signal will be generated in two cases:
(1) when both bits A and B are 1, or
(2) when one of the two bits is 1 and the Cin is 1.


For N-bit CLA with k-bit blocks the delay is: t~CLA~ = t~pg~ + t~pg_block~ + (N/k – 1)*t~AND_OR~ + k*t~FA~
t~pg~ : delay to generate all Pi, Gi
t~pg_block~ : delay to generate all Pi:j, Gi:j
t~AND_OR~ : delay from Cin to Cout of final
t~FA~:  is the delay of a full adder

