/**
 * Author: Tim Norman
 * Date: 2016/02/23
 */

public class ProdTask extends Task {
	private int[] numbers;
	private static final String taskType = "ProdTask";

	public ProdTask(int[] nums) {
		numbers = nums;
	}

	public void execute() {
		// Execute the default behaviour
		super.execute();
		int product = 1;
		for (int i=0; i<numbers.length; i++) {
			product = product * numbers[i];
		}
		System.out.println("Product = " + product);
	}
}
