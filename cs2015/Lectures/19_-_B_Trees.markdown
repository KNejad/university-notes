# 19 - B Trees
Created Tuesday 15 November 2016

Balanced Tree

Organises index in organised way.
Balanced: Any piece of information would take the same amount of jumps to access

Multi-level Index:
------------------
The key idea used to improve search efficiency is to add another level of index to the initial level of index
This idea can be repeated several times to define several levels of index


Leaf Node:
----------
Any node that does not have child nodes. 

B-Trees store data pointers in non-leaf nodes and also leaf nodes

B+ Trees:
---------
B+-Tree stores data pointers in leaf nodes only


#### Insertion:
If there is an overflow split the leaf node.
Create a new node 
The final value left in the original node is replicated in the parent node
Add a pointer to the new node
	
#### Deleting:
Redistribute the entries to ensure that alll leaf nodes are at least half full
Or merge multiple entries to reduce the number of leaf nodes


Trees:
------
Trees are aranged such that you can follow the nodes by viewing the left leaf for smaller values than the node value and the right leaf for larger values than the node. 
Nodes can also have ranges (ie 3 8) then anything between 3 and 8 (excluding 3, including 8) will be in the central node
	




