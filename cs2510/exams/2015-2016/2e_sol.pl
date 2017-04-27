c(X,[X|Ys],S):-  c(X,Ys,Z), S is Z + 1.
c(_,[_|Xs],S):- c(_,Xs,S).
c(_,[],0).
