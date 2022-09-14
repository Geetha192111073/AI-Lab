Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> route(Town1,Town2,Distance) road(Town1,Town2,Distance). route(Town1,Town2,Distance) road(Town1,X,Dist1),
...  	route(X,Town2,Dist2), 
...  	Distance=Dist1+Dist2, domains
...  town= symbol distance =integer
... 
...  predicates
...  nondeterm road(town,town,distance) nondetermroute(town,town,distance)
... 
...  clauses
...  road("tampa","houston",200).
...  road("gordon","tampa",300).
...  road("houston","gordon",100).
...  	road("houston","kansas_city",120). 
...  	road("gordon","kansas_city",130).
...  route(Town1,Town2,Distance):-
...  road(Town1,Town2,Distance). route(Town1,Town2,Distance):-
...  road(Town1,X,Dist1), route(X,Town2,Dist2),
... goal
...  
... Distance=Dist1+Dist2,
... !.
...  route("tampa", "kansas_city",X),
... write("Distance from Tampa to Kansas City is ",X),nl.
... Distance from Tampa to Kansas City is 320 X=320
... 1 Solution
