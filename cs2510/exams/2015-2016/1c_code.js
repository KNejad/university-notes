var a, b;
function f() {
	console.log(a);
	console.log(b);
}
function g() {
	var a;
	a = 20;
	b = 5
	f();
}
a = 10;
b = 7;
g();
