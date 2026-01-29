import os
import pandas as pd
import matplotlib.pyplot as plt

PATH = "data/processed/formulations_processed.csv"
OUT_FIG = "outputs/figures/compat_vs_strength.png"

def main():
    print("Lendo:", PATH)
    df = pd.read_csv(PATH)
    print("OK, linhas:", len(df))

    os.makedirs("outputs/figures", exist_ok=True)
    print("Salvando figura em:", OUT_FIG)

    plt.figure()
    plt.scatter(df["compatibilizer_pct"], df["sigma_exp_MPa"])
    plt.xlabel("compatibilizer_pct (%)")
    plt.ylabel("sigma_exp_MPa (MPa)")
    plt.title("Compatibilizer vs Experimental Strength")
    plt.tight_layout()

    plt.savefig(OUT_FIG, dpi=150)
    plt.close()
    print("OK! Figura salva.")

if __name__ == "__main__":
    main()
