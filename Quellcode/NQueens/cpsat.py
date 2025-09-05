from ortools.sat.python import cp_model
import time
import sys

def n_queens_cpsat(n: int) -> bool:
    model = cp_model.CpModel()
    Q = [model.NewIntVar(0, n - 1, f"q_{i}") for i in range(n)]
    model.AddAllDifferent(Q)

    d1 = [model.NewIntVar(0, 2 * n - 2, f"d1_{i}") for i in range(n)]
    d2 = [model.NewIntVar(0, 2 * n - 2, f"d2_{i}") for i in range(n)]
    for i in range(n):
        model.Add(d1[i] == Q[i] + i)
        model.Add(d2[i] == Q[i] - i + (n - 1))

    model.AddAllDifferent(d1)
    model.AddAllDifferent(d2)

    #model.AddDecisionStrategy(Q,  cp_model.CHOOSE_MIN_DOMAIN_SIZE, cp_model.SELECT_MIN_VALUE)
    #model.AddDecisionStrategy(d1 + d2, cp_model.CHOOSE_MIN_DOMAIN_SIZE, cp_model.SELECT_MIN_VALUE)

    solver = cp_model.CpSolver()

    #solver.parameters.num_workers = 1
    solver.parameters.random_seed = 12345
  
    status = solver.Solve(model)
    return status in (cp_model.OPTIMAL, cp_model.FEASIBLE)

def time_one_run(n: int) -> float:
    t0 = time.process_time()
    _ = n_queens_cpsat(n)
    t1 = time.process_time()
    return t1 - t0

def warmup_runs(n: int, m: int) -> None:
    for _ in range(max(0, m)):
        n_queens_cpsat(n)

def run_n(n: int, runs: int, warmup: int) -> None:
    warmup_runs(n, warmup)
    for i in range(1, runs + 1):
        t = time_one_run(n)
        print(f"{n}:{i}:{t:0.10f}", flush=True)

if __name__ == "__main__":
    size = int(sys.argv[1])
    num_runs = int(sys.argv[2])
    num_warmup = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    run_n(size, runs=num_runs, warmup=num_warmup)
