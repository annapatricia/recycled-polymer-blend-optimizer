import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm


PATH = "data/processed/formulations_processed.csv"


def main():
    df = pd.read_csv(PATH)

    # Variáveis
    y_exp = df["sigma_exp_MPa"]
    y_sim = df["sigma_sim_MPa"]

    # =========================
    # 1) ERRO DO MODELO (RMSE)
    # =========================
    rmse = np.sqrt(mean_squared_error(y_exp, y_sim))
    print("RMSE (MPa):", round(rmse, 3))

    # =========================
    # 2) REGRESSÃO LINEAR
    # exp = a + b * sim
    # =========================
    X = sm.add_constant(y_sim)   # adiciona intercepto
    model = sm.OLS(y_exp, X).fit()

    print("\n=== REGRESSÃO LINEAR ===")
    print(model.summary())

    # Coeficientes principais
    intercept, slope = model.params
    print("\nIntercepto:", round(intercept, 3))
    print("Inclinação:", round(slope, 3))


if __name__ == "__main__":
    main()
