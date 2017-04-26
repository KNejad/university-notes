c(X,[X|Ys],S):- S = S + 1, c(X,Ys,S).
c(_,[_|Xs],S):- c(_,Xs,S).
c(_,[],0).
