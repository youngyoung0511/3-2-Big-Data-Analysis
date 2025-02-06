import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

file_path = 'Zillow.csv'
data = pd.read_csv(file_path, encoding='latin1')


data.columns = ['Index', 'Living Space', 'Beds', 'Baths', 'Zip', 'Year', 'List Price']


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
data.groupby('Year')['List Price'].mean().plot(kind='bar', ax=axes[0], title='Avg Housing Price vs Year')
data.groupby('Year')['Living Space'].mean().plot(kind='bar', ax=axes[1], title='Avg Living Space vs Year')
data.groupby('Year')['Baths'].mean().plot(kind='bar', ax=axes[2], title='Avg number of Bathrooms vs Year')
plt.tight_layout()
plt.show()


columns = ['List Price', 'Living Space', 'Baths']
corr_results = {}
for col1, col2 in combinations(columns, 2):
    corr = data[col1].corr(data[col2])
    corr_results[(col1, col2)] = corr

sorted_corr = sorted(corr_results.items(), key=lambda x: abs(x[1]), reverse=True)
for pair, value in sorted_corr:
    print(f'{pair[0]} and {pair[1]}: {value:.2f}')
print(f'Highest correlation: {sorted_corr[0][0]} with {sorted_corr[0][1]} ({sorted_corr[0][1]:.2f})')
