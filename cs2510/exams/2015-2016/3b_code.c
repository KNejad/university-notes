void f( void ) {
	int x, y;
	/* Definition 1 */
	...
		while (...) {
			int y, z;
			/* Definition 2 */
			...
				while (...) {
					int z, w;
					/* Definition 3 */
					...
				}
			...
				/* Point 1 */
				/* Point 2 */
		}
	...
}
