# 8 - Web Forms
Created Tuesday 09 February 2016

put form in <form> </form> tag 
<input type="text" name="surname" id="username" /> surname is the variable that gets edited and sent to the server
<input type="submit" />

Attributes:
name
autocomplete: whether autocomplete is allowed
novalidate: Says that the form should not be validated before sending to server
id: Unique identifier of the form
method: How the form will be sent to the server
action: Specify the script on the server which will process the form
	
GET: pass the data into the address
POST: sends the data in a different packet

![](./8_-_Web_Forms/pasted_image001.png)

<option value="value name" disabled selected> item name </option> disables means you can't select it and selected means its the pre selected option. Option goes in the select tag

<label for="id-of-radio-button">words</label>

to make sure a field is set you can validate it client side with Javascript, Jquery or with a required tag or  server side with php etc
you should use all of them because users can edit the client side stuff. required tag is only supported in HTML 5. Use client side so that bandwidth isn't wasted sending data back and forth.


