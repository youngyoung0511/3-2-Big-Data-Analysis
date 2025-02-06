import pandas as pd

def verify_data(filename):
    # CSV 파일 읽기 (구분자를 자동으로 감지)
    df = pd.read_csv(filename, encoding='utf-8')

    # 열 이름의 공백 제거
    df.columns = df.columns.str.strip()

    # 필요한 열이 존재하는지 확인
    required_columns = ['Region ID', '2012', '2017', 'Total']
    for col in required_columns:
        if col not in df.columns:
            print(f"Required column '{col}' is missing from the data.")
            print("Available columns:", df.columns.tolist())  # 현재 열 목록 출력
            return

    # 각 지역별로 2012년과 2017년의 합계를 계산
    df['Calculated_Total'] = df['2012'] + df['2017']

    # True/False 비교
    df['Match'] = df['Total'] == df['Calculated_Total']

    # 결과 출력
    for index, row in df.iterrows():
        print(f"Region ID: {row['Region ID']}, Match: {row['Match']}")

        # 일치하지 않는 경우 차이를 출력
        if not row['Match']:
            gap = row['Total'] - row['Calculated_Total']
            print(f"Gap for Region ID {row['Region ID']}: {gap}")

# 파일 처리
verify_data("seoul_ems_test.csv")
