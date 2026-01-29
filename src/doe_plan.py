import os
import itertools
import pandas as pd
import numpy as np


OUT_PATH = "outputs/tables/doe_plan_16_runs.csv"


def main():
    os.makedirs("outputs/tables", exist_ok=True)

    # 4 fatores em 2 níveis (baixo/alto)
    factors = {
        "compatibilizer_pct": [0.5, 4.5],   # baixo, alto
        "filler_pct": [2.0, 18.0],
        "process_temp_C": [175.0, 215.0],
        "cooling_rate_Cmin": [8.0, 35.0],
    }

    # mantém blend fixo e alguns defaults (para simplificar)
    fixed = {
        "rPP_frac": 0.65,
        "rPE_frac": 0.35,
        "antioxidant_pct": 0.4,
        "screw_speed_rpm": 150.0,
    }

    # produto cartesiano (2^4 = 16)
    keys = list(factors.keys())
    combos = list(itertools.product(*[factors[k] for k in keys]))

    rows = []
    for combo in combos:
        row = dict(zip(keys, combo))
        row.update(fixed)
        rows.append(row)

    doe = pd.DataFrame(rows)
    doe.to_csv(OUT_PATH, index=False)

    print("OK! Plano DoE salvo em:", OUT_PATH)
    print(doe.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
