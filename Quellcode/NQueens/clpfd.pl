:- use_module(library(clpfd)).

queens(N, Qs) :-
    length(Qs, N),
    Qs ins 1..N,
    all_distinct(Qs),
    safe_diagonals(Qs),
    labeling([ff], Qs).

safe_diagonals(Qs) :-
    length(Qs, N),
    numlist(1, N, Is),
    maplist(sum_index,  Qs, Is, D1),
    maplist(diff_index, Qs, Is, D2),
    all_distinct(D1),
    all_distinct(D2).

sum_index(Q, I, S)  :- S #= Q + I.
diff_index(Q, I, D) :- D #= Q - I.

% Warmup & Messung

% Ungemessene Warmups (M >= 0)
warmup_runs(_, 0) :- !.
warmup_runs(N, M) :-
    M > 0,
    once(queens(N, _)),
    M1 is M - 1,
    warmup_runs(N, M1).

% Ein Messlauf
time_one_run(N, CpuSeconds) :-
    statistics(cputime, T0),
    once(queens(N, _)),
    statistics(cputime, T1),
    CpuSeconds is T1 - T0.

% X Messläufe, pro Lauf ausgeben: "N:Lauf:Zeit"
run_times_print(_, 0, _) :- !.
run_times_print(N, I, Total) :-
    I > 0,
    time_one_run(N, T),
    K is Total - I + 1,
    format("~w:~w:~10f~n", [N, K, T]),
    I1 is I - 1,
    run_times_print(N, I1, Total).

% Einstieg: run_n(N, Runs, Warmup)
run_n(N, Runs, Warmup) :-
    warmup_runs(N, Warmup),
    run_times_print(N, Runs, Runs),
    !.
