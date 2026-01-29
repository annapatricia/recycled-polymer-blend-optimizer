import os
import pandas as pd


OUT_PATH = "outputs/tables/recycling_routes_assessment.csv"


def main():
    os.makedirs("outputs/tables", exist_ok=True)

    # Dados fictícios das rotas
    data = [
        {
            "route": "Mechanical recycling (standard)",
            "performance_index": 0.75,
            "energy_MJ_per_kg": 5.0,
            "CO2_kg_per_kg": 0.45,
            "water_L_per_kg": 2.0,
            "cost_index": 0.6,
        },
        {
            "route": "Mechanical recycling + compatibilizer",
            "performance_index": 0.90,
            "energy_MJ_per_kg": 6.0,
            "CO2_kg_per_kg": 0.55,
            "water_L_per_kg": 2.5,
            "cost_index": 0.7,
        },
        {
            "route": "Chemical recycling",
            "performance_index": 0.95,
            "energy_MJ_per_kg": 12.0,
            "CO2_kg_per_kg": 1.20,
            "water_L_per_kg": 6.0,
            "cost_index": 1.0,
        },
    ]

    df = pd.DataFrame(data)

    # Score simples (quanto maior, melhor)
    # desempenho pesa positivamente, impactos pesam negativamente
    df["sustainability_score"] = (
        2.0 * df["performance_index"]
        - 0.3 * df["energy_MJ_per_kg"]
        - 0.5 * df["CO2_kg_per_kg"]
        - 0.1 * df["water_L_per_kg"]
        - 0.4 * df["cost_index"]
    )

    df_sorted = df.sort_values("sustainability_score", ascending=False)
    df_sorted.to_csv(OUT_PATH, index=False)

    print("OK! Avaliação técnico-ambiental salva em:", OUT_PATH)
    print("\nRanking das rotas:")
    print(df_sorted.to_string(index=False))


if __name__ == "__main__":
    main()
