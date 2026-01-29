import os
import pandas as pd


DOE_PATH = "outputs/tables/doe_plan_16_runs.csv"
OUT_PATH = "outputs/tables/doe_results_simulated.csv"


def simulate_row(r):
    # propriedades base fictícias
    E_PP, E_PE = 1400.0, 900.0
    sig_PP, sig_PE = 32.0, 22.0

    rPP = r["rPP_frac"]
    rPE = r["rPE_frac"]

    compat = r["compatibilizer_pct"]
    filler = r["filler_pct"]
    temp = r["process_temp_C"]

    filler_factor = 1 + 0.018 * filler
    compat_factor = 1 + 0.03 * (compat / 5)
    degradation = 1 - 0.10 * ((temp - 170) / 50)

    E_sim = (rPP * E_PP + rPE * E_PE) * filler_factor * compat_factor * degradation
    sigma_sim = (rPP * sig_PP + rPE * sig_PE) * compat_factor * degradation

    return E_sim, sigma_sim


def main():
    os.makedirs("outputs/tables", exist_ok=True)

    doe = pd.read_csv(DOE_PATH)

    E_list = []
    sig_list = []
    for _, r in doe.iterrows():
        E_sim, sigma_sim = simulate_row(r)
        E_list.append(E_sim)
        sig_list.append(sigma_sim)

    doe["E_sim_MPa"] = E_list
    doe["sigma_sim_MPa"] = sig_list

    # critério simples: score = força + (E/1000) pra equilibrar unidades
    doe["score"] = doe["sigma_sim_MPa"] + doe["E_sim_MPa"] / 1000.0

    doe_sorted = doe.sort_values("score", ascending=False)
    doe_sorted.to_csv(OUT_PATH, index=False)

    print("OK! Resultados DoE simulados salvos em:", OUT_PATH)
    print("\nTop 5 cenários (maior score):")
    print(doe_sorted.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
