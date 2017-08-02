# 14 - AJAX and JQuery
Created Thursday 03 March 2016

Asynchronous JavaScript And XML (AJAX):
---------------------------------------
AJAX uses JavaScript’s XMLHttpRequest method to exchange data with the server without reloading the current page.


JQuery:
-------
A library of JS functions
Contains HTML element Manipulation, Animation, etc
To use download JQuery.js and add it as an external JS file or <script src="<https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js>"></script>
Basic syntax is: $(selector).action()
A dollar sign to define jQuery
A (selector) to "query (or find)" HTML elements
A jQuery action() to be performed on the element(s)


### Examples:

#### Hide:
$(this).hide()
	
#### On Load Function:
$(document).ready(function(){
// Code to be run when everything has loaded
});


#### CSS Manipulation
$("p").css("background-color","yellow");
	
#### Event Handler:
$("button").click(
function(){
$("p").hide();
}
);


#### Animation:
$(selector).hide(speed,callback); //callback is called after the animation finishes 


#### Load:
$(selector).load(url,data,callback)


