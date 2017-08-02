# 18 - File Organisation
Created Thu  Dec 1 2016

We study three types of file organization:
------------------------------------------

### Unordered or Heap files:
Records are stored in the same order in which they are created
Very fast for insert but slow for everything else


### Ordered or sequential files:
Records are sorted by one or more fields (primary keys)
Very slow for insert but fast for everything else


### Hash files:
Records are sorted based on the hashes of the prime key(s)
Fast on all query types


Indexing:
---------
By indexing query performance can be further increased
ISAM: Indexed sequential access method
	
### Secondary Indexes::
An index which uses non primary keys for indexing
Usefull for queries which do not involve the primary key


### Creating indexes in SQL:
An index can be created for any field in sql
CREATE INDEX field ON table

