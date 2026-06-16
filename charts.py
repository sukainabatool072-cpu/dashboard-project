import matplotlib.pyplot as plt
import seaborn as sns

PALETTE = "Set2"

# 1. PIE CHART — Match distribution by surface
def plot_pie_surface(df):
    fig, ax = plt.subplots(figsize=(5, 4))
    counts = df["surface"].value_counts()
    ax.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        pctdistance=1.2,
        colors=sns.color_palette(PALETTE, len(counts)),
        startangle=90,
        wedgeprops=dict(edgecolor="white", linewidth=1.5)
    )
    ax.set_title("Match Distribution by Surface")
    plt.tight_layout()
    return fig


# 2. HISTOGRAM — Winner age distribution
def plot_histogram_age(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df["winner_age"].dropna(), bins=25,
            color=sns.color_palette(PALETTE)[1], edgecolor="white")
    ax.set_title("Winner Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    return fig


# 3. LINE CHART — Matches per month over the season
def plot_line_matches_over_time(df):
    monthly = df.groupby(df["tourney_date"].dt.to_period("M")).size().reset_index()
    monthly.columns = ["Month", "Matches"]
    monthly["Month"] = monthly["Month"].dt.to_timestamp()

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(monthly["Month"], monthly["Matches"],
            marker="o", color=sns.color_palette(PALETTE)[2], linewidth=2)
    ax.set_title("Matches per Month (2016 Season)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Matches")
    plt.xticks(rotation=30)
    plt.tight_layout()
    return fig


# 4. BAR CHART — Top 10 players by wins
def plot_bar_top_winners(df):
    top = df["winner_name"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(x=top.values, y=top.index, palette=PALETTE, ax=ax)
    ax.set_title("Top 10 Players by Wins")
    ax.set_xlabel("Wins")
    ax.set_ylabel("Player")
    plt.tight_layout()
    return fig


# 5. SCATTER PLOT — Winner rank vs loser rank
def plot_scatter_ranks(df):
    sample = df.dropna(subset=["winner_rank", "loser_rank"]).sample(
        min(500, len(df)), random_state=42)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(sample["winner_rank"], sample["loser_rank"],
               alpha=0.5, color=sns.color_palette(PALETTE)[3], s=20)
    ax.set_title("Winner Rank vs Loser Rank")
    ax.set_xlabel("Winner Rank")
    ax.set_ylabel("Loser Rank")
    plt.tight_layout()
    return fig


# 6. BOX PLOT — Winner vs loser age spread
def plot_box_ages(df):
    data = [
        df["winner_age"].dropna().values,
        df["loser_age"].dropna().values
    ]
    fig, ax = plt.subplots(figsize=(5, 4))
    bp = ax.boxplot(data, tick_labels=["Winner Age", "Loser Age"], patch_artist=True,
                    medianprops=dict(color="black", linewidth=2))
    colors = sns.color_palette(PALETTE, 2)
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
    ax.set_title("Age Spread: Winners vs Losers")
    ax.set_ylabel("Age")
    plt.tight_layout()
    return fig


# 7. HEATMAP — Correlation between rank and age columns
def plot_heatmap_correlation(df):
    cols = ["winner_age", "loser_age", "winner_rank", "loser_rank"]
    corr = df[cols].corr()

    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
                linewidths=0.5, ax=ax)
    ax.set_title("Correlation Heatmap")
    plt.tight_layout()
    return fig


# 8. AREA CHART — Cumulative matches over the season
def plot_area_cumulative(df):
    daily = df.groupby("tourney_date").size().cumsum().reset_index()
    daily.columns = ["Date", "Cumulative Matches"]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.fill_between(daily["Date"], daily["Cumulative Matches"],
                    color=sns.color_palette(PALETTE)[4], alpha=0.6)
    ax.plot(daily["Date"], daily["Cumulative Matches"],
            color=sns.color_palette(PALETTE)[4], linewidth=1.5)
    ax.set_title("Cumulative Matches Over 2016 Season")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Matches")
    plt.xticks(rotation=30)
    plt.tight_layout()
    return fig


# 9. COUNT PLOT — Matches per tournament (top 10)
def plot_count_tournaments(df):
    top_tourneys = df["tourney_name"].value_counts().head(10).index
    filtered = df[df["tourney_name"].isin(top_tourneys)]

    fig, ax = plt.subplots(figsize=(7, 4))
    sns.countplot(data=filtered, y="tourney_name",
                  order=top_tourneys, palette=PALETTE,
                  hue="tourney_name", legend=False, ax=ax)
    ax.set_title("Top 10 Tournaments by Match Count")
    ax.set_xlabel("Match Count")
    ax.set_ylabel("Tournament")
    plt.tight_layout()
    return fig


# 10. VIOLIN PLOT — Winner age distribution by surface
def plot_violin_age_surface(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.violinplot(data=df, x="surface", y="winner_age",
                   hue="surface", palette=PALETTE,
                   inner="box", legend=False, ax=ax)
    ax.set_title("Winner Age Distribution by Surface")
    ax.set_xlabel("Surface")
    ax.set_ylabel("Age")
    plt.tight_layout()
    return fig 
