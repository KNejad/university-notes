# 09 - Normalization
Created Tuesday 11 October 2016


Unnormalized Form (UNF):
------------------------
A table that contains one or more repeating groups.
To create an unnormalized table: transform data from information source (e.g. form) into table format with columns and rows.


First Normal Form (1NF);
------------------------
A relation in which intersection of each row and column contains one and only one value.
ie you do not have a field item1 and a field item2


Second Normal Form (2NF):
-------------------------

### Based on concept of full functional dependency:
A and B are attributes of a relation R, 
B is fully dependent on A (denoted A->B) if B is functionally dependent on A but not on any proper subset of A.
	
A relation that is in 1NF and every non-primary-key attribute is fully functionally dependent on the primary key.
Every value in a column depends on its primary key.

Third Normal Form (3NF):
------------------------


### Based on concept of transitive dependency:
A, B and C are attributes of a relation such that if A -> B and B -> C, 
Then C is transitively dependent on A through B.  (Provided that A is not functionally dependent on B or C).

A relation that is in 1NF and 2NF and in which no non-primary-key attribute is transitively dependent on the primary key.
Every value in a column directly depends on its primary key (so B can't depend on A through C) 

