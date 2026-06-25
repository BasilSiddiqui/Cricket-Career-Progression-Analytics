import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# ------------------------ STYLE SETTINGS ------------------------
sns.set_theme(style="whitegrid", palette="pastel")
plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13

# ------------------------ READ DATA ------------------------
df = pd.read_excel(
    r"C:\Users\basil\OneDrive\Desktop\Base\Other\Datasets\Cricket\Cricket stats.xlsx",
    sheet_name="Matches"
)

# Date handling & sorting
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)

# Match number (starting at 1)
df["Match_No"] = range(1, len(df) + 1)

# ------------------------ CUMULATIVE TOTALS ------------------------
df["Cum_Balls"] = df["Balls"].cumsum()
df["Cum_Runs"] = df["Runs"].cumsum()
df["Cum_Wickets"] = df["Wickets"].cumsum()
df["Cum_Maidens"] = df["Maidens"].cumsum()
df["Cum_Wins"] = (df["Result"] == "W").cumsum()
df["Cum_Losses"] = (df["Result"] == "L").cumsum()

# ------------------------ RUNNING METRICS ------------------------
df["Running_Overs"] = df["Cum_Balls"] / 6
df["Running_Economy"] = df["Cum_Runs"] / df["Running_Overs"]
df["Running_SR"] = np.where(
    df["Cum_Wickets"] > 0,
    df["Cum_Balls"] / df["Cum_Wickets"],
    np.nan
)
df["Running_Avg"] = np.where(
    df["Cum_Wickets"] > 0,
    df["Cum_Runs"] / df["Cum_Wickets"],
    np.nan
)
df["Running_WinPct"] = (df["Cum_Wins"] / df["Match_No"]) * 100

df = df[df['Date'].notna()].reset_index(drop=True)

# ===================== GRAPH 1: Running Overs =====================
plt.figure(figsize=(12, 6))
plt.plot(df["Match_No"], df["Running_Overs"],
         marker="o", linestyle="-", color="goldenrod",
         linewidth=2.5, markersize=7, label="Overs")
plt.xlim(0, df["Match_No"].max() * 1.05)
plt.ylim(0, df["Running_Overs"].max() * 1.05)
plt.xlabel("Matches")
plt.ylabel("Overs")
plt.title("Career Bowling Progression – Overs", fontweight="bold")
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
sns.despine()
plt.tight_layout()
plt.show()

# ===================== GRAPH 2: Running Maidens =====================
plt.figure(figsize=(12, 6))
plt.plot(df["Match_No"], df["Cum_Maidens"],
         marker="o", linestyle="-", color="slateblue",
         linewidth=2.5, markersize=7, label="Maidens")
plt.xlim(0, df["Match_No"].max() * 1.05)
plt.ylim(0, df["Cum_Maidens"].max() * 1.05)
plt.xlabel("Matches")
max_maidens = int(df["Cum_Maidens"].max())
plt.yticks(np.arange(0, max_maidens + 2, 1))  # +2 to include top
plt.ylabel("Maidens")
plt.title("Career Bowling Progression – Maidens", fontweight="bold")
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
sns.despine()
plt.tight_layout()
plt.show()

# ===================== GRAPH 3: Running Runs =====================
plt.figure(figsize=(12, 6))
plt.plot(df["Match_No"], df["Cum_Runs"],
         marker="o", linestyle="-", color="teal",
         linewidth=2.5, markersize=7, label="Runs")
plt.xlim(0, df["Match_No"].max() * 1.05)
plt.ylim(0, df["Cum_Runs"].max() * 1.05)
plt.xlabel("Matches")
plt.ylabel("Runs")
plt.title("Career Bowling Progression – Runs", fontweight="bold")
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
sns.despine()
plt.tight_layout()
plt.show()

# ===================== GRAPH 4: Running Wickets =====================
plt.figure(figsize=(12, 6))
plt.plot(df["Match_No"], df["Cum_Wickets"],
         marker="o", linestyle="-", color="crimson",
         linewidth=2.5, markersize=7, label="Wickets")
plt.xlim(0, df["Match_No"].max() * 1.05)
plt.ylim(0, df["Cum_Wickets"].max() * 1.05)
plt.xlabel("Matches")
plt.ylabel("Wickets")
plt.title("Career Bowling Progression – Wickets", fontweight="bold")
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
sns.despine()
plt.tight_layout()
plt.show()

# ===================== GRAPH 5: Running Economy =====================
plt.figure(figsize=(12, 6))
plt.plot(df["Match_No"], df["Running_Economy"],
         marker="o", linestyle="-", color="gold",
         linewidth=2.5, markersize=7, label="Economy")
plt.xlim(0, df["Match_No"].max() * 1.05)
plt.ylim(0, df["Running_Economy"].max() * 1.05)
plt.xlabel("Matches")
plt.ylabel("Economy (runs/over)")
plt.title("Career Bowling Progression – Economy", fontweight="bold")
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
sns.despine()
plt.tight_layout()
plt.show()

# ===================== GRAPH 6: Average + Strike Rate =====================
plt.figure(figsize=(12, 6))
plt.plot(df["Match_No"], df["Running_Avg"],
         marker="o", linestyle="-", color="green",
         linewidth=2.5, markersize=7, label="Average")
plt.plot(df["Match_No"], df["Running_SR"],
         marker="o", linestyle="-", color="crimson",
         linewidth=2.5, markersize=7, label="Strike Rate")
plt.xlim(0, df["Match_No"].max() * 1.05)
ymax = max(df["Running_Avg"].max(), df["Running_SR"].max())
plt.ylim(0, ymax * 1.05)
plt.xlabel("Matches")
plt.ylabel("Value")
plt.title("Career Bowling – Average & Strike Rate", fontweight="bold")
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
sns.despine()
plt.tight_layout()
plt.show()

# ===================== GRAPH 7: Matches & Wickets over Dates =====================
plt.figure(figsize=(12, 6))

plt.plot(df["Date"], df["Match_No"],
         marker="o", linestyle="-", color="navy",
         linewidth=2.5, markersize=3, label="Matches (cumulative)")
plt.plot(df["Date"], df["Cum_Wickets"],
         marker="o", linestyle="-", color="crimson",
         linewidth=2.5, markersize=3, label="Wickets (cumulative)")

plt.ylim(0, max(df["Match_No"].max(), df["Cum_Wickets"].max()) * 1.05)

ax = plt.gca()
ax.grid(False)

# ---- Major ticks: years ----
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.grid(axis='x', which='major', linestyle='-', alpha=0.3, color='gray', linewidth=1.5)

# ---- Minor ticks: quarters (from the quarter containing min date to the one containing max) ----
first_quarter = df["Date"].min().to_period('Q').start_time
last_quarter = df["Date"].max().to_period('Q').start_time
quarter_starts = pd.date_range(start=first_quarter, end=last_quarter, freq='QS')

ax.set_xticks(quarter_starts, minor=True)
ax.grid(axis='x', which='minor', linestyle='--', alpha=0.15, color='gray', linewidth=1)

# Rotate year labels
plt.xticks(rotation=45, ha='right')

plt.xlabel("Date")
plt.ylabel("Cumulative Count")
plt.title("Career Progression – Matches & Wickets over Time", fontweight="bold")
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
sns.despine()
plt.tight_layout()
plt.show()


# ===================== GRAPH 8: Running Win/Loss Ratio =====================
plt.figure(figsize=(12, 6))

# Drop NaN win percentages to avoid plotting issues
df_clean = df.dropna(subset=["Running_WinPct"])

# Define three groups
above_50 = df_clean[df_clean["Running_WinPct"] > 50]
equal_50 = df_clean[df_clean["Running_WinPct"] == 50]
below_50 = df_clean[df_clean["Running_WinPct"] < 50]

# Plot the trend line (gray, light)
plt.plot(df_clean["Match_No"], df_clean["Running_WinPct"],
         linestyle="-", color="gray", linewidth=1.5, alpha=0.6, label="Win % (trend)")

# Scatter: >50% green, =50% yellow, <50% red
plt.scatter(above_50["Match_No"], above_50["Running_WinPct"],
            color="green", s=80, label="> 50%", zorder=5)
plt.scatter(equal_50["Match_No"], equal_50["Running_WinPct"],
            color="gold", s=80, label="= 50%", zorder=5, edgecolor="black", linewidth=0.5)
plt.scatter(below_50["Match_No"], below_50["Running_WinPct"],
            color="crimson", s=80, label="< 50%", zorder=5)

# Horizontal reference line at 50%
plt.axhline(y=50, color="black", linestyle="--", linewidth=1.2, alpha=0.7, label="50% mark")

# Axis limits
plt.xlim(0, df_clean["Match_No"].max() * 1.05)
plt.ylim(0, 105)

# Labels and title
plt.xlabel("Matches")
plt.ylabel("Win Percentage")
plt.title("Running Win Percentage over Career", fontweight="bold")

# Legend
plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")

sns.despine()
plt.tight_layout()
plt.show()