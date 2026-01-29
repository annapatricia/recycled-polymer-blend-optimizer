import os
import numpy as np
import pandas as pd


def generate_fictitious_data(n_samples=200, seed=42):
    np.random.seed(seed)

    # Frações do blend (somam 1)
    rPP_frac = np.random.uniform(0.3, 0.9, n_samples)
    rPE_frac = 1.0 - rPP_frac

    # Aditivos e processo
    compatibilizer_pct = np.random.uniform(0.0, 5.0, n_samples)
    antioxidant_pct = np.random.uniform(0.0, 1.0, n_samples)
    filler_pct = np.random.uniform(0.0, 20.0, n_samples)

    process_temp = np.random.uniform(170, 220, n_samples)
    screw_speed = np.random.uniform(80, 250, n_samples)
    cooling_rate = np.random.uniform(5, 40, n_samples)

    # Propriedades base fictícias
    E_PP, E_PE = 1400, 900        # MPa
    sig_PP, sig_PE = 32, 22       # MPa
    Tg_PP, Tg_PE = -10, -120      # °C

    # Modelos simplificados (simulação)
    filler_factor = 1 + 0.018 * filler_pct
    compat_factor = 1 + 0.03 * (compatibilizer_pct / 5)
    degradation = 1 - 0.10 * ((process_temp - 170) / 50)

    E_sim = (rPP_frac * E_PP + rPE_frac * E_PE) * filler_factor * compat_factor * degradation
    sigma_sim = (rPP_frac * sig_PP + rPE_frac * sig_PE) * compat_factor * degradation
    Tg_sim = (rPP_frac * Tg_PP + rPE_frac * Tg_PE) + 0.1 * filler_pct + 2 * antioxidant_pct

    elong_sim = 120 * compat_factor * (1 - 0.02 * (filler_pct / 20)) * degradation

    # Dados "experimentais" = simulação + ruído
    E_exp = E_sim + np.random.normal(0, 60, n_samples)
    sigma_exp = sigma_sim + np.random.normal(0, 1.5, n_samples)
    Tg_exp = Tg_sim + np.random.normal(0, 3, n_samples)
    elong_exp = elong_sim + np.random.normal(0, 8, n_samples)

    df = pd.DataFrame({
        "rPP_frac": rPP_frac,
        "rPE_frac": rPE_frac,
        "compatibilizer_pct": compatibilizer_pct,
        "antioxidant_pct": antioxidant_pct,
        "filler_pct": filler_pct,
        "process_temp_C": process_temp,
        "screw_speed_rpm": screw_speed,
        "cooling_rate_Cmin": cooling_rate,
        "E_sim_MPa": E_sim,
        "sigma_sim_MPa": sigma_sim,
        "Tg_sim_C": Tg_sim,
        "elong_sim_pct": elong_sim,
        "E_exp_MPa": E_exp,
        "sigma_exp_MPa": sigma_exp,
        "Tg_exp_C": Tg_exp,
        "elong_exp_pct": elong_exp,
    })

    return df


if __name__ == "__main__":
    df = generate_fictitious_data()

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/formulations_fictitious.csv", index=False)

    print("Dataset fictício gerado com sucesso!")
    print(df.head())
