import matplotlib.pyplot as plt
import numpy as np


def read_data(file: str):
    data = []
    with open(file, "r") as f:
        for line in f:
            if "load" not in line:
                run_num, time_str = line.strip().split(":")
                run_num = int(run_num)
                run = float(time_str)
                while len(data) < run_num:
                    data.append(None)
                data[run_num-1] = run
    return data



data_cpsat_1thread_ff = read_data("./benchmark_cpsat_1thread_ff.txt")
data_cpsat_1thread = read_data("./benchmark_cpsat_1thread.txt")
data_cpsat_xthread = read_data("./benchmark_cpsat_xthread.txt")
data_clpfd = read_data("./benchmark_clpfd.txt")

datasets = [
    data_clpfd,
    data_cpsat_1thread_ff,
    data_cpsat_1thread,
    data_cpsat_xthread
]

labels = ["CLP(FD)", "Variante 1", "Variante 2", "Variante 3"]

means = [np.mean(d) for d in datasets]
stds  = [np.std(d) for d in datasets]

x = np.arange(len(labels))

plt.figure(figsize=(10, 6))
plt.bar(x, means, yerr=stds, capsize=8, tick_label=labels)
plt.ylabel("CPU-Zeit (s)")
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

