import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def read_nqueens(file: str):
    d = defaultdict(list)
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if "load" in line or ":" not in line: 
                continue
            n_str, _, t_str = line.strip().split(":")
            d[int(n_str)].append(float(t_str))
    return d

clpfd = read_nqueens("benchmark_clpfd.txt")
v1    = read_nqueens("benchmark_cpsat_1thread_ff.txt")
v2    = read_nqueens("benchmark_cpsat_1thread.txt")
v3    = read_nqueens("benchmark_cpsat_xthread.txt")

Ns = sorted(set(clpfd)&set(v1)&set(v2)&set(v3))
def stats(d): 
    mu = [np.mean(d[n]) for n in Ns]
    sd = [np.std(d[n])  for n in Ns]
    return mu, sd

m1,s1 = stats(clpfd)
m2,s2 = stats(v1)
m3,s3 = stats(v2)
m4,s4 = stats(v3)

fig, axes = plt.subplots(4, 1, figsize=(10,10), sharex=True, sharey=False)

axes[0].errorbar(Ns, m1, yerr=s1, marker="o",  capsize=3)
axes[0].set_title("CLP(FD)")

axes[1].errorbar(Ns, m2, yerr=s2, marker="s",  capsize=3, linestyle="--")
axes[1].set_title("Variante 1")

axes[2].errorbar(Ns, m3, yerr=s3, marker="^",  capsize=3, linestyle=":")
axes[2].set_title("Variante 2")

axes[3].errorbar(Ns, m4, yerr=s4, marker="x",  capsize=3, linestyle="-.")
axes[3].set_title("Variante 3")
axes[3].set_xlabel("N (Schachbrettgröße)")
for ax in axes:
    ax.set_ylabel("CPU-Zeit (s)")
    ax.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout(rect=[0,0,1,0.96])
plt.show()
