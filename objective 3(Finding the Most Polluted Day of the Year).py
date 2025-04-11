import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv(r"F:\UTTAR_pradesh_2005_air_quality.csv")

# Clean column names
data.columns = data.columns.str.strip()

# Convert 'Date' column to datetime
data['Sampling Date'] = pd.to_datetime(data['Sampling Date'], errors='coerce')

# Drop rows with missing Date or PM10
data = data.dropna(subset=['Sampling Date', 'RSPM/PM10'])

# Find the most polluted day
max_pm10 = data['RSPM/PM10'].max()
most_polluted = data[data['RSPM/PM10'] == max_pm10].iloc[0]

# Scatter plot
plt.figure(figsize=(14, 6))
plt.scatter(data['Sampling Date'], data['RSPM/PM10'], color='skyblue', label='PM10 Level')
plt.scatter(most_polluted['Sampling Date'], most_polluted['RSPM/PM10'], color='red', label='Most Polluted Day')

# Labels and title
plt.xlabel('Sampling Date')
plt.ylabel('PM10 Level')
plt.title('Most Polluted Day in Uttar Pradesh (2005)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Print details
print("Most polluted day:", most_polluted['Sampling Date'].date())
print("PM10 level on that day:", most_polluted['RSPM/PM10'])
