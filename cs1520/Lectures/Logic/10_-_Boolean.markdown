# 10 - Boolean
Created Friday 19 February 2016

C overlapping L means Combinational Logic
![](./10_-_Boolean/pasted_image.png)


Boolean Axioms:
---------------
 ![](./10_-_Boolean/pasted_image001.png)
#A2  0=1 supposed to be 0=1' and 1=0 is supposed to be 1=0'


Boolean Theorems:
-----------------
![](./10_-_Boolean/pasted_image002.png)
#T5 is supposed to be B * B' and B + B'


Boolean Theorems of Several Variables:
--------------------------------------
![](./10_-_Boolean/pasted_image006.png)


Bubble Pushing:
---------------
Bubble pushing is a technique to apply De Morgan's theorem directly to a logic diagram.
![](./10_-_Boolean/pasted_image005.png)


Sum-of-Products (SOP):
----------------------
All equations can be written in SOP form
Each truth table row has a minterm
A minterm is a product (AND) of input variables
Each minterm is TRUE for that row (and only that row)
Form function by ORing minterms where the output is TRUE 
Thus, a sum (OR) of products (AND terms)
![](./10_-_Boolean/pasted_image007.png)
Y = F(A, B) = A'B + AB = Σ(1, 3)


Product-of-Sums (POS):
----------------------
All Boolean equations can be written in POS form
Each truth table row has a maxterm
A maxterm is a sum (OR) of literals
Each maxterm is FALSE for that row (and only that row)
Form function by ANDing the maxterms for which the output is FALSE
Thus, a product (AND) of sums (OR terms)
![](./10_-_Boolean/pasted_image008.png)
Y = F(A, B) = (A + B)(A' + B) = Π(0, 2)
	


