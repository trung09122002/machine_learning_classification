import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu từ bảng
data = {
    "y": [1250, 1380, 1425, 1425, 1450, 1300, 1400, 1510, 1575, 1650],
    "quang_cao": [41, 54, 63, 54, 48, 46, 62, 61, 64, 71],
    "vi_tri": [21, 30, 63, 54, 25, 46, 26, 61, 45, 17],
    "mat_hang": [4, 9, 36, 5, 6, 23, 62, 16, 43, 12]
}

# Chuyển đổi dữ liệu sang numpy array
y = np.array(data["y"])
X = np.column_stack([
    np.array(data["quang_cao"]),
    np.array(data["vi_tri"]),
    np.array(data["mat_hang"])
])

# Thêm cột 1 để tính intercept
X_with_intercept = np.column_stack([np.ones(X.shape[0]), X])

# Hàm tính toán hệ số hồi quy bằng phương pháp bình phương tối thiểu
def linear_regression(X, y):
    # Công thức: beta = (X^T * X)^-1 * X^T * y
    beta = np.linalg.inv(X.T @ X) @ X.T @ y
    return beta

# Tính toán hệ số
beta = linear_regression(X_with_intercept, y)

# In phương trình hồi quy
print("Phương trình hồi quy:")
print(f"y = {beta[0]:.2f} + {beta[1]:.2f}*quang_cao + {beta[2]:.2f}*vi_tri + {beta[3]:.2f}*mat_hang")

# Dự đoán
y_pred = X_with_intercept @ beta

# Tính SSE (Sum of Squared Errors)
sse = np.sum((y - y_pred) ** 2)
print(f"SSE = {sse:.2f}")

# Hàm vẽ biểu đồ
def plot_variable_vs_sales(var_name, var_data, y, y_pred):
    plt.figure(figsize=(8, 6))
    plt.scatter(var_data, y, color='blue', label='Thực tế')
    plt.scatter(var_data, y_pred, color='red', label='Dự đoán', marker='x')
    plt.xlabel(var_name)
    plt.ylabel('Doanh số (y)')
    plt.title(f'{var_name} vs Doanh số')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Vẽ biểu đồ từng biến
variable_names = ["quang_cao", "vi_tri", "mat_hang"]
for name, var_data in zip(variable_names, X.T):
    plot_variable_vs_sales(name, var_data, y, y_pred)