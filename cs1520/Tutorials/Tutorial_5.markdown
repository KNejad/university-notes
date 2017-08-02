# Tutorial 5
Created Monday 22 February 2016

1. A three-input OR-AND-INVERT (OAI) gate shown in the following produces a FALSE output if C is TRUE and A or B is TRUE. Otherwise it produces a TRUE output. Complete a truth table for the gate.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](./Tutorial_5/pasted_image.png)


### Answer:
A	B	C	Y
0	0	0	1
0	0	1	1
0	1	0	1
0	1	1	0
1	0	0	1
1	0	1	0
1	1	0	1
1	1	1	0

2. Is it possible to assign logic levels so that a device with the transfer characteristics shown in the following would serve as an inverter? If so, what are the input and output low and high levels (VIL, VOL, VIH, VOH) and noise margins (NML, and NMH)? If not, explain why not.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](./Tutorial_5/pasted_image001.png)


### Answer:
VIL = 2.5; VIH = 3; VOL = 1.5; VOH = 4; NML = 1; NMH = 1;


3. Write a Boolean equation in sum-of-products canonical form for each of the truth tables in the following figure
------------------------------------------------------------------------------------------------------------------
	
![](./Tutorial_5/pasted_image002.png)


### Answer:

#### a)
A'B' + AB' + AB


#### b)
A'B'C' + ABC


#### c)
A'B'C' + A'BC' + AB'C' + AB'C + ABC


#### d)
A'B'C'D' + A'B'C'D + A'B'CD' + A'B'CD + AB'C'D' + AB'CD' + ABCD'


#### e)
A'B'C'D' + A'B'CD + A'BC'D + A'BCD' + AB'C'D + ABC'D' + ABCD


4. Write a Boolean equation in product-of-sums canonical form for the truth tables in the above Figure (from Question 3).
-------------------------------------------------------------------------------------------------------------------------

### Answers:

#### a)
(A + B')


#### b)
(A+ B + C') * (A + B' + C) * (A + B' + C') * ( A' + B + C) * (A' + B + C') * (A' + B' + C)


#### c)
(A + B + C') * (A + B' + C') * (A' B' C)


#### d)
THIS IS BORING


#### e)
NEXT EXERCISE 


5. Minimize each of the Boolean equations from Question 4.
----------------------------------------------------------

#### a)
A + B'


#### b)
A'B'C' + ABC


