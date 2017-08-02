# Tutorial 03
Created Thursday 06 October 2016

1) Give regular expressions which exactly define the following languages. The alphabet in each case is given at the end.
------------------------------------------------------------------------------------------------------------------------

### (i). contains exactly one a, besides bs. {a, b}
b^+^ab^+^


### (ii). no a appears without another a beside it. {a, b}
(b*aaa*b*)*


### (iii). has 00 or 11 as a substring. {0, 1}
(0+1)*00+11(0+1)*


### (iv). has no b occurring anywhere after any a. {a, b, c}
(b + c)*(a+c)*


### (v). contains exactly two as or exactly two bs. {a, b}
(b*ab*ab*) +  (a*ba*ba*)


### (vi). has a substring abc or bc. {a, b, c}
(a + b + c)* bx (a + b +c)*


### (vii). {a, b} * - {a} 	{a,b} [i.e. any string of as and bs, but not the string "a"]
λ + a(a + b)^+^ + b(a + b) ^*^


### (viii). contains an even number of as and an even number of bs. {a, b}
((aa)*(bb)*)*


### (ix). represents a number divisible by 3. {0, 1}

2) Describe in plain English the languages defined by the following regular expressions:
----------------------------------------------------------------------------------------

### (i) (a + b) *
Any combination of as and bs


### (ii) (a + b) * ab(a + b) *
Any combination of as and bs containing ab


### (iii) a^2 + b^2
aa or bb


### (iv) ((a + b)^2 ) *
Any combination of as and bs with an even number of characters


### (v) a * b
Strings of any number of a's (including 0) followed by b.


### (vi) 1(0 + 1) *
1 followed by any number of 0s or 1s


### (vii) (0 + 1) * 011
Any number of 0s and 1s followed by 011


### (viii) 011 * + 100 *
0 followed by a non zero number of 1s ending in 1 followed by a non zero number of 0s


### (ix) (00 + 1) *
a string of 0s and 1s where all 0s come in pairs 


### (x) 0 (1+0) * 0
a string ending in 0 and starting with 0 of at least 2 characters


3) A certain programming language allows real constants to be written in exponent form - e.g. 3.25E6 (for 3.25x106) or 2.16E-5 (for 2.16x10-5). There must be exactly one digit before the decimal point (preceded by an optional sign), at least one digit after the decimal point, and the exponent can be a positive or negative integer. Write a regular expression specifying the language of such numbers. Define any abbreviations you use.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

S = λ + "+" + "-"
D = "."
N = 0 + 1 + 2 + ... + 9

SNDN + ESN +

4) Give a regular expression for all character strings which contain the word "cat". Assume only letters and spaces occur in the strings, and that words are separated by single spaces.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let X = Any letter in the alphabet
Let S = Space
(X*S)*CAT(S*X*)*

