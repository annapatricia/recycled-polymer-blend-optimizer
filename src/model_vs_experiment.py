import os
import pandas as pd
import matplotlib.pyplot as plt

PATH = "data/processed/formulations_processed.csv"
OUT_FIG = "outputs/figures/sim_vs_exp_strength.png"

def main():
    df = pd.read_csv(PATH)

    os.makedirs("outputs/figures", exist_ok=True)

    x = df["sigma_sim_MPa"]
    y = df["sigma_exp_MPa"]

    plt.figure()
    plt.scatter(x, y)

    # Linha y = x (modelo perfeito)
    min_v = min(x.min(), y.min())
    max_v = max(x.max(), y.max())
    plt.plot([min_v, max_v], [min_v, max_v])

    plt.xlabel("Simulated strength (MPa)")
    plt.ylabel("Experimental strength (MPa)")
    plt.title("Simulated vs Experimental Strength")
    plt.tight_layout()

    plt.savefig(OUT_FIG, dpi=150)
    plt.close()

    print("OK! Figura salva em:", OUT_FIG)

if __name__ == "__main__":
    main()
