# 02 - FSA
Created Tuesday 13 September 2016

Example of a Finite State Machine:
----------------------------------
![](./02_-_FSA/pasted_image.png)
The arrow points to the initial state 
The double circle is the final state


Finite State Automaton:
-----------------------
Q: states = a finite set;
I: initial states = a nonempty subset of Q;
F: final states = a subset of Q;
T: an alphabet;
E: edges = a subset of Q × (T + λ) × Q.
(The above definition of an FSA allows nondeterminism)


Path:
-----
A sequence of edges where the end state of one is the first state of the next
A path is successful if the start state of the first edge is an initial state, and the end state of the last is a final state.

A string is accepted by a FSA if it is the label of a successful path.


Non-Determinism:
----------------
From one state there could be a number of edges with the same label. Have to remember possible branching points as we trace out a path, and investigate all branches.
Some of the edges could be labelled with λ, the empty string. How does this affect our algorithm?
May be more than one initial state. Where do we start?


Deterministic:
--------------
There are no λ-labelled edges;
For any pair of state and symbol (q,t), there is at most one edge (q,t, p)
There is only one initial state.


Transition function:
--------------------
The resulting destination in an edge when given initial state and input


Minimum Size of FSA's:
----------------------
If x and y are in T* and we append z to both. Now if only 1 of the 2 xz or yz are in T* then x and y are different






