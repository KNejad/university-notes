# 12 - Combinational
Created Friday 26 February 2016

Outputs determined by values of inputs
No memory

Rules For Combinational Composition:
------------------------------------
Every element is combinational
Every node is either an input or connects to exactly one output.
The circuit contains no cyclic paths


Adders:
-------

### Half Adder:
The sum can be found using the XOR operation and the carry using the AND operation.
![](./12_-_Combinational/pasted_image.png) ![](./12_-_Combinational/pasted_image003.png)


### Full Adder:
We can change our half adder into to a full adder by including gates for processing the carry bit.
![](./12_-_Combinational/pasted_image001.png)![](./12_-_Combinational/pasted_image002.png)
	

Decoders:
---------
Decoders are another important type of combinational circuit.
Among other things, they are useful in selecting a memory location according to a binary value placed on the address lines of a memory bus.
Address decoders with n inputs can select any of 2^n^ locations. 
![](./12_-_Combinational/pasted_image005.png)
	

Multiplexer:
------------
A multiplexer does just the opposite of a decoder.
It selects a single output from several inputs.
The particular input chosen for output is determined by the value of the multiplexer’s control lines.
To be able to select among n inputs, log 2^n^ control lines are needed. 
![](./12_-_Combinational/pasted_image004.png)

