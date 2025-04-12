import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the CSV file
data = pd.read_csv(r"F:\UTTAR_pradesh_2005_air_quality.csv")

# Step 2: Clean column names
data.columns = data.columns.str.strip()

# Step 3: Show basic stats
print("Mean values:\n", data[['RSPM/PM10', 'SO2', 'NO2']].mean())
print("\nMedian values:\n", data[['RSPM/PM10', 'SO2', 'NO2']].median())
print("\nStandard deviation:\n", data[['RSPM/PM10', 'SO2', 'NO2']].std())

# Step 4: Most and least polluted cities (by average PM10)
city_avg = data.groupby('City/Town/Village/Area')['RSPM/PM10'].mean()
most_polluted = city_avg.idxmax()
least_polluted = city_avg.idxmin()
print(f"\nMost polluted city: {most_polluted} ({city_avg.max():.2f})")
print(f"Least polluted city: {least_polluted} ({city_avg.min():.2f})")

# Step 5: Line plot of pollution trend over time
plt.figure(figsize=(10, 5))
data['Sampling Date'] = pd.to_datetime(data['Sampling Date'], errors='coerce')
data_sorted = data.sort_values(by='Sampling Date')
plt.plot(data_sorted['Sampling Date'], data_sorted['RSPM/PM10'], color='orange')
plt.title('PM10 Trend Over Time')
plt.xlabel('Date')
plt.ylabel('PM10 Level')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 6: Heatmap to show correlation between pollutants
plt.figure(figsize=(6, 4))
corr = data[['RSPM/PM10', 'SO2', 'NO2']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Pollutants')
plt.show()
