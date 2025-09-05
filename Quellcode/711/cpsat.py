from ortools.sat.python import cp_model
import time
import sys

def solve_711():
    model = cp_model.CpModel()

    max_price = 711
    prices = [model.NewIntVar(1, max_price, f'p{i}') for i in range(4)]

    model.Add(sum(prices) == 711)

    target_product = 711 * 100**3
    product = model.NewIntVar(1, target_product, 'product')
    model.AddMultiplicationEquality(product, prices)
    model.Add(product == target_product)

    #model.AddDecisionStrategy(
    #    prices,
    #    cp_model.CHOOSE_MIN_DOMAIN_SIZE,
    #    cp_model.SELECT_MIN_VALUE
    #)

    #solver.parameters.num_workers = 1

    solver = cp_model.CpSolver()   
    solver.parameters.random_seed = 12345
    start_cpu = time.process_time()
    status = solver.Solve(model)
    end_cpu = time.process_time()

    cpu_time = end_cpu - start_cpu

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        solution = [solver.Value(p) for p in prices]
        return cpu_time, solution
    else:
        return cpu_time, None

def run_benchmark(n):
    times = []

    for i in range(1, n+1):
        cpu_time, solution = solve_711()
        if (i >= 6):
            times.append(cpu_time)
            print(f"{i-5}:{cpu_time:.4f}")
        



if __name__ == '__main__':
    if len(sys.argv) > 1: 
        run_benchmark(sys.argv[1])
