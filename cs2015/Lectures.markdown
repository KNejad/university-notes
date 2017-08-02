# Lectures
Created Tuesday 13 September 2016

User-Defined Domains in ANSI SQL:
---------------------------------

### Users can create their own domains:
CREATE DOMAIN SexType AS CHAR(1)
DEFAULT 'M'
CHECK (VALUE IN ('M', 'F'));


### Using the Domain:
CREATE TABLE Staff (StaffNo VARCHAR(5),
Lname VARCHAR(20), Salary FLOAT,
HireDate DATE, Sex SexType);


### Maximum number of connections:
CREATE ASSERTION StaffNotOverLoaded
CHECK (NOT EXISTS
(SELECT StaffNo FROM PropertyForRent
GROUP BY StaffNo HAVING COUNT (*) > 100));
CREATE TABLE PropertyForRent (...
CONSTRAINT StaffNotOverLoaded);

