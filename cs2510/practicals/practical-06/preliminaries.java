class QueueOfIntegers {
	private LinkedList<Integer> items = new LinkedList<Integer>();
	private int queueLength;
	public QueueOfIntegers() {
		queueLength = 10;
	}
	public void push(Integer item) {
		items.addLast(item);
	}
	public Integer pop() {
		return items.removeFirst();
	}
	public boolean isEmpty() {
		return (items.size() == 0);
	}
}
