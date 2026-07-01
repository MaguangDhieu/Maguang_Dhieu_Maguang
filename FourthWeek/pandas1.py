import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29]
}
df = pd.DataFrame(data)
print(df)
print(df['Name'].iloc[0])
print(df['Age'].iloc[0])
print(df.loc[1])
print(pd.__version__)