import subprocess
import sys

# Konfiguration
n_start = 25
n_end = 50
runs = 100       # Anzahl Messläufe pro N
warmup = 5       # Warmup-Läufe

prolog_file = "clpfd.pl"
python_file = "cpsat.py"

output_prolog = "benchmark_clpfd.txt"
output_cpsat = "benchmark_cpsat.txt"

with open(output_prolog, "w") as f_clpfd, open(output_cpsat, "w") as f_cpsat:
    for n in range(n_start, n_end + 1):
        print(f"--- N = {n} ---")

        # --- Prolog ---
        prolog_cmd = [
            "swipl",
            "-q",
            "-g", f"run_n({n},{runs},{warmup}),halt.",
            prolog_file
        ]
        result_prolog = subprocess.run(
            prolog_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        sys.stdout.write(result_prolog.stdout)
        f_clpfd.write(result_prolog.stdout)
        if result_prolog.stderr:
            sys.stderr.write(result_prolog.stderr)

        # --- Python ---
        python_cmd = [
            "python",
            python_file,
            str(n),
            str(runs),
            str(warmup)
        ]
        result_python = subprocess.run(
            python_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        sys.stdout.write(result_python.stdout)
        f_cpsat.write(result_python.stdout)
        if result_python.stderr:
            sys.stderr.write(result_python.stderr)

print(f"Benchmark abgeschlossen.\nCLP(FD) in {output_prolog}\nCP-SAT in {output_cpsat}")
