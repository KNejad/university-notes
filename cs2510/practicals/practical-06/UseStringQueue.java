import java.io.Console;

public final class UseStringQueue {

	public static final void main(String[] args) {
		Queue thequeue = new Queue();
		Console console = System.console();
		char choice = 'c';
		console.printf("Welcome to the queue.\nYou can:\n\t- add element to the queue (option \'a\');\n\t- remove one element from the queue (option \'r\');\n\t- process the whole queue (option \'p\'); or\n\t- quit the programme (option \'q\')\n\n");
		while (choice != 'q') {
			try {
				choice = console.readLine("Please enter an option (a/r/p/q): ").charAt(0);
			}
			catch (StringIndexOutOfBoundsException e) {
				// Make the choice invalid if nothing is input
				choice = 'c';
			}
			switch (choice) {
				case 'a':
					try {
						thequeue.push(console.readLine("Please enter a string: "));
					}
					catch (NumberFormatException e) {
						console.printf("Sorry, you have to enter a string!\n\n");
					}
					catch (QueueFullException e) {
						console.printf("Sorry, the queue is full!\n\n");
					}
					catch (Exception e) {
						console.printf("Unknown problem, please try again.\n\n");
					}
					break;
				case 'r':
					try {
						console.printf("Processing front of queue: %1$s\n\n",thequeue.pop());
					}
					catch (QueueEmptyException e) {
						console.printf("Sorry, the queue is empty!\n\n");
					}
					catch (Exception e) {
						console.printf("Unknown problem, please try again.\n\n");
					}
					break;
				case 'p':
					try {
						while (!thequeue.isEmpty()) {
							console.printf("Processing front of queue: %1$s\n",thequeue.pop());
						}
						console.printf("End\n\n");
					}
					catch (Exception e) {
						// We should never get a QueueEmpty Exception here
						console.printf("Unknown problem, please try again.\n\n");
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
}

