# 19 - Memory Arrays
Created Tuesday 22 March 2016

N address bits and M data bits:
-------------------------------
2^N^ rows and M columns
Depth: number of rows (number of words)
Width: number of columns (size of word)
Array size: depth * width = 2^N^  *  M


Memory Array:
-------------
![](./19_-_Memory_Arrays/pasted_image001.png)

### Bit Cell:
![](./19_-_Memory_Arrays/pasted_image.png)
To retrieve data from stored bit enable wordline (Set high) 
Then read the value of the bitline.
	


Volatile Memory:
----------------
Loses its data when power off
Read and written quickly
Main memory in your computer is RAM (DRAM)


Nonvolatile Memory:
-------------------
Retains data when power off
Read quickly, but writing is impossible or slow
Flash memory in cameras, thumb drives, and digital cameras are all ROMs


Types of Ram:
-------------

### DRAM (Dynamic random access memory):
Uses a capacitor
![](./19_-_Memory_Arrays/pasted_image003.png)
Dynamic because the value needs to be refreshed (rewritten) periodically and after read
READ: data values are transferred from the capacitor to the bitline
WRITE: data values are transferred from the bitline to the capacitor
	
	

### SRAM (Static random access memory):
Uses cross-coupled inverters
![](./19_-_Memory_Arrays/pasted_image002.png)
Value does not have to be refreshed
Faster Than DRAM but more expensive 


Dot Notation:
-------------
![](./19_-_Memory_Arrays/pasted_image004.png)

A dot means that there is a 1 stored no dot means 0


Multi-ported Memories:
----------------------
![](./19_-_Memory_Arrays/pasted_image006.png)
Port: address/data pair
3-ported memory (can access several addresses simultaneously)
2 read ports (A1/RD1, A2/RD2)
1 write port (A3/WD3, WE3 enables writing)
Port 1 reads the data from address A1 onto the read data output RD1
Port 2 reads the data from address A2 onto the read data output RD2
Port 3 writes the data from the write data input WD3 into address A3 on the rising edge of the clock if write enables WE3 is asserted


PLAs (Programmable logic arrays):
---------------------------------
![](./19_-_Memory_Arrays/pasted_image005.png)
AND array followed by OR array
Combinational logic only
Fixed internal connections


FPGAs (Field programmable gate arrays):
---------------------------------------
Array of Logic Elements (LEs)
Combinational and sequential logic
Programmable internal connections

