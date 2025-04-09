import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Đọc dữ liệu từ file Excel
file_path = "fruit_data.xlsx"  # Đảm bảo đường dẫn đúng
df = pd.read_excel(file_path)

# Xóa cột không cần thiết
df = df.drop(columns=["Unnamed: 0", "fruit_type"])

# Mã hóa nhãn (Tốt -> 1, Hư hỏng -> 0)
label_encoder = LabelEncoder()
df["damaged (label)"] = label_encoder.fit_transform(df["damaged (label)"])

# Tách dữ liệu thành đặc trưng (X) và nhãn (y)
X = df.drop(columns=["damaged (label)"])
y = df["damaged (label)"]

# Chia dữ liệu thành tập huấn luyện (80%) và tập kiểm tra (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Khởi tạo và huấn luyện mô hình Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá độ chính xác
accuracy = accuracy_score(y_test, y_pred)
print(f"Độ chính xác của mô hình: {accuracy:.2f}")
