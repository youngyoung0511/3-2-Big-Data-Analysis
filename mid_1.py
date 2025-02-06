import pandas as pd

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

def process_data(filename, output_filename):
    # 파일을 utf-8 또는 cp949로 읽기
    try:
        df = pd.read_csv(filename, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(filename, encoding="cp949")

    # NaN을 0으로 대체
    df = df.fillna(0)

    # "합계"가 포함된 행 제거
    df = df[~df['자치구별'].str.contains("합계", na=False)]

    # '유료관광지'인 경우만 필터링
    df_paid = df[df['관광지별'] == '유료관광지']

    # 필터링된 데이터 확인
    print("Filtered Data (Paid Attractions):")
    print(df_paid)

    # 자치구별로 그룹화하고 각 그룹에 대해 통계를 계산
    result_data = []
    for district, group in df_paid.groupby('자치구별'):
        row = {'자치구별': district}

        # 연도별 데이터 열을 가져옴
        year_columns = group.columns[2:]  # 2013부터 연도별 데이터 열을 가져옴
        year_data = group[year_columns].values.flatten()  # 모든 연도별 데이터를 평탄화

        # 통계 계산
        stats = StatisticsCalculator(year_data)
        row['mean'] = stats.calculate_mean()
        row['std_dev'] = stats.calculate_std_dev()

        # 결과 데이터에 추가
        result_data.append(row)

    # 결과를 DataFrame으로 변환 후 CSV 파일로 저장
    result_df = pd.DataFrame(result_data)

    # 결과를 utf-8로 저장
    result_df.to_csv(output_filename, index=False, encoding="utf-8-sig")

# 파일 처리
process_data("attraction_list_1.csv", "sightsee.csv")
