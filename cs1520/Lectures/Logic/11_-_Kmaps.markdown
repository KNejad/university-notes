# 11 - Kmaps
Created Tuesday 23 February 2016

Circuit Schematic Rules:
------------------------
Inputs on the left (or top) of a schematic.
Outputs on right (or bottom) of a schematic.
Whenever possible, gates flow from left to right.
Straight wires are best
Wires always connect at a T junction
A dot where wires cross indicates a connection between the wires
Wires crossing without a dot make no connection


Don't Cares:
------------
An output or input where we don't care if it is High or Low
Marked with an X
	

Karnaugh Maps:
--------------
A way to simplify a truth table in order to get the most simple equations.
Useful for up to six variables
![](./11_-_Kmaps/pasted_image.png)


### Rules:
Every 1 must be circled at least once (it can be circled multiple times)
Each circle must span a power of 2 (i.e. 1, 2, 4) adjacent squares in each direction
Each circle must be as large as possible
A circle may wrap around the edges
A "don't care" (X) is circled only if it helps minimize the equation.


Illegal Value: X
----------------
The symbol X indicates that the circuit node has an unknown or illegal value.
Since X is also used for don't care, look at the context to decide what the X is


Floating Value: Z
-----------------
The symbol Z indicates a node is being driven neither HIGH nor LOW.
.

