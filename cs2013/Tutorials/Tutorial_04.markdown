# Tutorial 04
Created Thursday 13 October 2016

[What is Mathematical induction?](https://en.wikipedia.org/wiki/Mathematical_induction)



To prove that a statement P(n) is true for all natural numbers k , where  k is a natural number, we proceed as follows:
-----------------------------------------------------------------------------------------------------------------------
Help: [Mathematical Induction -- First Principle](http://www.cs.odu.edu/~cs381/cs381content/induction/induction.html)
Basis Step: Prove that P(k) is true. 
Induction: Prove that for any integer k, if P(k) is true (called induction hypothesis), then P(k+1) is true. 

The first principle of mathematical induction states that if the basis step and the inductive step are proven, then P(n) is true for all natural number tex2html_wrap_inline59 . 

As a first step for proof by induction,   it is often a good idea to restate P(k+1) in terms of P(k) so that P(k), which is assumed to be true, can be used.

1) (Number theory.) Prove: The n-th positive even number equals 2n.
-------------------------------------------------------------------
Let the n-th positive even number = E(n) 
	
Basis step: We need to prove that E(1) = 2*1 = 2, which is true, because E(1)=2. 
	
Induction step: Suppose (this is the Induction Hypothesis, IH) that for certain n, it is true that E(n)=2n. We now need to prove that it follows that E(n+1)=2(n+1). So let's focus on E(n+1). 
	
Evidently, E(n+1)=E(n)+2. By writing E(n+1) in this form (in which E(n) occurs!), we are now able to apply IH. For, by IH, it follows from E(n+1)=E(n)+2 that E(n+1)=2n+2. But from this it follows directly that E(n+1)=2(n+1), which is what we wanted to prove. QED
	

2) (Number theory.) Prove: 3^n < n! for n>=7.
---------------------------------------------
Let the n-th power of 3 be P(n)
	
3^(n+1) = 3^n * 3
(n+1)! = n! * b where b=n+1.
	
Basis step: P(7) < 7! => 2187 < 5040 
	
Induction Step:  P(n)* 3 < n!*n+1  
	
	
3) (Set theory) Prove that if A1,A2,..,An and B1,B2,..,Bn are sets such that A_j is a subset of B_j for each j=1,2,..,n, then (A1 intersection ... intersection An) is s subset of (B1 intersection ... intersection Bn).
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4) ( Propositional logic , using - for negation and ^ for conjunction) Prove that -(p1 v p2 v ... v p_n) <==> -p1 ^ -p2 ^ ... ^ -p_n.
-------------------------------------------------------------------------------------------------------------------------------------

5) ( Number theory ) What is wrong with this “proof”? “Theorem”: For every positive integer n, if x and y are positive integers with max(x,y)=n, then x=y. Base step: Let n=1. If max(x,y)=1 then x=y=1. Induction step: Let k be a positive integer. Suppose that whenever x and y are positive integers with max(x,y)=k, then x=y. Now let max(x,y)=k+1, where x and y are positive integers. Then max (x-1,y-1)=k, hence (by the induction hypothesis) x-1=y-1, from which it follows that x=y.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

6)( Formula induction ) Prove that all statements of propositional logic have an even number of brackets. (Formulated and proven in class.)
-------------------------------------------------------------------------------------------------------------------------------------------

