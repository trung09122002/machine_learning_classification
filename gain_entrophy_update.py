import math
import pandas as pd

def calculate_entropy(total_count, positive_count):
    """
    Tính entropy của tập dữ liệu
    
    :param total_count: Tổng số mẫu
    :param positive_count: Số mẫu thuộc lớp dương
    :return: Giá trị entropy
    """
    # Xác suất của các lớp
    p1 = positive_count / total_count
    p2 = 1 - p1
    
    # Hàm logarit an toàn
    def safe_log2(x):
        return math.log2(x) if x > 0 else 0
    
    # Tính entropy
    return -(p1 * safe_log2(p1) + p2 * safe_log2(p2))

def calculate_feature_gain(df, feature_column, target_column='Choi cau long', positive_value='Co'):
    """
    Tính Information Gain cho một đặc trưng
    
    :param df: DataFrame chứa dữ liệu
    :param feature_column: Tên cột đặc trưng
    :param target_column: Tên cột mục tiêu
    :param positive_value: Giá trị dương của cột mục tiêu
    :return: Từ điển chứa các giá trị entropy và Information Gain
    """
    # Tổng số mẫu
    total_samples = len(df)
    
    # Đếm số mẫu thuộc lớp dương
    total_positive = len(df[df[target_column] == positive_value])
    
    # Tính entropy tổng
    total_entropy = calculate_entropy(total_samples, total_positive)
    
    # Từ điển lưu kết quả
    results = {
        'E(s)': total_entropy,
        'feature_entropies': {},
        'Gain': 0
    }
    
    # Tính entropy cho từng giá trị của đặc trưng
    conditional_entropy = 0
    for feature_value in df[feature_column].unique():
        # Lọc tập con
        subset = df[df[feature_column] == feature_value]
        
        # Số mẫu của tập con
        subset_total = len(subset)
        
        # Số mẫu dương của tập con
        subset_positive = len(subset[subset[target_column] == positive_value])
        
        # Tính entropy của tập con
        subset_entropy = calculate_entropy(subset_total, subset_positive)
        
        # Lưu entropy của tập con
        results['feature_entropies'][feature_value] = subset_entropy
        
        # Tính entropy có điều kiện
        conditional_entropy += (subset_total / total_samples) * subset_entropy
    
    # Tính Information Gain
    results['Gain'] = total_entropy - conditional_entropy
    
    return results

def main():
    # Đọc file CSV
    df = pd.read_csv('decision_tree_data.csv')
    
    # Các đặc trưng cần tính Gain
    features = ['Tiet troi', 'Nhiet do', 'Do am', 'Gio']
    
    # Tính Gain cho từng đặc trưng
    for feature in features:
        print(f"\nTính Gain cho đặc trưng: {feature}")
        gain_results = calculate_feature_gain(df, feature)
        
        # In kết quả
        print(f"E(s) = {gain_results['E(s)']:.4f}")
        
        # In entropy của từng giá trị
        for value, entropy in gain_results['feature_entropies'].items():
            print(f"E(S{value}) = {entropy:.4f}")
        
        print(f"Gain({feature}) = {gain_results['Gain']:.4f}")

if __name__ == '__main__':
    main()

# Chức năng:
# 1. Tính entropy tổng
# 2. Tính entropy cho từng giá trị của đặc trưng
# 3. Tính Information Gain
# 4. Hỗ trợ tính toán cho nhiều đặc trưng