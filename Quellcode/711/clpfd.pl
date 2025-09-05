:- use_module(library(clpfd)).

seven_eleven :-
    Vars = [A, B, C, D],
    Vars ins 1..711,
    A + B + C + D #= 711,
    A * B * C * D #= 711*100^3,
    labeling([ff], Vars).

repeat_test(N) :-
    findall(Time,
        (between(1, N, I),
         ( I >= 6 ->
             statistics(cputime, T0),
             once(seven_eleven),
             statistics(cputime, T1),
             Time is T1 - T0,
             format('~d:~3f~n', [I-5, Time])
           ; % else Warmup
             once(seven_eleven),
             Time = warmup
         )
        ),
        Times).
    % Warmup-Zeiten herausfiltern
    %exclude(==(warmup), Times, FilteredTimes),
    %sorted_times_info(FilteredTimes).

sorted_times_info(Times) :-
    msort(Times, Sorted),
    length(Sorted, Len),
    sum_list(Sorted, Sum),
    Avg is Sum / Len,
    nth1(1, Sorted, Min),
    last(Sorted, Max),
    (   0 is Len mod 2
    ->  I1 is Len // 2, I2 is I1 + 1,
        nth1(I1, Sorted, M1),
        nth1(I2, Sorted, M2),
        Median is (M1 + M2) / 2
    ;   I is (Len + 1) // 2,
        nth1(I, Sorted, Median)
    ),
    format('Min: ~3f s, Max: ~3f s, Median: ~3f s, Avg: ~3f s~n', [Min, Max, Median, Avg]).
