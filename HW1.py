# Quinn Aho - BE2100 Hw1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data
failure_data = np.array([
    1115, 865, 1015, 885, 1594, 1000, 1416, 1501, 1310, 2130, 845, 1223, 2023,
    1820, 1560, 1238, 1540, 1421, 1674, 375, 1315, 1940, 1055, 990, 1502, 1109,
    1016, 2265, 1269, 1120, 1764, 1468, 1258, 1481, 1102, 1910, 1260, 910, 1330,
    1512, 1315, 1567, 1605, 1018, 1888, 1730, 1608, 1750, 1085, 1883, 706, 1452,
    1782, 1102, 1535, 1642, 798, 1203, 2215, 1890, 1522, 1578, 1781, 1020, 1270,
    785, 2100, 1792, 758, 1750
], dtype=float)

s = pd.Series(failure_data)

# basic stats
n = s.size
x_min, x_max = s.min(), s.max()
mean, std = s.mean(), s.std(ddof=1)

print(f"Total: {n}  |  Range: {int(x_min)}–{int(x_max)} cycles")
print(f"Mean: {mean:.2f}  |  Std Dev: {std:.2f}")

# binning
k = int(1 + np.log2(n))
bins = np.linspace(x_min, x_max, k + 1)

# freq table
freq, edges = np.histogram(s, bins=bins)
cum = np.cumsum(freq)
rel = freq / n

table = pd.DataFrame({
    "Class Interval": [f"[{edges[i]:.0f}, {edges[i+1]:.0f})" for i in range(len(freq))],
    "Frequency": freq,
    "Relative Freq": rel.round(3),
    "Cumulative Freq": cum
})
print("\nFREQUENCY DISTRIBUTION")
print(table.to_string(index=False))
print(f"\nTotals -> Frequency: {freq.sum()} | Relative: {rel.sum():.3f} | Cumulative: {cum[-1]}")

# plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.hist(s, bins=bins, edgecolor='black')
plt.axvline(mean, linestyle='--', linewidth=2, label=f"Mean = {mean:.0f}")
plt.title('Histogram of Cycles to Failure')
plt.xlabel('Cycles to Failure')
plt.ylabel('Frequency')
plt.legend()
plt.grid(alpha=0.3)

plt.subplot(2, 1, 2)
plt.boxplot(s, vert=False, patch_artist=True)
plt.xlabel('Cycles to Failure')
plt.title('Box Plot of Cycles to Failure')
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# adiitional outliers
q1, q3 = s.quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = s[(s < lower) | (s > upper)].tolist()

print("\nADDITIONAL STATISTICS")
print(f"Median: {s.median():.2f}")
print(f"Q1: {q1:.2f} | Q3: {q3:.2f} | IQR: {iqr:.2f}")
print(f"Range: {x_max - x_min:.0f}")

# mode
top_counts = s.value_counts().head(3)
print("Most common values (top 3):")
for val, cnt in top_counts.items():
    print(f"  {int(val)} -> {cnt}x")
print(f"\nPotential outliers (IQR method): {outliers}")
print(f"Number of outliers: {len(outliers)}")