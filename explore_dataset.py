import kagglehub

# Download latest version
path = kagglehub.dataset_download("abhisheksubhashswami/fruits-and-vegetables")

print("Path to dataset files:", path)
import os

print("Files in dataset folder:")
print(os.listdir(path))

import pandas as pd

# Replace 'filename.csv' with the actual CSV file name you see in the folder
df = pd.read_csv(os.path.join(path, 'filename.csv'))

# Show the first few rows
print(df.head())

# Show column names
print("Columns:", df.columns.tolist())

