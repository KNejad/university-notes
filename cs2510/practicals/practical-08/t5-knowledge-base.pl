c(_,[],[]).
c(A,[A|As],[A|Bs]):- c(A,As,Bs).
c(A,[_|As],Bs):- c(A,As,Bs).
