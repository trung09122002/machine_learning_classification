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

# lấy tọa độ tâm các cụm
centers = kmeans.cluster_centers_

# Tên các kim loại
metal_names = ['Gold', 'Silver', 'Bronze']

# Hiển thị kết quả phân cụm
print("Clustering results:")
for i, point in enumerate(point_names):
    print(f"Point {point} belongs to cluster {labels[i] + 1} ({metal_names[labels[i]]})")

print("\nCoordinates of cluster centers:")
for i, center in enumerate(centers):
    print(f"Cluster {i + 1} ({metal_names[i]}): {center}")

# Tính khoảng cách từ mỗi điểm đến tâm cụm của nó
distances = np.zeros(len(data))
for i in range(len(data)):
    cluster_center = centers[labels[i]]
    distances[i] = np.sqrt(np.sum((data[i] - cluster_center) ** 2))

print("\nDistance from each point to its cluster center:")
for i, point in enumerate(point_names):
    print(f"Point {point}: {distances[i]:.4f}")

# Vẽ biểu đồ 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Màu sắc cho các cụm
colors = ['gold', 'silver', 'chocolate']

# Vẽ các điểm dữ liệu
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], data[i, 2], c=colors[labels[i]], 
               s=100, label=f"Points {point_names[i]}")
    ax.text(data[i, 0], data[i, 1], data[i, 2], point_names[i], size=12)

# Vẽ tâm các cụm
for i, center in enumerate(centers):
    ax.scatter(center[0], center[1], center[2], c=colors[i], marker='*', 
               s=300, edgecolor='black', label=f'Center {metal_names[i]}')

# Thiết lập nhãn và tiêu đề
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('K-means Clustering of Metals')

# Loại bỏ các nhãn trùng lặp trong legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper left')

plt.tight_layout()
plt.savefig('phan_cum_khoang_san.png')  # Lưu hình
plt.show()

# tinh tong binh phuong khoang cach trong cum (inertia)
print(f"\nTotal sum of squared distances (inertia): {kmeans.inertia_:.4f}")

# tinh phuong sai giai thich (explained variance)
total_variance = np.var(data, axis=0).sum()
explained_variance = 1 - kmeans.inertia_ / (total_variance * len(data))
print(f"Explained variance: {explained_variance:.4f}")





