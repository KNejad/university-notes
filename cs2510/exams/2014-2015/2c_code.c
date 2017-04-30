void fun (int first, int second) {
	first += first;
	second += second;
}
void main() {
	int list[2] = {1, 3};
	fun(list[0], list[1]);
}
