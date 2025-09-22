# HW 3 - BE 2100, Quinn Aho

from math import comb, exp

# Binomial PMF
def binom_pmf(k, n, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# 3.5.8
n, p = 25, 0.25
prob_more_than_20 = sum(binom_pmf(k, n, p) for k in range(21, n + 1))
prob_less_than_5 = sum(binom_pmf(k, n, p) for k in range(0, 5))
print("3.5.8:")
print(f"a) P(X>20) = {prob_more_than_20:.6f}")
print(f"b) P(X<5)  = {prob_less_than_5:.6f}\n")

# Poisson PMF
def pois_pmf(k, lam):
    fact = 1
    for i in range(2, k + 1):
        fact *= i
    return exp(-lam) * (lam ** k) / fact

# 3.8.6
lam_5 = 2 * 5
lam_half = 2 * 0.5
p_no_cracks = pois_pmf(0, lam_5)
p_at_least_one = 1 - pois_pmf(0, lam_half)
print("3.8.6:")
print(f"a) P(0 in 5 miles) = {p_no_cracks:.6f}")
print(f"b) P(≥1 in 0.5 mi) = {p_at_least_one:.6f}")
print("c) Poisson assumes constant rate λ. If load varies, variance > mean -> Poisson may not fit.")
