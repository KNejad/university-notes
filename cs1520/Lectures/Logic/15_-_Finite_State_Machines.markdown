# 15 - Finite State Machines
Created Tuesday 08 March 2016

Moore FSM:
----------
Outputs depend only on current state
Input drawn on lines output on state


### Example:
![](./15_-_Finite_State_Machines/pasted_image001.png)
	

Mealy FSM:
----------
Outputs depend on current state and inputs
Input and output shown on lines. 


### Example:
![](./15_-_Finite_State_Machines/pasted_image.png)
	

State Transition And Output Table:
----------------------------------
To create a state transition and output table encode the states as 0s and 1s (So state 0 can be 000, state 1 can be 001 etc)
Then create a table with the current state with all the state encoding values as separate items of the table and the input and the next state that will cause along with the output (So S1, S2, Input, S1', S2', Output)
Then create K-maps and get the minterms using each next state item as an output (So 1 k-map with S1' as output another with S2' as output etc)
#These are in the timing lecture slides 


### Example:
![](./15_-_Finite_State_Machines/pasted_image002.png)
	

