import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
data = pd.read_csv(r"F:\UTTAR_pradesh_2005_air_quality.csv")

# Step 2: Clean column names
data.columns = data.columns.str.strip()

# Step 3: Convert date column to datetime format
data['Sampling Date'] = pd.to_datetime(data['Sampling Date'], errors='coerce')

# Step 4: Extract month from the date
data['Month'] = data['Sampling Date'].dt.month

# Step 5: Group by month and calculate average values for PM10, SO2, and NO2
monthly_avg = data.groupby('Month')[['RSPM/PM10', 'SO2', 'NO2']].mean()

# Step 6: Plot line graphs for each pollutant
plt.figure(figsize=(10, 6))

plt.plot(monthly_avg.index, monthly_avg['RSPM/PM10'], label='RSPM/PM10', marker='o')
plt.plot(monthly_avg.index, monthly_avg['SO2'], label='SO2', marker='o')
plt.plot(monthly_avg.index, monthly_avg['NO2'], label='NO2', marker='o')

plt.title('Monthly Average Pollution Levels')
plt.xlabel('Month')
plt.ylabel('Pollution Level')
plt.xticks(range(1, 13))
plt.grid(True)
plt.legend()
plt.show()
