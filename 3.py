import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터 로드
file_path = "student_health_2.csv"
data = pd.read_csv(file_path, encoding='euc-kr')

# 2. 필요한 열만 선택
columns_needed = ['학년', '키', '몸무게', '수축기', '이완기']
data = data[columns_needed]

# 3. 데이터 전처리 (결측값 확인 및 학년 정수형 변환)
data['학년'] = data['학년'].astype(int)  # 학년을 정수형으로 변환


# 5. 학년별 평균 계산
averages = data.groupby('학년').agg({
    '키': 'mean',
    '몸무게': 'mean',
    '수축기': 'mean',
    '이완기': 'mean'
}).reset_index()

# 모든 학년 고정
grades = [1, 2, 3, 4, 5, 6]
average_height_fixed = [averages[averages['학년'] == grade]['키'].values[0] if grade in averages['학년'].values else 0 for grade in grades]
average_weight_fixed = [averages[averages['학년'] == grade]['몸무게'].values[0] if grade in averages['학년'].values else 0 for grade in grades]
average_systolic_fixed = [averages[averages['학년'] == grade]['수축기'].values[0] if grade in averages['학년'].values else 0 for grade in grades]
average_diastolic_fixed = [averages[averages['학년'] == grade]['이완기'].values[0] if grade in averages['학년'].values else 0 for grade in grades]

# 6. 그래프 생성 함수
def plot_bar(x, y, title, xlabel, ylabel, color, edgecolor='black'):
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color=color, edgecolor=edgecolor)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(x, labels=x, fontsize=12)  # X축 값 강제 설정
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

# Graph 1: Number of students per grade
plot_bar(
    x=grades,
    y=[data['학년'].value_counts().get(grade, 0) for grade in grades],
    title='Number of Students per Grade',
    xlabel='Grade',
    ylabel='Number of Students',
    color='skyblue'
)

# Graph 2: Average height per grade
plot_bar(
    x=grades,
    y=average_height_fixed,
    title='Average Height per Grade',
    xlabel='Grade',
    ylabel='Height (cm)',
    color='lightgreen'
)

# Graph 3: Average weight per grade
plot_bar(
    x=grades,
    y=average_weight_fixed,
    title='Average Weight per Grade',
    xlabel='Grade',
    ylabel='Weight (kg)',
    color='orange'
)

# Graph 4: Average systolic blood pressure per grade
plot_bar(
    x=grades,
    y=average_systolic_fixed,
    title='Average Systolic Blood Pressure per Grade',
    xlabel='Grade',
    ylabel='Systolic BP (mmHg)',
    color='pink'
)

# Graph 5: Average diastolic blood pressure per grade
plot_bar(
    x=grades,
    y=average_diastolic_fixed,
    title='Average Diastolic Blood Pressure per Grade',
    xlabel='Grade',
    ylabel='Diastolic BP (mmHg)',
    color='purple'
)
