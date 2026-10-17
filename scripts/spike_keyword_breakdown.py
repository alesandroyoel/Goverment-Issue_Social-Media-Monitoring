"""Keyword breakdown of one day's engagement.

Reproduces the 29 April 2026 figures cited in the report (prabowo 21%, guru 15%,
impeachment 14%, no king 12%, politik 11%). This check is not part of the notebook.

Usage:
    python scripts/spike_keyword_breakdown.py "<path to data xlsx>" [YYYY-MM-DD]
"""
import sys
import pandas as pd

path = sys.argv[1] if len(sys.argv) > 1 else "data/Data Test_Assigment Tahap 1.xlsx"
date = sys.argv[2] if len(sys.argv) > 2 else "2026-04-29"

df = pd.read_excel(path, sheet_name="Posts")
df["keyword_clean"] = df["keyword"].str.lower().str.replace("#", "", regex=False).str.strip()
df["jumlah_like"] = df["jumlah_like"].fillna(0)
df["total_engagement"] = df["jumlah_like"] + df["jumlah_komentar"] + df["jumlah_share"]

day = df[df["tanggal_post"].dt.date.astype(str) == date]
share = (day.groupby("keyword_clean")["total_engagement"].sum()
         / day["total_engagement"].sum() * 100).sort_values(ascending=False)

print(f"{date}: total engagement = {int(day['total_engagement'].sum()):,}")
print("Top 5 keywords by share of the day's engagement (%):")
print(share.head(5).round(1).to_string())
