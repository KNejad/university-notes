/**
 * Author: Tim Norman
 * Date: 2016/02/23
 */

public class StringTask extends Task {
	private String theString;
	private int number;
	private static final String taskType = "StringTask";

	public StringTask(String s) {
		theString = s;
		number = 5;
	}

	public void execute() {
		System.out.println("Executing a StringTask task");
		for (int i=0; i<number; i++) {
			System.out.println(theString);
		}
	}
}
