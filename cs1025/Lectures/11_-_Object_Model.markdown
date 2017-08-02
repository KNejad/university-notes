# 11 - Object Model
Created Mon Nov 28 2016

A method on an object is called
Ruby looks through the receiving object’s instance methods. If it finds the method it executes it
If not found: pass request up chain to object’s class
If not found: pass request up to classes parent class, etc, up to the Object class itself
If not found: Go back to the object and call method ‘method_missing’ if exist
If not exist: Go to object’s class, and parent’s classes
If method_missing not found:  raise a NoMethodError 


Singleton Method:
-----------------
A method attached to a particular object which can only be called by that object.

