import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

file_path = 'London.csv'
data = pd.read_csv(file_path, encoding='cp949')

print("Columns in CSV:", data.columns)

data = data.rename(columns={
    'Property Name': 'Property Name',
    'House Type': 'House Type',
    'Area in sq ft': 'Area',
    'No. of Bedrooms': 'Number of Bedrooms',
    'No. of Bathrooms': 'Number of Bathrooms',
    'Location': 'Location',
    'City/County': 'City/County',
    'Postal Code': 'Postal Code'
})

house_types = data['House Type'].unique()

for house in house_types:
    house_data = data[data['House Type'] == house]
    x = house_data['Area']
    y = house_data['Price']

    if len(x) > 1:
        slope, intercept, r_value, _, _ = linregress(x, y)
        line = slope * x + intercept
        tolerance = abs(line - y).mean()

        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, color='blue', label='Data Points')
        plt.plot(x, line, color='red', label=f'Regression Line (R²={r_value**2:.2f})')
        plt.fill_between(x, line - tolerance, line + tolerance, color='gray', alpha=0.2, label='Tolerance Interval')
        plt.title(f'Linear Regression for {house}')
        plt.xlabel('Area (sq ft)')
        plt.ylabel('Price (£)')
        plt.legend()
        plt.show()


averages = data.groupby('House Type').agg({
    'Price': 'mean',
    'Area': 'mean',
    'Number of Bedrooms': 'mean',
    'Number of Bathrooms': 'mean'
}).reset_index()

print("Average Values per House Type:")
print(averages)

for _, row in averages.iterrows():
    print(f"House Type: {row['House Type']}")
    print(f" - Average Price: {row['Price']:.2f} £")
    print(f" - Average Area: {row['Area']:.2f} sq ft")
    print(f" - Average Number of Bedrooms: {row['Number of Bedrooms']:.1f}")
    print(f" - Average Number of Bathrooms: {row['Number of Bathrooms']:.1f}")
    print("-" * 40)
