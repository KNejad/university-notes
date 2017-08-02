# 04 - Equivalence
Created Monday 26 September 2016

Regular expressions and FSA's are equivalent

Combining NDFSA:
----------------

### L = L1 + L2:
A = (Q1 ∪ Q2 ∪ {i,f} , {i} , {f} , T , E1 ∪ E2 ∪ {(i,λ,i 1 ),(i,λ,i 2 ),(f1 ,λ,f),(f2 ,λ,f)})


### L =L1L2:
A = (Q1 ∪ Q2 , {i1} , {f2} , T , E1 ∪ E2 ∪ {(f1,λ,i2)})


### L = L1*:
A = (Q1 ∪ {i,f} , {i}, {f}, T, E1 ∪ {(i,λ,i 1 ),(i,λ,f),(f1 ,λ,f),(f1 ,λ,i1)})


Convert Regular Expression To NDFSA:
------------------------------------
Deconstruct the regular expression into its base parts
Convert base parts into NDFSAs
Combine base parts 


Convert NDFSA To Regular Expression:
------------------------------------
A regular finite state automaton (RFSA) is a FSA where the edge labels may be regular expressions.
An edge labelled with the regular expression r indicates that we can move along that edge on input of any string included in r


### 1) Create Unique Initial State:
Input: (Q, I, F, T, E)
Q := Q ∪ {i} (where i ∉ Q)
for each q ∈ I, E:= E ∪ {(q,λ,i)} //might be (i,λ,q)
I := {i}
	

### 2) Create Unique Final State:
Input: (Q, I, F, T, E)
Q := Q ∪ {f} (where f ∉ Q)
for each q ∈ F, E:= E ∪ {(q,λ,f)}
F := {f}
C

### 3) Algorithm To Convert NDFSA to RE:
While there are states in Q\{i,f}
begin
For each state p in Q with more than one edge to itself, labelled r1 ,r2 ,...,rn , 
replace all those edges by (p,r1+r2+...+rn,p).
For each pair of states p,q in Q with more than one edge from p to q labelled r1 ,r2 ,...,rn
replace all those edges by (p,r1+r2+...+rn ,q).
select a state s ∉ {i,f}
For each pair of states p,q (≠s) s.t. there are edges (p,r 1 ,s) and (s,r 2 ,q)
begin
if there is an edge (s,r3 ,s)
add the edge (p,r1r3*r2 ,q)
else 
add the edge (p,r1r2 ,q)
end
remove all edges to or from s
remove all states & edges with no path from i
end
return r, where E = (i,r,f).


Regular Finite State Automaton (RFSA):
--------------------------------------
A FSA where the edge labels may be regular expressions
An edge labelled with a regular expression indicates that we can move along that edge on an input string included in the regular expression


