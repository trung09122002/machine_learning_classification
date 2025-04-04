import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
x1 = np.array([41, 54, 63, 54, 48, 46, 62, 61, 64, 71])
x2 = np.array([21, 30, 63, 54, 25, 46, 26, 61, 45, 17])
x3 = np.array([4, 9, 36, 5, 6, 23, 62, 16, 43, 12])

y = np.array([1250, 1380, 1425, 1425, 1450, 1300, 1400, 1510, 1575, 1650])

# Số lượng điểm dữ liệu
n = len(x1)

# Tính các giá trị trung bình
x1_mean = np.mean(x1)
x2_mean = np.mean(x2)
x3_mean = np.mean(x3)

y_mean = np.mean(y)

# Tính các hệ số
numerator1 = np.sum((x1 - x1_mean) * (y - y_mean))
numerator2 = np.sum((x2 - x2_mean) * (y - y_mean))
numerator3 = np.sum((x3 - x3_mean) * (y - y_mean))


denominator1 = np.sum((x1 - x1_mean)**2)
denominator2 = np.sum((x2 - x2_mean)**2)
denominator3 = np.sum((x3 - x3_mean)**2)

# Hệ số góc (beta_1)
beta1_1 = numerator1 / denominator1
beta2_1 = numerator2 / denominator2
beta3_1 = numerator3 / denominator3

# Hệ số chặn (beta_0)
beta1_0 = y_mean - beta1_1 * x1_mean
beta2_0 = y_mean - beta2_1 * x2_mean
beta3_0 = y_mean - beta3_1 * x3_mean

# In phương trình hồi quy
print(f"phuong trinh hoi quy 1: y = {beta1_0:.2f} + {beta1_1:.2f}x1")
print(f"phuong trinh hoi quy 2: y = {beta2_0:.2f} + {beta2_1:.2f}x2")
print(f"phuong trinh hoi quy 3: y = {beta3_0:.2f} + {beta3_1:.2f}x3")
beta_0 = beta1_0 + beta2_0 + beta3_0
print(f"phuong trinh hoi quy: y = {beta_0:.2f} + {beta1_1:.2f}x1 + {beta2_1:.2f}x2 + {beta3_1:.2f}x3")

# tinh MSE
y1_pred = beta1_0 + beta1_1 * x1
y2_pred = beta2_0 + beta2_1 * x2
y3_pred = beta3_0 + beta3_1 * x3
mse1 = np.mean((y - y1_pred)**2)
mse2 = np.mean((y - y2_pred)**2)
mse3 = np.mean((y - y3_pred)**2)

print(f"MSE1: {mse1:.2f}")
print(f"MSE2: {mse2:.2f}")
print(f"MSE3: {mse3:.2f}")
print(f"MSE: {(mse1 + mse2 + mse3):.2f}")


# Ve do thi 1
plt.figure(figsize=(10, 6))
plt.scatter(x1, y, color='blue', label='Du lieu thuc ve Doanh thu vs Chi tieu Quang cao')
x1_line = np.linspace(min(x1), max(x1), 100)
y1_line = beta1_0 + beta1_1 * x1_line
plt.plot(x1_line, y1_line, color='red', label='Duong hoi quy')
plt.title('Hoi quy tuyen tinh: Doanh thu vs Chi tiêu Quang cao')
plt.xlabel('Chi tieu Quang cao')
plt.ylabel('Doanh Thu')
plt.legend()
plt.grid(True)
plt.show()

# Vẽ do thi 2
plt.figure(figsize=(10, 6))
plt.scatter(x2, y, color='green', label='Du lieu thuc ve Doanh thu vs Chi tieu Vi Tri')
x2_line = np.linspace(min(x2), max(x2), 100)
y2_line = beta2_0 + beta2_1 * x2_line
plt.plot(x2_line, y2_line, color='blue', label='Duong hoi quy 2')
plt.title('Hoi quy tuyen tinh: Doanh thu vs Chi tieu Vi Tri')
plt.xlabel('Chi tieu Quang cao')
plt.ylabel('Doanh Thu')
plt.legend()
plt.grid(True)
plt.show()

# Ve do thi 3
plt.figure(figsize=(10, 6))
plt.scatter(x3, y, color='yellow', label='Du lieu thuc ve Doanh thu vs Chi tieu Mat Hang')
x3_line = np.linspace(min(x3), max(x3), 100)
y3_line = beta3_0 + beta3_1 * x3_line
plt.plot(x3_line, y3_line, color='orange', label='Duong hoi quy 3')
plt.title('Hoi quy tuyen tinh: Doanh thu vs Chi tieu Mat Hang')
plt.xlabel('Chi tieu Quang cao')
plt.ylabel('Doanh Thu')
plt.legend()
plt.grid(True)
plt.show()

# # ve do thi
# plt.figure(figsize=(10, 6))
# plt.scatter(x1, y, color='blue', label='Du lieu thuc ve Doanh thu vs Chi tieu Quang cao')
# plt.scatter(x2, y, color='green', label='Du lieu thuc ve Doanh thu vs Chi tieu Vi Tri')
# plt.scatter(x3, y, color='yellow', label='Du lieu thuc ve Doanh thu vs Chi tieu Mat Hang')

# x1_line = np.linspace(min(x1), max(x1), 100)
# x2_line = np.linspace(min(x2), max(x2), 100)
# x3_line = np.linspace(min(x3), max(x3), 100)

# y1_line = beta1_0 + beta1_1 * x1_line
# y2_line = beta2_0 + beta2_1 * x2_line
# y3_line = beta3_0 + beta3_1 * x3_line

# plt.plot(x1_line, y1_line, color='red', label='Duong hoi quy')

# plt.plot(x2_line, y2_line, color='blue', label='Duong hoi quy 2')

# plt.plot(x3_line, y3_line, color='orange', label='Duong hoi quy 3')

# plt.title('Hoi quy tuyen tinh: Doanh thu voi Chi tieu Quang cao, Vi Tri, Mat Hang')
# plt.xlabel('Chi tieu')
# plt.ylabel('Doanh Thu')
# plt.legend()
# plt.grid(True)
# plt.show()