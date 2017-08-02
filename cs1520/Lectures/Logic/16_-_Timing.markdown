# 16 - Timing
Created Friday 11 March 2016

Terms:
------
Setup time: t~setup~ = time before clock edge data must be stable (i.e. not changing)
Hold time: t~hold~ = time after clock edge data must be stable
Aperture time: t~a~ = time around clock edge data must be stable (t~a~ = t~setup~ +  t~hold~)
Propagation delay: t~pcq~ = time after clock edge that the output Q is guaranteed to be stable (i.e., to stop changing). (These are different than prop and cont delay with logic gates as done before.)
Contamination delay: t~ccq~ = time after clock edge that Q might be unstable (i.e., start changing) 


Setup Time Constraint (Tc):
---------------------------
Depends on the maximum delay from register R1 through combinational logic to R2.
The input to register R2 must be stable at least t~setup~ before clock edge.
T~c~ ≥ t~pcq~ + t~pd~ + t~setup~
t~pd~ ≤ T~c~ – (t~pcq~ + t~setup~)
![](./16_-_Timing/pasted_image.png)


Hold Time Constraint:
---------------------
Depends on the minimum delay from register R1 through the combinational logic to R2.
The input to register R2 must be stable for at least t~hold~ after the clock edge.
if t~ccq~ + t~cd~ > t~hold~ then the delay is met. if it is not then add more gates (eg buffer)
![](./16_-_Timing/pasted_image001.png)
	

