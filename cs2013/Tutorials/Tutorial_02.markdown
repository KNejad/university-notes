# Tutorial 02
Created Thursday 29 September 2016

1) Describe in words the languages accepted by each of the following FSAs:
--------------------------------------------------------------------------

### i)
![](./Tutorial_02/pasted_image.png)
	
Accepts a strings 0s and 1s with an even number of 0s


### ii)
![](./Tutorial_02/pasted_image001.png)
Accepts a sting of 0s and 1s starting with "10" and not containing "00"


### iii)
![](./Tutorial_02/pasted_image002.png)
Accepts a sting of 0s and 1s containing "00" or "11"


2) Give a formal definition for the FSAs which define the following languages (i.e. specify Q, I, F, T, E):
-----------------------------------------------------------------------------------------------------------

### (i) strings containing a or ab {a, b}
Q = 1, 2
I  = 1
F = 2
T = a , b
E = {1,a,2}, {2,a,2}, {2,b,2}

### (ii) strings containing aba or bab {a, b}
Q = 1, 2, 3 , 4 ,5 ,6
I  = 1
F = 4
T = a , b
E = {1,a,2}, {1,b,5}, {2,a,2}, {2.b,3}, {3,a,4}, {3,b,5}, {4,a,4},{4,b,4}, {5,a,6}, {5,b,5}, {6,a,2}, {6,b,4}

### (iii) strings containing exactly one a (and any number of bs) or exactly one b (and any number of as) {a, b}
Q = 1,2,3,4
I = 1
F = 3, 4
T = a,b
E = {1,a,3}, {1,b,4}, {2,a,2}, {2,b,2}, {3, a,2}, {3,b,3}, {4,a,2},{4,b,2}


### (iv) strings containing a, ab or abc {a, b, c}
Q = 1, 2
I  = 1
F = 2
T = a , b
E = {1,a,2}, {2,a,2}, {2,b,2}
	
### (v) strings containing a, ba or cba {a, b, c}
Q = 1, 2
I  = 1
F = 2
T = a , b
E = {1,a,2}, {2,a,2}, {2,b,2}
	


3) Give a formal definition for a FSA accepting the infinite set of strings representing numbers divisible by 2. (i.e. 0,2,4,6,8,10,12,....)
--------------------------------------------------------------------------------------------------------------------------------------------
Just check the last digit, make sure it’s even (need two states)
Let E=0,2,4,6,8
Let O=1,3,5,7,9
Then QIFTE=({1,2},{1},{2},{O,E},{(1,O,1),(1,E,2),(2,O,1),(2,E,2)})

