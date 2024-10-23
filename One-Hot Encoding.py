import pandas as pd
import numpy as np

data = {'Category': ['Low', 'Medium', 'High', 'Medium', 'Low', 'High']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


def one_hot_encoding(df, column):
    
    one_hot_df = pd.get_dummies(df[column], prefix=column)
    df = pd.concat([df, one_hot_df], axis=1)
    return df

df = one_hot_encoding(df, 'Category')

print("\nDataFrame after One-Hot Encoding:")
print(df)