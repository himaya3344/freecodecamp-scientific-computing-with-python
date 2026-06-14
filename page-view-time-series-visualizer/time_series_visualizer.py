import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True
)

# Clean data: remove bottom 2.5% and top 2.5%
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Create a copy of the dataframe
    df_line = df.copy()

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(16, 6))

    # Draw line plot
    ax.plot(
        df_line.index,
        df_line["value"],
        color="red",
        linewidth=1
    )

    # Add title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image
    fig.savefig("line_plot.png")

    return fig

def draw_bar_plot():
    # Create a copy of the dataframe
    df_bar = df.copy()

    # Add year and month columns
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Correct month order
    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    df_bar["month"] = pd.Categorical(
        df_bar["month"],
        categories=month_order,
        ordered=True
    )

    # Group by year and month, then calculate average page views
    df_bar = df_bar.groupby(
        ["year", "month"],
        observed=False
    )["value"].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(
        kind="bar",
        figsize=(10, 8)
    ).figure

    # Set labels and legend
    ax = fig.axes[0]
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")

    # Save image
    fig.savefig("bar_plot.png")

    return fig

def draw_box_plot():
    # Create a copy of the dataframe
    df_box = df.copy()

    # Prepare data for box plots
    df_box.reset_index(inplace=True)

    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")

    # Correct month order
    month_order = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    df_box["month"] = pd.Categorical(
        df_box["month"],
        categories=month_order,
        ordered=True
    )

    # Create figure with two plots
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # Year-wise box plot
    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise box plot
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        ax=axes[1]
    )

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save image
    fig.savefig("box_plot.png")

    return fig