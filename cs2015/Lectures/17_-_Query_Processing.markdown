# 17 - Query Processing
Created Tuesday November 8 2016

Query Processing Operations:
----------------------------
Syntax Analysis: transform SQL into an internal form
Normalisation: Rewrites the WHERE and AND and OR predicates into disjunctine or conjunctive form (see relational algebra) 
Semantic analysis: Checks if the query is valid (whether it makes sense)
Simplification: Remove redundant parts
Generating execution plan:  Query optimisation
Executing plan and returning results to client


### Steps In Lexical And Syntactical Analysis:
Identify keywords
Identify table names & aliases
Map aliases to table names
Identify column names
Check if columns exist


Relational Algebra:
-------------------
A symbolic formal way of describing relational operations
Says how, as well as what (order is important)
Can use re-write rules to simplify and optimise complex queries


### RA Notaion:
Selection: σ
Projection: π
Rename: ρ
Cartesian product: x
union: U
intersection: ∩
conjunction (AND): Λ
disjunction (OR): V
negation (NOT): ~
Natural Join: ⋈


### Operations SQL Equivalent:
Selection: WHERE
Projection: SELECT
Rename: AS


### SQL Queries in RA:
SELECT name FROM staff: π name (staff)
SELECT name FROM staff AS user: ρ user (name) π name (staff)
SELECT name FROM staff where  salary =1: π name σ salary=1 (staff)


### Relational Algebra Tree (RAT):
The output of the syntactical analysis

