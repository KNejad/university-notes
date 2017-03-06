/**
 * Author: Tim Norman
 * Date: 2016/02/23
 */

import java.io.Console;
import java.util.Random;

public class TaskGenerationThread implements Runnable {
	Queue<Task> taskqueue;

	public TaskGenerationThread (Queue<Task> tq) {
		taskqueue = tq;
	}

	public void run() {
		Console console = System.console();
		char choice = 'c';
		console.printf("Welcome to the task queue.\nYou can:\n\t- create a random SumTask (option \'s\');\n\t - create a random ProdTask (option \'p\');\n\t - create a random StringTask (option \'t\'); or\n\t- quit the programme (option \'q\')\n\n");
		while (choice != 'q') {
			try{
				choice = console.readLine("Please enter an option (s/t/p/q): ").charAt(0);
			}
			catch (StringIndexOutOfBoundsException e) {
				// Make the choice invalid if nothing is input
				choice = 'c';
			}
			switch (choice) {
				case 's':
					try {
						taskqueue.push( new SumTask( getNumArray() ));
					}
					catch (QueueFullException e) {
						System.out.println("Sorry, the queue is full...\n\n");
					}
					catch (Exception e) {
						System.err.println("Unexpected exception in TaskThreadGenerator\n");
					}
					break;
				case 't':
					try {
						taskqueue.push( new StringTask( getString() ));
					}
					catch (QueueFullException e) {
						System.out.println("Sorry, the queue is full...\n\n");
					}
					catch (Exception e) {
						System.err.println("Unexpected exception in the bagging area!\n");
					}
					break;
				case 'p':
					try {
						taskqueue.push( new ProdTask( getNumArray() ));
					}
					catch (QueueFullException e) {
						System.out.println("Sorry, the queue is full...\n\n");
					}
					catch (Exception e) {
						System.err.println("Unexpected exception in the bagging area!\n");
					}
					break;
				case 'q':
					console.printf("Bye!\n\n");
					break;
				default:
					console.printf("Unrecognised option; please try again.\n\n");
					break;		
			}
		}
	}

	private String getString() {
		String MYCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		StringBuilder s = new StringBuilder();
		Random rand = new Random();
		while (s.length() < 18) {
			s.append(MYCHARS.charAt( rand.nextInt(MYCHARS.length()) ));
		}
		return s.toString();
	}

	private int[] getNumArray() {
		Random rand = new Random();
		int[] anArray = new int[10];
		for (int i=0; i<anArray.length; i++) {
			anArray[i] = rand.nextInt(20);
		}
		return anArray;
	}
}
