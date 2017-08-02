# 20 - Single-cycle Processor
Created Friday 25 March 2016


#single-cycle, multi-cycle and pipelined processors materials will not be in the exam. 



![](./20_-_Single-cycle_Processor/pasted_image.png)


Multiple implementations for a single architecture:
---------------------------------------------------
Single-cycle: Each instruction executes in a single cycle
Multicycle: Each instruction is broken into series of shorter steps
Pipelined: Each instruction broken up into series of steps & multiple instructions execute at once


Processor Performance Definitions:
----------------------------------
CPI: The number of cycles per instruction is the number of clock cycles required to execute an average instruction
CPI: Cycles/instruction
IPC: instructions/cycle = IPC
Clock period: The number of seconds per cycle is the clock period Tc
Tc = seconds/cycle
	
	

Single-Cycle MIPS Processor:
----------------------------
Executes an entire instruction in one cycle
Datapath
Control


Single Cycle Datapath:
----------------------

### STEP 1: Fetch instruction from memory
PC register contains the address of the instruction to execute. 
The first step is to read this instruction from instruction memory.
The instruction memory reads out, or fetches, the 32-bit instruction, labeled Instr


### STEP 2: Read source operands from register file
![](./20_-_Single-cycle_Processor/pasted_image1.png)
	
I-type instructions use two register operands and one immediate operand.
The 32-bit instruction has 4 fields: op, rs, rt, imm.
rs and imm are the source registers; rt is the destination for addi and lw instructions  


### STEP 3: Sign-extend the immediate:
The lw instruction requires an offset. The offset is stored in the immediate field of the instruction, Instr15:0. 
The 16-bit immediate might be either positive or negative, it must be sign-extended to 32 bits
SignImm~15:0~ = Instr~15:0~; SignImm~31:16~ = Instr~15~
	

### STEP 4: Compute the memory address:
The process must add the base address to the offset to find the address to read from memory.
ALUControl is set to 010 to add the base address and offset
ALUResult is sent to the data memory as the address for the load instruction
	

### STEP 5: Read data from memory and write it back to register file:
The data is read from the data memory onto the ReadData bus, then written back to the destination register in the register file at the end of the cycle.
The destination register for the lw instruction is specified in the rt field, Instr20:16, which is connected to the port 3 address input A3.
ReadData is connected to to WD3. 
The write takes place on the rising edge of the clock
	

### STEP 6: Determine address of next instruction:
The process must compute the next instruction.
Instructions are 32 bits = 4 bytes, the next instruction is PC + 4.
The new address is written into the program counter on the next rising edge of the clock.
	

### R-type:
Register Type
R-type instructions use three registers as operands: two as sources, one as a destination. 
The 32-bit instruction has 6 fields: op, rs, rt, rd, shamt and funct.
R-type instructions: add, sub, and, or and slt
	




