import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/MOCK_DATA.csv")
print(df)

print("\nNumber of duplicate rows:", df.duplicated().sum())

# duplicates=df[df.duplicated()]
# print(duplicates)

duplicates = df.duplicated()
print("duplicates:",duplicates)
df=df.drop_duplicates()
# df["Name"]=df["Name"].fillna("Unknown")
df["DOB"]=df["DOB"].fillna("01-01-1990")
print(df)



# print(df.info())
# print(df.describe())
# print(df.isnull().sum())