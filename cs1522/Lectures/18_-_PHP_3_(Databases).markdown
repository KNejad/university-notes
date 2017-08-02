# 18 - PHP 3 (Databases)
Created Thursday 17 March 2016

#just doing stuff that i did in Databases at high school


To create classes:
------------------
class Dog {
$name;
$breed;
$shoes_eaten;
f}


Then make a new instance of this object:
----------------------------------------
$puppy = new Dog();
$puppy->name = 'Rover';
$puppy->breed = 'mongrel';
$puppy->shoes_eaten = 6;
echo $puppy->name; //will print Rover


Before you can access data in a database, you must create a connection to the database, which is a new PDO object:
------------------------------------------------------------------------------------------------------------------
$db = new PDO('mysql:host=hostname;dbname=dbname;charset=utf8mb4', $username, $password);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);



Example Connection:
-------------------
<?php
$username = 'anythingotherthanroot';
$password = 'cheese';
$host = 'mysql.abdn.ac.uk';
$dbname = 'lovelycheeses';
$db = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $username,$password);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
?>


Try Catch:
----------
try {
//try something
} catch (PDOException $ex} {
//die($ex); use this in development only. prints the error
redirect('brokensite.php'); //send user to an error page
}


The university's MySQL server is mysql.abdn.ac.uk
This server is not available outside the university network

The university provides SFTP access on ftpweb.abdn.ac.uk
Note: FTP will not work!

