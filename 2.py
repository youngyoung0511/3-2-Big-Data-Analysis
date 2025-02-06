import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as stats

file_path = 'hw_25000.csv'
data = pd.read_csv(file_path, encoding='latin1')

data.columns = ['Index', 'Height', 'Weight']

def plot_hist_with_norm(data_column, ax, title):
    df_min, df_max = data_column.min(), data_column.max()
    df_mean, df_std = data_column.mean(), data_column.std()

    data_column.hist(bins=30, density=True, alpha=0.6, ax=ax, color='skyblue')

    df_lins = np.linspace(df_min, df_max, 100)
    df_norm = stats.norm.pdf(df_lins, df_mean, df_std)
    ax.plot(df_lins, df_norm, color='red')
    ax.set_title(title)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
plot_hist_with_norm(data['Height'], axes[0], 'Height Distribution')
plot_hist_with_norm(data['Weight'], axes[1], 'Weight Distribution')
plt.tight_layout()
plt.show()

height_mean, height_var = data['Height'].mean(), data['Height'].var()
weight_mean, weight_var = data['Weight'].mean(), data['Weight'].var()

height_random = np.random.normal(height_mean, np.sqrt(height_var), 100)
weight_random = np.random.normal(weight_mean, np.sqrt(weight_var), 100)


result_df = pd.DataFrame({'Height': height_random, 'Weight': weight_random})
result_df.to_csv('resultprob2.csv', index=False)
