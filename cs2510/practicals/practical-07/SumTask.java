/**
 * Author: Tim Norman
 * Date: 2016/02/23
 */

public class SumTask extends Task {
	private int[] numbers;
	private static final String taskType = "SumTask";
	public SumTask(int[] nums) {
		numbers = nums;
	}

	public void execute() {
		// Execute the default behaviour
		super.execute();
		int sum = 0;
		for (int i=0; i<numbers.length; i++) {
			sum += numbers[i];
		}
		System.out.println("Sum = " + sum);
	}
}
