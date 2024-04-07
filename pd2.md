1.1

A) Brat

B) Kuzyn

C) Swaci

D) macocha

E) bracia przyrodni

F) Brat Męża

G) nie wiem

2.1

kobieta(X) :-
    osoba(X),
    \+m(X).

ojciec(X,Y) :-
    osoba(X),
    osoba(Y),
    m(X),
    rodzic(X,Y).

matka(X,Y) :-
    osoba(X),
    osoba(Y),
    kobieta(X),
    rodzic(X,Y).

corka(X,Y) :-
    osoba(X),
    osoba(Y),
    kobieta(X),
    rodzic(Y,X).

brat_rodzony(X,Y) :-
    osoba(X),
    osoba(Y),
    ojciec(Ojciec, X),
    ojciec(Ojciec, Y),
    matka(Matka, X),
    matka(Matka, Y),
    m(X).

brat_przyrodni(X,Y) :-
    osoba(X),
    osoba(Y),
    m(X),
    ((ojciec(Ojciec1, X), ojciec(Ojciec1,Y), matka(Matka1, X), \+matka(Matka1, Y)) ;
    (ojciec(Ojciec2, X), \+ojciec(Ojciec2,Y), matka(Matka2, X), matka(Matka2, Y))).

kuzyn(X,Y) :-
    osoba(X),
    osoba(Y),
    rodzic(Z, X), 
    rodzic(W, Y),
    brat_rodzony(Z, W).

dziadek_od_strony_ojca(X,Y) :-
    osoba(X),
    osoba(Y),
    rodzic(X, Z), 
    m(Z), 
    rodzic(Z, Y), 
    m(Y).

dziadek_od_strony_matki(X, Y) :- 
    osoba(X),
    osoba(Y),
    rodzic(X, Z), 
    kobieta(Z), 
    rodzic(Z, Y), 
    m(Y).

dziadek(X, Y) :- 
    osoba(X),
    osoba(Y),
    rodzic(X, Z), 
    rodzic(Z, Y), 
    m(Z).

babcia(X, Y) :-
    osoba(X),
    osoba(Y),
    rodzic(X, Z), 
    rodzic(Z, Y),
    kobieta(Z).

wnuczka(X, Y) :- 
    osoba(X),
    osoba(Y),
    rodzic(Y, Z), 
    rodzic(Z, X), 
    kobieta(X).

przodek_do2pokolenia_wstecz(X, Y) :- 
    osoba(X),
    osoba(Y),
    rodzic(X, Z), 
    rodzic(Z, Y).

przodek_do3pokolenia_wstecz(X, Y) :- 
    osoba(X),
    osoba(Y),
    rodzic(X, Z), 
    przodek_do2pokolenia_wstecz(Z, Y).

