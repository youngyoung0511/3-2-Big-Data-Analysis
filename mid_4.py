import numpy as np
import pandas as pd

# 주어진 숫자 목록
data = [
    955, 890, 519, 707, 634, 689, 177, 404, 375, 458, 607, 704, 219, 804,
    983, 848, 808, 766, 868, 981, 803, 149, 237, 778, 671, 555, 693, 429,
    486, 602, 160, 808, 382, 852, 162, 169, 4, 300, 73, 907, 199, 548,
    867, 567, 568, 242, 737, 312, 225, 170, 975, 539, 665, 631, 286, 78,
    216, 84, 127, 19, 133, 970, 296, 622, 874, 949, 809, 616, 379, 451,
    498, 420, 442, 461, 183, 760, 766, 958, 822, 2, 891, 518, 432, 363,
    517, 561, 871, 107, 744, 529, 38, 659, 413, 674, 522, 210, 711, 987,
    138, 231, 53, 382, 456, 691, 14, 284, 861, 349, 761, 478, 604, 491,
    582, 473, 321, 29, 706, 525, 221, 498, 684, 241, 602, 695, 51, 266,
    342
]

# NumPy 계산
data_np = np.array(data)
mean_np = np.mean(data_np)
variance_np = np.var(data_np)
std_dev_np = np.std(data_np)
median_np = np.median(data_np)
percentile_20_np = np.percentile(data_np, 20)
percentile_80_np = np.percentile(data_np, 80)

# Pandas 계산
data_pd = pd.Series(data)
mean_pd = data_pd.mean()
variance_pd = data_pd.var()
std_dev_pd = data_pd.std()
median_pd = data_pd.median()
percentile_20_pd = data_pd.quantile(0.2)
percentile_80_pd = data_pd.quantile(0.8)

# 결과 출력
print("NumPy Calculations:")
print(f"Mean (NumPy): {mean_np}")
print(f"Variance (NumPy): {variance_np}")
print(f"Standard Deviation (NumPy): {std_dev_np}")
print(f"Median (NumPy): {median_np}")
print(f"20th Percentile (NumPy): {percentile_20_np}")
print(f"80th Percentile (NumPy): {percentile_80_np}")

print("\nPandas Calculations:")
print(f"Mean (Pandas): {mean_pd}")
print(f"Variance (Pandas): {variance_pd}")
print(f"Standard Deviation (Pandas): {std_dev_pd}")
print(f"Median (Pandas): {median_pd}")
print(f"20th Percentile (Pandas): {percentile_20_pd}")
print(f"80th Percentile (Pandas): {percentile_80_pd}")

# 차이 계산
print("\nDifferences between NumPy and Pandas:")
print(f"Mean Difference: {mean_np - mean_pd}")
print(f"Variance Difference: {variance_np - variance_pd}")
print(f"Standard Deviation Difference: {std_dev_np - std_dev_pd}")
print(f"Median Difference: {median_np - median_pd}")
print(f"20th Percentile Difference: {percentile_20_np - percentile_20_pd}")
print(f"80th Percentile Difference: {percentile_80_np - percentile_80_pd}")
