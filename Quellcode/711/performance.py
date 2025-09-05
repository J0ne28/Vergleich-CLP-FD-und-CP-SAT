import subprocess

# Konfiguration
runs = 100     # Anzahl Messläufe pro N
warmup = 5      # Warmup-Läufe


prolog_file = "clpfd.pl"
python_file = "cpsat.py"

output_prolog = "benchmark_clpfd.txt"
output_cpsat = "benchmark_cpsat.txt"

with open(output_prolog, "w") as f_clpfd, open(output_cpsat, "w") as f_cpsat:
    
        # --- Prolog ---
        prolog_cmd = [
            "swipl",
            "-q",
            "-g", f"repeat_test({runs + warmup}),halt.",
            prolog_file
        ]
        result_prolog = subprocess.run(
            prolog_cmd,
            capture_output=True,
            text=True
        )
        f_clpfd.write(result_prolog.stdout)
    

            # --- Python ---
        python_cmd = [
            "python",
            python_file,
            str(runs + warmup)
        ]
        result_python = subprocess.run(
            python_cmd,
            capture_output=True,
            text=True
        )
        f_cpsat.write(result_python.stdout)
print(f"Benchmark abgeschlossen.\nCLP(FD) in {output_prolog}\nCP-SAT in {output_cpsat}")
