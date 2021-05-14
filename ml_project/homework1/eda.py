from pathlib import Path
from textwrap import dedent

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

DATA_PATH = "data/raw/heart.csv"
PLOTS_DIR = "reports/figures"


def main():
    dataset_description = """
    # 1. Dataset Description
    <br>
    **Context**
    This database contains 76 attributes, but all published
    experiments refer to using a subset of 14 of them. In particular,
    the Cleveland database is the only one that has been used by
    ML researchers to this date. The "goal" field refers to the
    presence of heart disease in the patient.
    It is integer valued from 0 (no presence) to 4.
    <br>
    **Content**
    Attribute Information:
    <br>
    - age
    - sex
    - chest pain type (4 values)
    - resting blood pressure
    - serum cholestoral in mg/dl
    - fasting blood sugar > 120 mg/dl
    - resting electrocardiographic results (values 0,1,2)
    - maximum heart rate achieved
    - exercise induced angina
    - oldpeak = ST depression induced by exercise relative to rest
    - the slope of the peak exercise ST segment
    - number of major vessels (0-3) colored by flourosopy
    - thal: 3 = normal; 6 = fixed defect; 7 = reversable defect
    The names and social security numbers of the patients were
    recently removed from the database, replaced with dummy values.
    <br>
    One file has been "processed", that one containing the Cleveland
    database. All four unprocessed files also exist in this directory.
    <br>
    To see Test Costs (donated by Peter Turney), please see the folder "Costs"
    <br>
    **Acknowledgements**
    __Creators:__
    <br>
    Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
    University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
    University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
    V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:
    Robert Detrano, M.D., Ph.D.
    __Donor:__
    David W. Aha (aha '@' ics.uci.edu) (714) 856-8779
    <br>
    __Inspiration:__
    Experiments with the Cleveland database have concentrated on simply
    attempting to distinguish presence (values 1,2,3,4) from absence (value 0).
    <br>
    See if you can find any other trends in heart data to predict certain
    cardiovascular events or find any clear indications of heart health.
    """
    print(dedent(dataset_description))

    data = pd.read_csv(DATA_PATH)

    print("# 2. Data Overview")
    print(data.head(10).to_markdown())

    print("# 3 Real Features EDA")
    real_features = ["age", "chol", "oldpeak", "thalach", "trestbps"]
    sns_plot = sns.pairplot(data[real_features + ["target"]], hue="target")
    filename = "pairplot.png"
    fig_path = Path(f"{PLOTS_DIR}/{filename}").absolute()
    sns_plot.savefig(fig_path)
    print(f"![pairplot]({fig_path})")

    print("# 4. Categorical Features EDA")
    age_cohort = [
        "0-4",
        "5-9",
        "10-14",
        "15-19",
        "20-24",
        "25-29",
        "30-34",
        "35-39",
        "40-44",
        "45-49",
        "50-54",
        "55-59",
        "60-64",
        "65-69",
        "70-74",
        "75-79",
        "80-84",
        "85-89",
        "90-94",
        "95-99",
        "100+",
    ]
    age_coh_vals = [
        tuple(map(int, coh.replace("+", "-1000").split("-", 1))) for coh in age_cohort
    ]
    gentlemen = [
        data[(data.sex == 1) & (data.age.between(coh[0], coh[1]))]["age"].count()
        for coh in age_coh_vals
    ]
    ladies = [
        data[(data.sex == 0) & (data.age.between(coh[0], coh[1]))]["age"].count() * (-1)
        for coh in age_coh_vals
    ]

    df = pd.DataFrame({"age": age_cohort, "ladies": ladies, "gentlemen": gentlemen})

    plt.figure(figsize=(16, 8))
    bar_plot = sns.barplot(
        x="ladies",
        y="age",
        label="ladies",
        data=df,
        order=age_cohort[::-1],
        color="Salmon",
    )
    bar_plot = sns.barplot(
        x="gentlemen",
        y="age",
        label="gentlemen",
        data=df,
        order=age_cohort[::-1],
        color="LightSKyBlue",
    )
    bar_plot.set(
        xlabel="Quantity",
        ylabel="Age-Group",
        title="Population Pyramid of Dataset Sample",
    )
    plt.legend()
    filename = "bar1.png"
    fig_path = Path(f"{PLOTS_DIR}/{filename}").absolute()
    fig = bar_plot.get_figure()
    fig.savefig(fig_path)
    print(f"![bar1]({fig_path})")

    df["good"] = [
        data[(data.target == 0) & (data.age.between(coh[0], coh[1]))]["age"].count()
        for coh in age_coh_vals
    ]
    df["bad"] = [
        data[(data.target == 1) & (data.age.between(coh[0], coh[1]))]["age"].count()
        * (-1)
        for coh in age_coh_vals
    ]

    plt.figure(figsize=(16, 8))
    bar_plot = sns.barplot(
        x="bad",
        y="age",
        label="+ hearth disease",
        data=df,
        order=age_cohort[::-1],
        color="DarkGray",
    )
    bar_plot = sns.barplot(
        x="good",
        y="age",
        label="- hearth disease",
        data=df,
        order=age_cohort[::-1],
        color="Lavender",
    )
    bar_plot.set(
        xlabel="Quantity",
        ylabel="Age-Group",
        title="Target Class vs. Age Distribution of Dataset Sample",
    )
    plt.legend()
    filename = "bar2.png"
    fig_path = Path(f"{PLOTS_DIR}/{filename}").absolute()
    fig = bar_plot.get_figure()
    fig.savefig(fig_path)
    print(f"![heatmap]({fig_path})")

    print("# 5.Conclusion")
    print("Blah blah blah skewed data, needs preprocessing and so on.")


if __name__ == "__main__":
    main()
