import csv
import numpy as np
import pandas as pd

# 주어진 StatisticsCalculator 클래스를 재사용
class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count if count > 0 else 0

    def calculate_std_dev(self):
        mean = self.calculate_mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        variance = sum(squared_diffs) / len(squared_diffs) if len(squared_diffs) > 0 else 0
        return variance ** 0.5

# 데이터 생성 및 통계 계산 함수
def generate_and_calculate(size, distribution_type='normal', mu=0, sigma=1):
    if distribution_type == 'normal':
        data = np.random.normal(mu, sigma, size)
    else:  # 균일 분포
        low, high = 0, 1
        data = np.random.uniform(low, high, size)

    # StatisticsCalculator 클래스 사용
    stats = StatisticsCalculator(data.tolist())
    calculated_mean = stats.calculate_mean()
    calculated_std_dev = stats.calculate_std_dev()

    # 이론적 평균과 표준 편차 계산
    if distribution_type == 'normal':
        theoretical_mean, theoretical_std_dev = mu, sigma
    else:
        theoretical_mean, theoretical_std_dev = (low + high) / 2, (high - low) / (12 ** 0.5)

    # 오류 계산
    mean_error = abs(theoretical_mean - calculated_mean)
    std_dev_error = abs(theoretical_std_dev - calculated_std_dev)

    return {
        'distribution': distribution_type,
        'calculated_mean': calculated_mean,
        'calculated_std_dev': calculated_std_dev,
        'mean_error': mean_error,
        'std_dev_error': std_dev_error
    }

# 메인 처리 함수
def main():
    size = 2000000  # 적절한 샘플 크기 설정
    normal_results = generate_and_calculate(size, 'normal', mu=0, sigma=1)
    uniform_results = generate_and_calculate(size, 'uniform')

    # 오류 출력
    print(f"Normal Distribution Mean Error: {normal_results['mean_error']}")
    print(f"Normal Distribution Std Dev Error: {normal_results['std_dev_error']}")
    print(f"Uniform Distribution Mean Error: {uniform_results['mean_error']}")
    print(f"Uniform Distribution Std Dev Error: {uniform_results['std_dev_error']}")

    # 결과를 "stat_ms.csv"로 저장
    csv_filename = 'stat_ms.csv'
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Distribution', 'Mean', 'Standard Deviation', 'Mean Error', 'Std Dev Error'])
        writer.writerow([
            normal_results['distribution'], normal_results['calculated_mean'],
            normal_results['calculated_std_dev'], normal_results['mean_error'],
            normal_results['std_dev_error']
        ])
        writer.writerow([
            uniform_results['distribution'], uniform_results['calculated_mean'],
            uniform_results['calculated_std_dev'], uniform_results['mean_error'],
            uniform_results['std_dev_error']
        ])

    # Step 4: Generate new normal distributed data with the saved mean and standard deviation
    mean_from_csv = normal_results['calculated_mean']
    std_dev_from_csv = normal_results['calculated_std_dev']
    generated_data = np.random.normal(mean_from_csv, std_dev_from_csv, size)

    # Calculate mean and standard deviation of the generated data using the StatisticsCalculator class
    generated_stats = StatisticsCalculator(generated_data.tolist())
    generated_mean = generated_stats.calculate_mean()
    generated_std_dev = generated_stats.calculate_std_dev()

    print("Generated Data Mean:", generated_mean)
    print("Generated Data Standard Deviation:", generated_std_dev)

# 프로그램 실행
if __name__ == "__main__":
    main()
