# 9 - Transistors
Created Tuesday 16 February 2016

Definition:
-----------
A semiconductor device that amplifies, oscillates, or switches flow of current between two terminals by varying the current or voltage between one of the terminals and a third. 


Most common types:
------------------
Bipolar Junction Transistor (BJT)
Field-Effect Transistor (FET)


### Bipolar Junction Transistor:
Terminals labelled base, collector, emitter
Small current at the base control or switch a much larger current between the collector and emitter.
![](./9_-_Transistors/pasted_image.png)	 


### Field-Effect Transistor:
Terminals labelled gate, source, drain
Voltage at the gate can control a current between source and drain.
![](./9_-_Transistors/pasted_image001.png)


 ![](./9_-_Transistors/pasted_image002.png)
All logic gates work using combinations of transistors.

NOT Gate:
---------
![](./9_-_Transistors/pasted_image003.png)![](./9_-_Transistors/pasted_image004.png)

### Explanation:
When A is low the PMOS gate turns on allowing current to go to Y and the NMOS is off so Y doesn't get 0 
When A is high the PMOS gate turns off so the current from VDD can not pass through Y and NMOS turns on allowing Y to be connected to GND
	


NAND Gate:
----------

![](./9_-_Transistors/pasted_image005.png)![](./9_-_Transistors/pasted_image006.png)


