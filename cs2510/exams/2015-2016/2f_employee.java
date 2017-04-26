// Filename : Employee . java
public class Employee extends Person {
	private double salary ;
	public Employee ( String n , double s ) {
		super ( n ) ;
		salary = s ;
	}
	public String toString () {
		return " Employee " + getName () + " has salary " +
			salary ;
	}
}
