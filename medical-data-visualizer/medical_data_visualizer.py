import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Load data
df = pd.read_csv("medical_examination.csv")

#Task 1: Overweight column

df["overweight"] = (
    df["weight"] / ((df["height"] / 100) ** 2) > 25
).astype(int)

#Task 2: Normalize cholesterol and gluc
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)

df["gluc"] = (df["gluc"] > 1).astype(int)

#start function draw_cat_plot
def draw_cat_plot():

    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight"
        ]
    )

    df_cat = (
        df_cat
        .groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    cat_plot = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    )

    fig = cat_plot.fig

    return fig

def draw_heat_map():

    # Clean the data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) &
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) &
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
    ]

    # Calculate correlation matrix
    corr = df_heat.corr()

    # Generate mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw heatmap
    sns.heatmap(
        corr,
        ax=ax,
        mask=mask,
        annot=True,
        fmt=".1f",
        square=True,
        center=0,
        vmax=0.32,
        cbar_kws={"shrink": 0.5}
    )

    return fig    