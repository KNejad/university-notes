# 13 - Sequential 1
Created Tuesday 01 March 2016

Outputs depend on current and prior input values
Has memory (short-term)

### Definitions:
State: all the information about a circuit necessary to explain its future behaviour
Latches and flip-flops: state elements that store one bit of state
Synchronous sequential circuits: combinational logic followed by a bank of flip-flops


Timing:
-------
Propagation delay: t~pd~ = max delay from input to output
Contamination delay: t~cd~ = min delay from input to output


### Delay Is Caused By:
Capacitance and resistance in a circuit
Speed of light limitation


### Reasons Why Propagation And Contamination Delay May Be Different:
Different rising and falling delays
Multiple inputs and outputs, some of which are faster than others.
Circuits slow down when hot and speed up when cold.


Clock:
------
A special circuit that sends electrical pulses through a circuit
Clocks produce electrical waveforms (square waves)
State changes occur in sequential circuits only when the clock ticks. 
Circuits can change state on the rising edge, falling edge, or when the clock pulse reaches its highest voltage.


Bistable Circuit:
-----------------
![](./13_-_Sequential_1/pasted_image.png)
Two stable states, Q=0 and Q=1, 
Stores 1 bit of state in the state variable, Q (or Q')
But there are no inputs to control the state


SR (Set/Reset Latch):
---------------------
![](./13_-_Sequential_1/pasted_image001.png)
SR Latch is a bistable circuit with 1 bit of state stored in Q.
S = 1, R = 0: then Q = 1 and Q' = 0
S = 0, R = 1: then Q' = 1 and Q = 0
S = 0, R = 0: then Q = Qprev (Memory)
S = 1, R = 1: then Q = 0 and Q'= 0 (Invalid State) 


D Latch:
--------

### Two inputs: CLK, D
CLK: controls when the output changes
D (the data input): controls what the output changes to


### Function
When CLK = 1: D passes through to Q (transparent)
When CLK = 0: Q holds its previous value (opaque)
Avoids invalid case when Q ≠ NOT Q
![](./13_-_Sequential_1/pasted_image002.png)![](./13_-_Sequential_1/pasted_image003.png)

