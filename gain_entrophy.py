import math
import pandas as pd

# doc file csv 
df = pd.read_csv('decision_tree_data.csv')
df_filtered = df[df["Choi cau long"] == "co"]

# lay du lieu cot tiet troi
tiet_troi = df['Tiet troi'].tolist()
choi_cau_long = df['Choi cau long'].tolist()

dem = 0
dem_nang = 0
dem_mua = 0
dem_nhieu_may = 0
dem_nang_1 = 0
dem_mua_1 = 0 
dem_nhieu_may_1 = 0
for index, row in df.iterrows():
    if row["Choi cau long"] == "Co":
        dem += 1
        if row["Tiet troi"] == "Nang":
            dem_nang += 1
        elif row["Tiet troi"] == "Nhieu may":
            dem_nhieu_may += 1
        elif row["Tiet troi"] == "Mua":
            dem_mua += 1
for i in tiet_troi:
    if i == "Nang":
        dem_nang_1 += 1
    elif i == "Nhieu may":
        dem_nhieu_may_1 += 1
    elif i == "Mua":
        dem_mua_1 += 1
p1 = dem / 14
p2 = (14-dem) / 14
a = -(p1*math.log2(p1)) - (p2*math.log2(p2))

p1_nang = dem_nang / dem_nang_1
p1_mua = dem_mua / dem_mua_1
p1_nhieu_may = dem_nhieu_may / dem_nhieu_may_1
p2_nang = (dem_nang_1 - dem_nang) / dem_nang_1
p2_mua = (dem_mua_1 - dem_mua) / dem_mua_1

b = -(p1_nang * math.log2(p1_nang)) - (p2_nang * math.log2(p2_nang))
c = -(p1_mua * math.log2(p1_mua)) - (p2_mua * math.log2(p2_mua))
d = -(p1_nhieu_may * math.log2(p1_nhieu_may))
Gain_tt = a - (dem_nang_1/14) * b - (dem_mua_1/14) * c - (dem_nhieu_may_1/14) * d
print(f"E(s) = {a}")
print(f"E(Snang) = {b}")
print(f"E(Smua) = {c}")
print(f"E(Snhieu may) = {d}")
print(f"Gain(s,tt) = {Gain_tt}")


# lay du lieu cot nhiet do
nhiet_do = df['Nhiet do'].tolist()
choi_cau_long = df['Choi cau long'].tolist()

dem = 0
dem_nong = 0
dem_mat = 0
dem_lanh = 0
dem_nong_1 = 0
dem_mat_1 = 0 
dem_lanh_1 = 0
for index, row in df.iterrows():
    if row["Choi cau long"] == "Co":
        dem += 1
        if row["Nhiet do"] == "Nong":
            dem_nong += 1
        elif row["Nhiet do"] == "Mat":
            dem_mat += 1
        elif row["Nhiet do"] == "Lanh":
            dem_lanh += 1
for i in nhiet_do:
    if i == "Nong":
        dem_nong_1 += 1
    elif i == "Mat":
        dem_mat_1 += 1
    elif i == "Lanh":
        dem_lanh_1 += 1

p1_nong = dem_nong / dem_nong_1
p1_mat = dem_mat / dem_mat_1
p1_lanh = dem_lanh / dem_lanh_1
p2_nong = (dem_nong_1 - dem_nong) / dem_nong_1
p2_mat = (dem_mat_1 - dem_mat) / dem_mat_1
p2_lanh = (dem_lanh_1 - dem_lanh) / dem_lanh_1


e = -(p1_nong * math.log2(p1_nong)) - (p2_nong * math.log2(p2_nong))
f = -(p1_mat * math.log2(p1_mat)) - (p2_mat * math.log2(p2_mat))
g = -(p1_lanh * math.log2(p1_lanh)) - (p2_lanh * math.log2(p2_lanh))

Gain_nd = a - (dem_nong_1/14) * e - (dem_mat_1/14) * f - (dem_lanh_1/14) * g
print(f"E(s) = {a}")
print(f"E(Snong) = {e}")
print(f"E(Smat) = {f}")
print(f"E(Slanh) = {g}")
print(f"Gain(s,nd) = {Gain_nd}")
