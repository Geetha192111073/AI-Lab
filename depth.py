Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
queens(N, Queens) :- length(Queens, N),
board(Queens, Board, 0, N, _, _), queens(Board, 0, Queens).

board([], [], N, N, _, _).
board([_|Queens], [Col-Vars|Board], Col0, N, [_|VR], VC) :- Col is Col0+1,
functor(Vars, f, N), constraints(N, Vars, VR, VC),
board(Queens, Board, Col, N, VR, [_|VC]).

constraints(0, _, _, _) :- !.
constraints(N, Row, [R|Rs], [C|Cs]) :- arg(N, Row, R-C),
M is N-1,
constraints(M, Row, Rs, Cs).

queens([], _, []).
queens([C|Cs], Row0, [Col|Solution]) :- Row is Row0+1,
select(Col-Vars, [C|Cs], Board), arg(Row, Vars, Row-Row), queens(Board, Row, Solution).
... % solve( Node, Solution):
... %	Solution is an acyclic path (in reverse order) between Node and agoal
... 
... solve( Node, Solution) :- depthfirst( [], Node, Solution).
... 
... % depthfirst( Path, Node, Solution):
... % extending the path [Node | Path] to a goal gives Solution
... 
... depthfirst( Path, Node, [Node | Path] ) :- goal( Node).
... 
... depthfirst( Path, Node, Sol) :- s( Node, Node1),
... \+ member(Node1,Path),	% Prevent a cycle depthfirst( [Node | Path], Node1,Sol).
... 
... depthfirst2( Node, [Node], _) :- goal( Node).
... 
... depthfirst2( Node, [Node | Sol], Maxdepth) :- Maxdepth> 0,
... s( Node, Node1),
... Max1 is Maxdepth - 1, depthfirst2( Node1, Sol, Max1).
... 
... 
... goal(f).
... goal(j).
... s(a,b).
... s(a,c).
... s(b,d).
... s(b,e).
... s(c,f).
... s(c,g).
... s(d,h).
... s(e,i).
... s(e,j).
... 
... 
... 
... 
... 
... 
... 
... 
