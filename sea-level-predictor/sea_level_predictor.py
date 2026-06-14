import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit: using all data
    result_all = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_all = pd.Series(range(df["Year"].min(), 2051))

    sea_levels_all = (
        result_all.slope * years_all + result_all.intercept
    )

    ax.plot(
        years_all,
        sea_levels_all
    )

    # Second line of best fit: using data from year 2000 onward
    df_2000 = df[df["Year"] >= 2000]

    result_2000 = linregress(
        df_2000["Year"],
        df_2000["CSIRO Adjusted Sea Level"]
    )

    years_2000 = pd.Series(range(2000, 2051))

    sea_levels_2000 = (
        result_2000.slope * years_2000 + result_2000.intercept
    )

    ax.plot(
        years_2000,
        sea_levels_2000
    )

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return figure
    fig.savefig("sea_level_plot.png")

    return fig