# Tutorial 01
Created Saturday 24 September 2016

1) Design a web application that displays the values of the following variables when accessing the root url address.
--------------------------------------------------------------------------------------------------------------------

### Code:
my_num = 25
my_boolean = true
my_string = "Ruby"


### Answer:
require 'sinatra'
my_num = 25
my_boolean = true
my_string = "Ruby"
	
get '/' do
"#{my_num} #{my_boolean} #{my_string}"
end
	


2) Design a web application that displays the same output as the following code in a browser when accessing the root url address.
---------------------------------------------------------------------------------------------------------------------------------

### Code:
puts "hello"
print "there"
print “Nigel”


### Answer:
require 'sinatra'
		
get '/' do
"hello <br> there <br> nigel"
end
		


3) Design a web application that uses the same code as below to display the length of the string in a browser when accessing the root url address.
--------------------------------------------------------------------------------------------------------------------------------------------------

### Code:
"Nigel Beacham".length


### Answer:
require 'sinatra'
varlength = "Nigel Beacham".length
get '/' do
"#{varlength}"
end

4) Design a web application that displays the same output as the following code in a browser when accessing the root url address.
---------------------------------------------------------------------------------------------------------------------------------

### Code:
"Eric".reverse


### Answer:
require 'sinatra'
varl = "Eric".reverse
get '/' do
"#{var}"
end

5) Design a web application that displays the same output as the following code in a browser when accessing the root url address.
---------------------------------------------------------------------------------------------------------------------------------

### Code:
puts "eric".upcase
puts "NIGEL".downcase


### Answer:
NO!

6) Design a web application that inserts a comment within a web page so that the same output is displayed as the following code in a browser when accessing the root url address.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Code:
# comment


### Answer:
NO!


7) Design a web application that inserts a multiline comment within a web page so that the same output is displayed as the following code in a browser when accessing the root url address.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Code:
=begin
comment
=end


### Answer:
NO!
	
8) Design a web application that displays the same output as the following code in a browser when accessed by a suitable url address.
-------------------------------------------------------------------------------------------------------------------------------------

### Code:
my_name = "Nigel"
my_age = 40
puts “My name is #{my_name} and I am #{my_age} years old.”


### Answer:
If you don't challenge me I won't do it!
	
9) Design a web application that displays the same output as the following code in a browser when accessed by a suitable url address.
-------------------------------------------------------------------------------------------------------------------------------------

### Code:
sum = 13+379
product = 923 * 15
quotient = 13209 / 17
print “sum=” + sum
print “product=” + product
print “quotient=” + quotient


### Answer:
Maybe I will do the full tutorial next week
	
10) Design a web application that displays the same output as the following code in a browser when accessed by a suitable url address.
--------------------------------------------------------------------------------------------------------------------------------------

### Code:
name = "Nigel".downcase.reverse.upcase
puts name


### Answer:
zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

