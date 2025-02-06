# 20221333 김서영
# Assignment2

# 정규분포, 카이제곱 분포, 균등분포에서 각각 100,000개의 값을 생성
# 각 분포에 대해 샘플 크기(10,000, 20,000, 30,000, 50,000, 100,000)에 따라 통계결과 출력
# 통계결과: 평균, 표준편차, 분산, 최대값, 최소값, 백분위(5,10,20,40,80,90)
# describe() 함수는 사용하지 말기
# csv 파일로 저장

import numpy as np
import pandas as pd

# 분포 생성
n_samples = 100000
#정규 분포
normal_dist = np.random.normal(0, 1, n_samples)
#카이제곱 분포
chi_square_dist = np.random.chisquare(2, n_samples)
#균등 분포
uniform_dist = np.random.uniform(0, 1, n_samples)

# 샘플 크기
sample_sizes = [10000, 20000, 30000, 50000, 100000]


# numpy를 사용한 통계값 계산
def calculate_statistics_numpy(data):
    stats = {
        'mean': np.mean(data),
        'std_dev': np.std(data),
        'variance': np.var(data),
        'max': np.max(data),
        'min': np.min(data),
        '5_percentile': np.percentile(data, 5),
        '10_percentile': np.percentile(data, 10),
        '20_percentile': np.percentile(data, 20),
        '40_percentile': np.percentile(data, 40),
        '80_percentile': np.percentile(data, 80),
        '90_percentile': np.percentile(data, 90)
    }
    return stats


# pandas를 사용한 통계 계산 함수
def calculate_statistics_pandas(data):
    stats = {
        'mean': pd.Series(data).mean(),
        'std_dev': pd.Series(data).std(),
        'variance': pd.Series(data).var(),
        'max': pd.Series(data).max(),
        'min': pd.Series(data).min(),
        '5_percentile': pd.Series(data).quantile(0.05),
        '10_percentile': pd.Series(data).quantile(0.10),
        '20_percentile': pd.Series(data).quantile(0.20),
        '40_percentile': pd.Series(data).quantile(0.40),
        '80_percentile': pd.Series(data).quantile(0.80),
        '90_percentile': pd.Series(data).quantile(0.90)
    }
    return stats


# 각 분포의 샘플 사이즈 담을 list 생성
statistics_results_numpy = []
statistics_results_pandas = []

# 각 분포의 샘플 사이즈의 통계값 계산 (numpy 150개, pandas 150개)
for size in sample_sizes:
    for dist_name, dist_data in zip(['Normal', 'Chi-square', 'Uniform'],
                                    [normal_dist, chi_square_dist, uniform_dist]):
        sample = dist_data[:size]

        # numpy 사용
        stats_numpy = calculate_statistics_numpy(sample)
        stats_numpy['distribution'] = dist_name
        stats_numpy['sample_size'] = size
        statistics_results_numpy.append(stats_numpy)

        # pandas 사용
        stats_pandas = calculate_statistics_pandas(sample)
        stats_pandas['distribution'] = dist_name
        stats_pandas['sample_size'] = size
        statistics_results_pandas.append(stats_pandas)

# numpy와 pandas 통계 결과 각각 150개
statistics_df_numpy = pd.DataFrame(statistics_results_numpy)
statistics_df_pandas = pd.DataFrame(statistics_results_pandas)

# csv 파일로 저장
distributions_df = pd.DataFrame({
    'Normal': normal_dist,
    'Chi-square': chi_square_dist,
    'Uniform': uniform_dist
})
distributions_df.to_csv('C:/Users/young/Downloads/distributions.csv', index=False)
statistics_df_numpy.to_csv('C:/Users/young/Downloads/statistics_results_numpy.csv', index=False)
statistics_df_pandas.to_csv('C:/Users/young/Downloads/statistics_results_pandas.csv', index=False)

