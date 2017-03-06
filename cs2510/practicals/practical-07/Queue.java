/**
 * Author: Tim Norman
 * Date: 2016/02/23
 */

// Need to import the LinkedList class from the java.util package
import java.util.LinkedList;

class Queue<T> {
    // Private data storage that can only be manipulated from within
    // the class. 
    private LinkedList<T> items = new LinkedList<T>();
    private int queueLength;

    /**
     * A default constructor; queue length 10
     */
    public Queue() {
	queueLength = 10;
    }

    /**
     * A constructor through which the queue length can be set
     */
    public Queue(int length) {
	queueLength = length;
    }

    /**
     * Push an object onto the end of the queue.
     *
     * Note that all methods that read/write items need to be
     * synchronized so that there are no read/write access conflicts
     * between multiple threads.
     */
    public synchronized void push(T item) throws QueueFullException {
	if (items.size() == 10) {
	    throw new QueueFullException();
	}
	items.addLast(item);
    }

    /**
     * Pop an object off the front of the queue
     */
    public synchronized T pop() throws QueueEmptyException {
	if (items.isEmpty()) {
	    throw new QueueEmptyException();
	}
	return items.removeFirst();
    }

    /**
     * Returns true if the queue is empty; false otherwise
     */
    public synchronized boolean isEmpty() {
	return (items.size() == 0);
    }
}
