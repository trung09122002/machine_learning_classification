import csv
import os

def create_decision_tree_csv(save_path=None):
    """
    Tạo file CSV từ dữ liệu cây quyết định
    
    :param save_path: Đường dẫn lưu file (tùy chọn)
    """
    # Dữ liệu từ bảng
    data = [
        ['Ngay', 'Tiet troi', 'Nhiet do', 'Do am', 'Gio', 'Choi cau long'],
        [1, 'Nang', 'Nong', 'Cao', 'Yeu', 'Khong'],
        [2, 'Nang', 'Nong', 'Cao', 'Manh', 'Khong'],
        [3, 'Nhieu may', 'Nong', 'Cao', 'Yeu', 'Co'],
        [4, 'Mua', 'Mat', 'Cao', 'Yeu', 'Co'],
        [5, 'Mua', 'Lanh', 'Thuong', 'Yeu', 'Co'],
        [6, 'Mua', 'Lanh', 'Thuong', 'Manh', 'Khong'],
        [7, 'Nhieu may', 'Lanh', 'Thuong', 'Manh', 'Co'],
        [8, 'Nang', 'Mat', 'Cao', 'Yeu', 'Khong'],
        [9, 'Nang', 'Lanh', 'Thuong', 'Yeu', 'Co'],
        [10, 'Mua', 'Mat', 'Thuong', 'Yeu', 'Co'],
        [11, 'Nang', 'Mat', 'Thuong', 'Manh', 'Co'],
        [12, 'Nhieu may', 'Mat', 'Cao', 'Manh', 'Co'],
        [13, 'Nhieu may', 'Nong', 'Thuong', 'Yeu', 'Co'],
        [14, 'Mua', 'Mat', 'Cao', 'Manh', 'Khong']
    ]
    
    # Xác định đường dẫn lưu file
    if save_path is None:
        # Nếu không có đường dẫn, sử dụng thư mục làm việc hiện tại
        save_path = os.path.join(os.getcwd(), 'decision_tree_data.csv')
    
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    try:
        # Mở file để ghi
        with open(save_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Tạo writer
            csv_writer = csv.writer(csvfile)
            
            # Ghi dữ liệu
            csv_writer.writerows(data)
        
        print(f"Đã tạo file CSV tại: {save_path}")
        return save_path
    
    except Exception as e:
        print(f"Lỗi khi tạo file CSV: {e}")
        return None

def main():
    # Các cách tạo file CSV
    
    # Cách 1: Sử dụng thư mục làm việc hiện tại
    create_decision_tree_csv()
    
    # Cách 2: Chỉ định đường dẫn đầy đủ
    # create_decision_tree_csv(r'D:/machine_learning/decision_tree_data.csv')

if __name__ == '__main__':
    main()

# Chức năng:
# 1. Tạo file CSV từ dữ liệu cây quyết định
# 2. Tự động tạo thư mục nếu chưa tồn tại
# 3. Linh hoạt với đường dẫn lưu file
# 4. Hỗ trợ Unicode