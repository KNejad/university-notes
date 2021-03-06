// Need to import the LinkedList class from the java.util package
// Note, I'm using a linked list rather than an array list because
// it gives me methods such as removeFirst() and addLast()
import java.util.LinkedList;

class QueueOfIntegers {
	// Private data storage that can only be manipulated from within
	// the class
	private LinkedList<Integer> items = new LinkedList<Integer>();
	private int queueLength;

	/**
	 * A constructor for a queue of length 10
	 */
	public QueueOfIntegers() {
		queueLength = 10;
	}
	
	public QueueOfIntegers(int length) {
		queueLength = length;
	}

	/**
	 * Push an integer object onto the end of the queue
	 */
	public void push(Integer item) throws QueueFullException {
		if (items.size() == queueLength) {
			throw new QueueFullException();
		}
		items.addLast(item);
	}

	/**
	 * Pop an integer object off the front of the queue
	 */
	public Integer pop() throws QueueEmptyException {
		if (items.isEmpty()) {
			throw new QueueEmptyException();
		}
		return items.removeFirst();
	}

	/**
	 * Returns true if the queue is empty; false otherwise
	 */
	public boolean isEmpty() {
		return (items.size() == 0);
	}
}
