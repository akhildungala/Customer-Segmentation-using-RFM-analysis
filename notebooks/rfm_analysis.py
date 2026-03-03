import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_excel("../Data/Online Retail.xlsx")

print("Dataset Loaded Successfully")
df.head()
print(df.shape)
print(df.info())
print(df.isnull().sum())


# Remove rows where CustomerID is missing
df = df.dropna(subset=['CustomerID'])

# Remove negative or zero quantities (returns)
df = df[df['Quantity'] > 0]

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("Data Cleaning Completed")

snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

