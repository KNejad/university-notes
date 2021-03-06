# 14 - Sequential 2
Created Friday 04 March 2016

Latches:
--------
Any change on the inputs is seen at the outputs immediately when CLK=1.
This causes synchronization problems.
Solution: Use latches to create flip-flops that can respond (update) only at specific times (instead of any time).


Flip-Flop:
----------
Output only changes according to behaviour of clock edge.
Also known as clocked devices.


### D Flip-Flop:
The fundamental circuit of computer memory. 
Two inputs: CLK, D
Edge-triggered: Samples D on rising edge of CLK (When CLK rises from 0 to 1, D passes through to Q. Otherwise, Q holds its previous value)
![](./14_-_Sequential_2/pasted_image.png)![](./14_-_Sequential_2/pasted_image002.png)


#### A D Flip-Flop is made of 2 D Latches:
![](./14_-_Sequential_2/pasted_image003.png)


### Enabled Flip-Flop:
Three inputs: CLK, D, EN
EN = 1: D passes through to Q on the clock edge
EN = 0: The flip-flop retains its previous state
![](./14_-_Sequential_2/pasted_image004.png)


### Resettable Flip-Flop:
Three inputs: CLK, D, Reset
Reset = 1:  Q is forced to 0 
Reset = 0:  flip-flop behaves as ordinary D flip-flop
![](./14_-_Sequential_2/pasted_image006.png)


#### Two types:
Synchronous: resets at the clock edge only
Asynchronous: resets immediately when Reset = 1


### Settable Flip-Flops:
Three inputs: CLK, D, Set
Set = 1:  Q is set to 1 
Set = 0:  The flip-flop behaves as ordinary D flip-flop
![](./14_-_Sequential_2/pasted_image005.png)


Finite State Machines:
----------------------
So far, our sequential circuit outputs have been limited to state variables (e.g. Q)
In general, sequential circuits have outputs in addition to the state variable(s).


### Two types (or models) of sequential circuits (FSMs):
Mealy Machine: Output is a function of present state and present input
Moore Machine: Output is a function of present state only


### State Diagram:
Describes a machine as a finite state machine 


#### Coin-Operated Turnstile State Diagram:
![](./14_-_Sequential_2/pasted_image007.png)
	

