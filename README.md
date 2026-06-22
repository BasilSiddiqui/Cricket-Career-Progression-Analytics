# Cricket Career Progression Analytics

## Overview

Most cricket analytics focus on isolated performances — a single match, a tournament, or a season.

This project takes a different approach.

Using cumulative performance metrics and concepts inspired by survival analysis, it tracks how a bowler's career evolves over time, showing not just where they are today, but how they got there.

Rather than treating every match independently, the analysis continuously updates career statistics after each game, creating a living record of improvement, consistency, and long-term development.

The result is a visual story of progression.

---

## Why This Project?

Averages, strike rates, and economy rates are often viewed as static numbers.

However, these metrics are the product of hundreds of overs, thousands of deliveries, and years of experience.

This project answers questions such as:

* How quickly did performance improve?
* When did major breakthroughs occur?
* How much impact did early performances have on career statistics?
* How long did it take for career figures to stabilize?
* What does long-term growth look like when viewed match by match?

By treating a cricket career as a time series rather than a collection of isolated matches, we gain a much deeper understanding of player development.

---

## Methodology

The analysis calculates cumulative career statistics after every match:

### Career Economy Rate

Measures how many runs are conceded per over throughout the player's career.

### Career Strike Rate

Tracks the average number of balls required to take a wicket across the entire career.

### Career Bowling Average

Measures the number of runs conceded per wicket over time.

### Career Wickets

Tracks cumulative wickets and highlights periods of rapid growth.

### Career Overs Bowled

Measures accumulated workload and experience.

### Career Runs Conceded

Provides context for the evolution of bowling metrics.

---

## Survival Analysis Inspiration

Traditional cricket statistics provide snapshots.

This project borrows ideas from survival analysis by focusing on progression over exposure and time.

Instead of analysing a single performance, the analysis follows the evolution of career metrics as additional overs are bowled and more wickets are taken.

This perspective helps reveal:

* Learning curves
* Performance stabilization
* Long-term consistency
* Career milestones
* The impact of experience on results

---

## Key Insight

One of the most fascinating observations is how volatile career statistics are in the early stages.

A single wicket or expensive spell can dramatically alter averages and strike rates.

As more matches are played, the metrics gradually stabilize and begin to reflect true performance levels.

The charts tell a story that raw statistics alone cannot:

A journey from uncertainty and small sample sizes to consistency, experience, and sustained performance.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* OpenPyXL

---

## What Makes This Different?

Many sports analytics projects focus on predicting future performance or comparing players.

This project focuses on something more personal:

**Visualizing growth.**

Every point on the graph represents another match played, another lesson learned, and another step forward.

The final statistics are important, but the path taken to reach them is where the real story lives.

These visualizations demonstrate how performance evolves through persistence, experience, and time — turning a collection of scorecards into a narrative of continuous improvement.
