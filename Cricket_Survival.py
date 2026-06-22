import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean, modern style
sns.set_theme(style="whitegrid", palette="pastel")
plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13

# Read data
df = pd.read_excel(
    r"C:\Users\basil\OneDrive\Desktop\Base\Other\Datasets\Cricket\Cricket stats.xlsx",
    sheet_name="Matches"
)

# Date handling & sorting
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)

# Match number (starting at 1)
df["Match_No"] = range(1, len(df) + 1)

# Cumulative totals
df["Cum_Balls"] = df["Balls"].cumsum()
df["Cum_Runs"] = df["Runs"].cumsum()
df["Cum_Wickets"] = df["Wickets"].cumsum()
df["Cum_Maidens"] = df["Maidens"].cumsum()   # Make sure your Excel has a 'Maidens' column

# Running metrics
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

# Define metrics: (column, color, label)
metrics = [
    ("Running_Overs", "darkorange", "Overs"),
    ("Cum_Maidens", "purple", "Maidens"),
    ("Cum_Runs", "cyan", "Runs"),
    ("Cum_Wickets", "blue", "Wickets"),
    ("Running_Economy", "gold", "Economy"),
    ("Running_SR", "red", "Strike Rate"),
    ("Running_Avg", "green", "Average"),
]

# Create a separate figure for each metric
for col, color, label in metrics:
    plt.figure(figsize=(12, 6))
    
    # Plot the data
    plt.plot(df["Match_No"], df[col],
             marker="o", linestyle="-", color=color,
             linewidth=2.5, markersize=7, label=label)
    
    # Force axes to start at 0
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    
    # Optionally add a small margin on the right/top so points aren't cut off
    xmax = df["Match_No"].max()
    ymax = df[col].max()
    plt.xlim(0, xmax * 1.05)          # 5% extra space on the right
    if not np.isnan(ymax):
        plt.ylim(0, ymax * 1.05)      # 5% extra space on top
    
    # Labels and title
    plt.xlabel("Matches")
    plt.ylabel(label)
    plt.title(f"Career Bowling Progression – {label}", fontweight="bold")
    
    # Legend with a clean frame
    plt.legend(frameon=True, loc="best", framealpha=0.9, edgecolor="gray")
    
    # Grid already provided by seaborn; we keep it
    # Remove top/right spines for a cleaner look (optional)
    sns.despine()
    
    plt.tight_layout()
    plt.show()