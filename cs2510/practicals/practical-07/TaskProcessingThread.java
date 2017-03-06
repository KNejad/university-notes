/**
 * Author: Tim Norman
 * Date: 2016/02/23
 */

public class TaskProcessingThread implements Runnable {
    Queue<Task> taskqueue;

    public TaskProcessingThread (Queue<Task> tq) {
	taskqueue = tq;
    }

    public void run() {
	// This thread will poll the queue 5 times
	int polls = 1;
	while (polls > 0) {
	    try {
		// Sleep for 10 seconds
		Thread.sleep(10000);
		// Execute all the pending tasks on the queue
		System.out.println("Checking task queue...\n\n");
		while (!taskqueue.isEmpty()) {
		    taskqueue.pop().execute();
		}
	    }
	    catch (InterruptedException e) {
		System.err.println("A problem with the thread.");
	    }
	    catch (QueueEmptyException e) {
		System.err.println("Tried to pop element off an empty queue.");
	    }
	    catch (Exception e) {
		System.err.println("Unexpected exception in TaskProcessingThread");
	    }
	    polls--;
	}
    }
}
