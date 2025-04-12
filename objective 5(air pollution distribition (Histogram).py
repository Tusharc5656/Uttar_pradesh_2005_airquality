import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"F:\UTTAR_pradesh_2005_air_quality.csv")

# Clean column names
data.columns = data.columns.str.strip()

# Optional: check column names to make sure they're correct
# print(data.columns)

# Create histograms for each pollutant
plt.figure(figsize=(15, 4))

# Histogram for RSPM/PM10
plt.subplot(1, 3, 1)
plt.hist(data['RSPM/PM10'].dropna(), bins=20, color='orange', edgecolor='black')
plt.title('Distribution of RSPM/PM10')
plt.xlabel('RSPM/PM10 Level')
plt.ylabel('Frequency')

# Histogram for SO2
plt.subplot(1, 3, 2)
plt.hist(data['SO2'].dropna(), bins=20, color='green', edgecolor='black')
plt.title('Distribution of SO₂')
plt.xlabel('SO₂ Level')

# Histogram for NO2
plt.subplot(1, 3, 3)
plt.hist(data['NO2'].dropna(), bins=20, color='blue', edgecolor='black')
plt.title('Distribution of NO₂')
plt.xlabel('NO₂ Level')

plt.show()
