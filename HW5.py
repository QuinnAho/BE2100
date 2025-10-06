# Quinn Aho HW5

import numpy as np
import pandas as pd

# joint PMF table
# rows = X = 0,1,2,3,4
# columns = Y = 1,2,3,4
pmf = np.array([
    [0.05, 0.05, 0.06, 0.05],
    [0.04, 0.01, 0.09, 0.09],
    [0.09, 0.06, 0.07, 0.01],
    [0.02, 0.03, 0.07, 0.04],
    [0.02, 0.09, 0.01, 0.05]
])

x_vals = np.array([0, 1, 2, 3, 4])
y_vals = np.array([1, 2, 3, 4])

# check PMF properties
total_prob = pmf.sum()
print(f"Total Probability = {total_prob:.2f} (should equal 1)")

# marginal probabilities
p_x = pmf.sum(axis=1)
p_y = pmf.sum(axis=0)
print("\nP(X):", p_x)
print("P(Y):", p_y)

# means (expected)
E_X = np.sum(x_vals * p_x)
E_Y = np.sum(y_vals * p_y)
print(f"\nE[X] = {E_X:.4f}")
print(f"E[Y] = {E_Y:.4f}")

# variances
Var_X = np.sum(((x_vals - E_X) ** 2) * p_x)
Var_Y = np.sum(((y_vals - E_Y) ** 2) * p_y)
print(f"Var(X) = {Var_X:.4f}")
print(f"Var(Y) = {Var_Y:.4f}")

# covariance
E_XY = np.sum(x_vals[:, None] * y_vals[None, :] * pmf)
Cov_XY = E_XY - E_X * E_Y
print(f"Cov(X,Y) = {Cov_XY:.4f}")

# correlation
Corr_XY = Cov_XY / np.sqrt(Var_X * Var_Y)
print(f"Corr(X,Y) = {Corr_XY:.4f}")

# independence check
# X and Y are independent if P(X,Y) = P(X)*P(Y) for all x,y
independent = np.allclose(pmf, np.outer(p_x, p_y), atol=1e-4)
print(f"Are X and Y independent? {'Yes' if independent else 'No'}")

# pretty print summary
summary = pd.DataFrame(pmf, index=[f"X={x}" for x in x_vals],
                       columns=[f"Y={y}" for y in y_vals])
print("\nJoint PMF Table:\n", summary)
