# 7 - Numbers
Created Tuesday 09 February 2016

How to Manage Complexity:
-------------------------
Abstraction (everything is "blocked" so that people can work on 1 level without worrying about the previous levels eg if your working on software you don't have to worry about logic gates)
Discipline


### The Three –Y’s:
Hierarchy
Modularity
Regularity (Encouraging uniformity, so modules can be easily reused)


How Many Values Can I Represent With n Numbers In Decimal?
----------------------------------------------------------
How many values? 10^N^
Range?  [0, 10^N^ - 1]

Most Significant bit (MSb): the bit with the highest value (on the left)
Least Significant bit (LSb): the bit with the lowest value (on the right)

![](./7_-_Numbers/pasted_image.png)

Overflow:
---------
When result is too big to fit in the available number of bits

Sign: [Lectures:Assembly:2 - Assembly Language 2](../Assembly/2_-_Assembly_Language_2.markdown)

Increasing Bit Width:
---------------------
Make the number have more bits in it.
We do this in order for a number to fit properly 


### Sign-extension:
Add all the numbers to be the sign that the number has (copy the left most bit)


### Zero-extension:
Add zeros to the number (does not work with two's complement)




