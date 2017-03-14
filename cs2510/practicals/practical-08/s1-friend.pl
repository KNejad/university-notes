% This is a comment (vim only recognises it as prolog if it starts with a comment)
rich(bill).
rich(arnie).
famous(bill).
friend(X):- rich(X),famous(X).
enemy(Y):- \+ friend(Y). %This will not return arnie if you execute enemy(X) because everything is an enemy including hgiwg
