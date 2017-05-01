list_max([H|T], X) :- list_max(T,H, X).


list_max([],M,M).
list_max([H|T],M,X) :- H<M, list_max(T,M,X).
list_max([H|T],M,X) :- H>=M, list_max(T,H,X).
