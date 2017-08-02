# 01 - Intro
Created Monday 12 September 2016


Definitions:
------------
Alphabet: A finite set of symbols.
A string over an alphabet T is a finite sequence of symbols from T. Also called T-string, or simply string.
The empty string is the string with no symbols, denoted by λ.
The length of a string, w, is the number of symbols in the sequence, denoted |w|.
If u is a substring of w, and y above is λ, then u is a suffix of w.	If u ≠ w, then u is a proper suffix.
If T is an alphabet, then T* is the set of all strings over T. T^+ is T* without λ.
If "a" is a symbol, then "a^n^" is the string of n a's
A language over an alphabet T is a set of strings over T. Also called a T-language, or simply a language.
a* is "a" any number of times in a row (Kleene Closure)


Language Operations:
--------------------
A+B is the set union of A and B
A ∩ B is the set intersection of A and B
A' is the complement of A - i.e. all strings in T* but not in A.
AB is the concatenation of A and B - i.e. all strings uv where u ∈ A and v ∈ B
A^n^ is the concatenation of A with itself n times.
	

Ordering:
---------

### Dictionary Order:
All strings beginning "a" are ordered before all strings beginning "b", and "b" before "c", etc.
Within groups of strings beginning with the same symbol, strings are ordered by their second symbol, and so on.
λ is always the first string. 


### Lexical Order:
Strings are ordered by their length, with the shortest first. 
Within groups of strings of the same length, strings are ordered in dictionary order.


Finite State Automata:
----------------------
A finite state automaton is an abstract model of a simple machine (or computer).
The machine can be in a finite number of states. It receives symbols as input, and the result of receiving a particular input in a particular state moves the machine to a specified new state.
Certain states are finishing states, and if the machine is in one of those states when the input ends, it has ended successfully.

