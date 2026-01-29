# Recycled Polymer Blend Optimizer

This project demonstrates a complete computational and data-driven workflow
to support material selection, simulation, experimental analysis, and
sustainability assessment of recycled polymer blends.

The project was designed to mimic an industrial R&D environment, integrating
simplified simulation models, statistical analysis, Design of Experiments (DoE),
and techno-environmental evaluation to support technical decision-making and
reduce experimental effort.

---

## 🎯 Project Objectives
- Support the selection of recycled polymer blends, additives, and compatibilizers
- Simulate mechanical and thermal behavior using simplified physical models
- Integrate simulation results with experimental data
- Quantify model accuracy using statistical metrics and regression
- Apply Design of Experiments (DoE) to reduce the number of experimental tests
- Compare recycling routes from a technical and environmental perspective
- Produce clear technical documentation to support decision-making

---

## 🧪 Workflow Overview

1. **Data Generation**
   - Creation of fictitious datasets representing recycled polymer formulations
   - Generation of simulated and experimental mechanical properties

2. **Data Processing & Validation**
   - Sanity checks on formulation constraints
   - Separation between raw and processed datasets

3. **Exploratory Data Analysis**
   - Visualization of relationships between formulation variables and properties

4. **Simulation vs Experimental Integration**
   - Comparison of simulated and experimental results
   - Visual and numerical evaluation of model performance

5. **Statistical Analysis & Model Evaluation**
   - RMSE calculation to quantify model error
   - Linear regression to assess bias and statistical significance

6. **Design of Experiments (DoE)**
   - 2-level factorial DoE with 16 experimental runs
   - Prioritization of optimal formulations based on simulated performance

7. **Techno-Environmental Assessment**
   - Comparison of mechanical and chemical recycling routes
   - Multi-criteria sustainability scoring to support decision-making

8. **Technical Reporting**
   - Consolidation of results into a structured technical report

---

## 📁 Project Structure
```
recycled-polymer-blend-optimizer/
│
├─ data/
│ ├─ raw/ # Raw fictitious datasets
│ ├─ processed/ # Cleaned and validated datasets
│
├─ src/
│ ├─ data_generation.py
│ ├─ preprocess.py
│ ├─ eda_basic.py
│ ├─ model_vs_experiment.py
│ ├─ model_evaluation.py
│ ├─ doe_plan.py
│ ├─ doe_simulate.py
│ └─ env_assessment.py
│
├─ outputs/
│ ├─ figures/ # Generated plots
│ ├─ tables/ # DoE and sustainability results
│ └─ report_final.md
│
├─ requirements.txt
└─ README.md
```


