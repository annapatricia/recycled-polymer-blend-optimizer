import os
import pandas as pd


RAW_PATH = "data/raw/formulations_fictitious.csv"
OUT_PATH = "data/processed/formulations_processed.csv"


def main():
    df = pd.read_csv(RAW_PATH)

    print("=== INFO BÁSICA ===")
    print("Linhas:", len(df))
    print("Colunas:", df.shape[1])
    print(df.dtypes)

    print("\n=== CHECAGENS ===")

    # 1) Ver se tem valores faltando
    missing = df.isna().sum().sum()
    print("Total de valores faltando:", missing)

    # 2) Checar se rPP_frac + rPE_frac ~ 1
    frac_sum = df["rPP_frac"] + df["rPE_frac"]
    max_error = (frac_sum - 1).abs().max()
    print("Erro máximo na soma das frações (deveria ser ~0):", max_error)

    # 3) Checar limites esperados (sanidade)
    checks = {
        "compatibilizer_pct": (0.0, 5.0),
        "antioxidant_pct": (0.0, 1.0),
        "filler_pct": (0.0, 20.0),
        "process_temp_C": (170.0, 220.0),
        "screw_speed_rpm": (80.0, 250.0),
        "cooling_rate_Cmin": (5.0, 40.0),
    }

    for col, (lo, hi) in checks.items():
        bad = df[(df[col] < lo) | (df[col] > hi)]
        print(f"{col}: fora do intervalo = {len(bad)}")

    # (opcional) Arredondar para ficar mais "bonito" no CSV
    df = df.round(4)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print("\nOK! Salvei dataset processado em:", OUT_PATH)
    print("\nPrévia (3 linhas):")
    print(df.head(3).to_string(index=False))


if __name__ == "__main__":
    main()
