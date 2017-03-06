/**
 * Author: Tim Norman
 * Date: 2016/02/23
 *
 * Note that because I am using the standard input and output for both
 * threads there will be some interaction between them on the
 * console. This should be fixed using a simple interface using two
 * output streams, one for each thread. This would require the output
 * stream to which the information is sent to be a member variable of
 * the task class, so requires some restructuring of the example.
 */

public class RunTasks {

    public static final void main(String[] args) {
	// Create the task queue
	Queue<Task> myTasks = new Queue<Task>();
	Thread processor = new Thread( new TaskProcessingThread( myTasks ) );
	processor.start();
	Thread generator = new Thread( new TaskGenerationThread( myTasks ) );
	generator.start();

	// Simply wait for both threads to complete (depends on user
	// exiting generator, and not the most elegant solution)
	try {
	    processor.join();
	    generator.join();
	}
	catch (InterruptedException e) {
	    System.err.println("Some unknown thread error occurred");
	}
    }
}
