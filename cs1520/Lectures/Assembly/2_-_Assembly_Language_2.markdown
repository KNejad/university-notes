# 2 - Assembly Language 2
Created Tuesday 26 January 2016

Sign numbers:
-------------
Signed numbers are used to differentiate positive and negative numbers
The number on the left is the sign number
Positive number: sign bit = 0
Negative number: sign bit = 1
eg 1101= -5


Addition:
---------
When working with signed numbers regular addition won't work so instead we use two's compliment 
To negate a number to 2’s complement flip the bits and add 1
89~10~ = 01011001
One’s complement:	89~10~ = 10100110 (flip all the bits i.e. all 1s become 0 all 0s become 1)
Two’s complement : -89~10~ = 10100110 + 1 =  10100111
Then just add the numbers together as usual 
	

