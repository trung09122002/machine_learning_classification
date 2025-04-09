import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Dữ liệu từ bảng
# Các điểm A, B, C, D, E, F với thuộc tính X, Y, Z
data = np.array([
    [1, 2, 4],  # A
    [3, 1, 2],  # B
    [4, 2, 1],  # C
    [3, 3, 5],  # D
    [2, 1, 4],  # E
    [5, 3, 2]   # F
])

# Tên các điểm
point_names = ['A', 'B', 'C', 'D', 'E', 'F']

# Áp dụng thuật toán K-means với k=3 (vàng, bạc, đồng)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(data)

# Lấy nhãn cụm cho mỗi điểm
labels = kmeans.labels_

# Lấy tọa độ tâm các cụm
centers = kmeans.cluster_centers_

# Tên các kim loại
metal_names = ['Vàng', 'Bạc', 'Đồng']

# Hiển thị kết quả phân cụm
print("Kết quả phân cụm:")
for i, point in enumerate(point_names):
    print(f"Điểm {point} thuộc cụm {labels[i] + 1} ({metal_names[labels[i]]})")

print("\nTọa độ tâm các cụm:")
for i, center in enumerate(centers):
    print(f"Cụm {i + 1} ({metal_names[i]}): {center}")

# Tính khoảng cách từ mỗi điểm đến tâm cụm của nó
distances = np.zeros(len(data))
for i in range(len(data)):
    cluster_center = centers[labels[i]]
    distances[i] = np.sqrt(np.sum((data[i] - cluster_center) ** 2))

print("\nKhoảng cách từ mỗi điểm đến tâm cụm của nó:")
for i, point in enumerate(point_names):
    print(f"Điểm {point}: {distances[i]:.4f}")

# Vẽ biểu đồ 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Màu sắc cho các cụm
colors = ['gold', 'silver', 'chocolate']

# Vẽ các điểm dữ liệu
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], data[i, 2], c=colors[labels[i]], 
               s=100, label=f"Điểm {point_names[i]}")
    ax.text(data[i, 0], data[i, 1], data[i, 2], point_names[i], size=12)

# Vẽ tâm các cụm
for i, center in enumerate(centers):
    ax.scatter(center[0], center[1], center[2], c=colors[i], marker='*', 
               s=300, edgecolor='black', label=f'Tâm cụm {metal_names[i]}')

# Đặt nhãn trục
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Phân cụm mẫu khoáng sản bằng K-means')

# Loại bỏ các nhãn trùng lặp trong legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper left')

plt.tight_layout()
plt.savefig('phan_cum_khoang_san.png')  # Lưu hình
plt.show()

# Tính tổng bình phương khoảng cách trong cụm (inertia)
print(f"\nTổng bình phương khoảng cách trong cụm: {kmeans.inertia_:.4f}")

# Tính phương sai giải thích (explained variance)
total_variance = np.var(data, axis=0).sum()
explained_variance = 1 - kmeans.inertia_ / (total_variance * len(data))
print(f"Phương sai giải thích: {explained_variance:.4f}")

# Thử nghiệm các giá trị K khác nhau để tìm K tối ưu
inertias = []
k_values = range(1, min(6, len(data)))

for k in k_values:
    kmeans_test = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans_test.fit(data)
    inertias.append(kmeans_test.inertia_)

# Vẽ biểu đồ Elbow
plt.figure(figsize=(10, 6))
plt.plot(k_values, inertias, 'o-', color='blue')
plt.xlabel('Số cụm (K)')
plt.ylabel('Tổng bình phương khoảng cách trong cụm')
plt.title('Phương pháp Elbow cho việc xác định số cụm tối ưu')
plt.grid(True)
plt.savefig('elbow_method.png')  # Lưu hình
plt.show()