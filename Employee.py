import pandas as pd
df = pd.read_csv("data1/MOCK_DATA (2).csv")
df["money"] = df["money"].replace(r'[\$,]', '', regex=True)
df["annual_salary"] = pd.to_numeric(df["money"])* 12
df.to_csv("annualsalary.csv", index=False)
print(df)