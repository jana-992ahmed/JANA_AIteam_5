import numpy as np

X = np.array([50, 60, 80, 100, 120])
y = np.array([150, 180, 240, 300, 330])

# Reshape X into a column vector
X = X.reshape(-1 ,1)
print("X shape:", X.shape)  # (5, 1)

# Add bias column of ones
X_b = np.hstack([np.ones((X.shape[0], 1)), X])
print("X with bias:\n", X_b)

#Normal Equation -> θ = (XᵀX)⁻¹ Xᵀy
theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
print("\nθ (parameters):", theta)

# Predict price
X_pred = np.array([1, 90])  # 1 for bias
price = X_pred @ theta
print(f"\nPredicted price for 90 m: {price:.2f} thousand")

