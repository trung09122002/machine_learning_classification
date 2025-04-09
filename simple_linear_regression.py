import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
x = np.array([41, 54, 63, 54, 48, 46, 62, 61, 64, 71])


y = np.array([1250, 1380, 1425, 1425, 1450, 1300, 1400, 1510, 1575, 1650])

# Số lượng điểm dữ liệu
n = len(x)

# Tính các giá trị trung bình
x_mean = np.mean(x)
y_mean = np.mean(y)
print(x_mean, y_mean)

# Tính các hệ số
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean)**2)

# Hệ số góc (beta_1)
beta_1 = numerator / denominator

# Hệ số chặn (beta_0)
beta_0 = y_mean - beta_1 * x_mean

# In phương trình hồi quy
print(f"Phương trình hồi quy: y = {beta_0:.2f} + {beta_1:.2f}x")

# tinh MSE
y_pred = beta_0 + beta_1 * x
mse = np.mean((y - y_pred)**2)
print(f"MSE: {mse:.2f}")

# Vẽ đồ thị
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Dữ liệu thực')

# Đường hồi quy
x_line = np.linspace(min(x), max(x), 100)
y_line = beta_0 + beta_1 * x_line
plt.plot(x_line, y_line, color='red', label='Đường hồi quy')

plt.title('Hoi quy tuyen tinh: Doanh thu vs Chi tiêu Quang cao')
plt.xlabel('Chi tieu Quang cao')
plt.ylabel('Doanh Thu')
plt.legend()
plt.grid(True)
plt.show()
