# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
df= pd.read_csv(r'C:\Users\Julius\Desktop\Training and Interns\Uptrail intern\Week 1\Week 1 project\customer_signups.csv')

df
df.dtypes
df['gender'].value_counts()

import matplotlib.pyplot as plt

# Count occurrences of each gender
gender_counts = df['gender'].value_counts()

# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Gender Distribution')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()