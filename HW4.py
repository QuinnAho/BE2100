# Fix the inverse normal (pphi) implementation with a clean Acklam algorithm.
import math

def pphi_clean(p):
    if p <= 0.0 or p >= 1.0:
        raise ValueError("p must be in (0,1)")
    a = [-3.969683028665376e+01,
          2.209460984245205e+02,
         -2.759285104469687e+02,
          1.383577518672690e+02,
         -3.066479806614716e+01,
          2.506628277459239e+00]
    b = [-5.447609879822406e+01,
          1.615858368580409e+02,
         -1.556989798598866e+02,
          6.680131188771972e+01,
         -1.328068155288572e+01]
    c = [-7.784894002430293e-03,
         -3.223964580411365e-01,
         -2.400758277161838e+00,
         -2.549732539343734e+00,
          4.374664141464968e+00,
          2.938163982698783e+00]
    d = [7.784695709041462e-03,
         3.224671290700398e-01,
         2.445134137142996e+00,
         3.754408661907416e+00]
    plow = 0.02425
    phigh = 1 - plow
    if p < plow:
        q = math.sqrt(-2*math.log(p))
        return (((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
               ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
    if p > phigh:
        q = math.sqrt(-2*math.log(1-p))
        return -(((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
                 ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
    q = p - 0.5
    r = q*q
    return (((((a[0]*r + a[1])*r + a[2])*r + a[3])*r + a[4])*r + a[5]) * q / \
           (((((b[0]*r + b[1])*r + b[2])*r + b[3])*r + b[4])*r + 1)

# Recompute with clean function
def norm_ppf_clean(p, mu=0.0, sigma=1.0):
    return mu + sigma * pphi_clean(p)

# Recompute critical z's
z_975 = norm_ppf_clean(0.975)  # ~1.95996
z_995 = norm_ppf_clean(0.995)  # ~2.57583
z_0841 = pphi_clean(0.841)

# 4.5.4 recompute
mu1, sd1 = 10.0, 2.0
x_a = mu1
x_b = norm_ppf_clean(0.05, mu1, sd1)
x_c = 10.0
x_d = sd1 * z_975
x_e = sd1 * z_995

# 4.5.8 recompute
mu2 = 159.2
sd2 = (200.0 - mu2) / z_0841
q1 = norm_ppf_clean(0.25, mu2, sd2)
q3 = norm_ppf_clean(0.75, mu2, sd2)
p90_val = norm_ppf_clean(0.90, mu2, sd2)

# 4.5.9 recompute with clean CDF using erf (unchanged) 
def phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2)))

def norm_cdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu)/sigma)

mu3, sd3 = 1.41, 0.01
p_a = 1.0 - norm_cdf(1.42, mu3, sd3)
thresh_b = norm_ppf_clean(0.05, mu3, sd3)
prop_c = norm_cdf(1.43, mu3, sd3) - norm_cdf(1.39, mu3, sd3)

answers_fixed = {
    "4.5.4": {
        "a_x": x_a,
        "b_x": x_b,
        "c_x": x_c,
        "d_x": x_d,
        "e_x": x_e,
    },
    "4.5.8": {
        "sigma": sd2,
        "quartiles": {"Q1": q1, "Q3": q3},
        "p90_value": p90_val,
    },
    "4.5.9": {
        "a_prob_gt_1.42": p_a,
        "b_5th_percentile": thresh_b,
        "c_within_spec_pct": prop_c*100,
    },
    "z_values": {
        "z_975": z_975,
        "z_995": z_995,
        "z_for_0.841": z_0841
    }
}