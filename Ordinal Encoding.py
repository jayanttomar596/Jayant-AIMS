import pandas as pd
import numpy as np


data = {'Category': ['Low', 'Medium', 'High', 'Medium', 'Low', 'High']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


def ordinal_encoding(df, column, categories):
    ordinal_mapping = {category: idx for idx, category in enumerate(categories)}
    df[column + '_ordinal'] = df[column].map(ordinal_mapping)
    return df


categories = ['Low', 'Medium', 'High']  
df = ordinal_encoding(df, 'Category', categories)

print("\nDataFrame after Ordinal Encoding:")
print(df)