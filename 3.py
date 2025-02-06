import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

file_path = 'student_health_2.csv'
data = pd.read_csv(file_path, encoding='cp949')
data = data.rename(columns={'학교명': 'School', '학년': 'Grade', '키': 'Height', '성별': 'Gender'})

unique_schools = data['School'].unique()
school_mapping = {school: f"School_{i+1}" for i, school in enumerate(unique_schools)}
data['School'] = data['School'].map(school_mapping)

data = data.dropna(subset=['Height'])

grade_school_avg = data.groupby(['School', 'Grade'], observed=False)['Height'].mean().unstack()

grade_school_avg = grade_school_avg.fillna(0)

plt.figure(figsize=(12, 8))
sns.heatmap(grade_school_avg, annot=True, cmap='coolwarm', cbar_kws={'label': 'Average Height'}, fmt='.1f')
plt.title('Colormap of Height: Grade vs School')
plt.xlabel('Grade'), plt.ylabel('School'), plt.show()

grade_means = data.groupby('Grade')['Height'].mean()
print("Mean height of each grade:\n", grade_means)

school_corr = {s: (pearsonr(grade_school_avg.loc[s], grade_means)[0] if (grade_school_avg.loc[s] > 0).any() else np.nan)
               for s in grade_school_avg.index}

print("Pearson correlation coefficients:")
for s, c in school_corr.items():
    print(f"{s}: {c:.2f}" if not np.isnan(c) else f"{s}: No valid data")

valid_corr = {k: v for k, v in school_corr.items() if not np.isnan(v)}
if valid_corr:
    max_school = max(valid_corr, key=valid_corr.get)
    print(f"Highest correlation is with {max_school}: {valid_corr[max_school]:.2f}")
else:
    print("No valid correlation data.")
