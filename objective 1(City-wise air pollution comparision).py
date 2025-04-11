import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv(r"F:\UTTAR_pradesh_2005_air_quality.csv")

# Remove leading/trailing spaces in column names
data.columns = data.columns.str.strip()

# Check column names (optional)
print(data.columns)

# Group by city and calculate average PM10
avg_pm10 = data.groupby('City/Town/Village/Area')['RSPM/PM10'].mean()

# Sort cities by PM10 (high to low)
avg_pm10 = avg_pm10.sort_values(ascending=False)

# Plot bar chart
plt.bar(avg_pm10.index, avg_pm10.values, color='orange')
plt.xticks(rotation=45)
plt.ylabel('PM10')
plt.title('Average PM10 by City')
plt.show()
