import pandas as pd
import matplotlib.pyplot as plt
data=[
{"name":"shivam", "Age":21, "department":"Senior-Developer", "company":"MIT-ADT UNIVERSITY", "Salary":200000},
{"name": "Aarav", "Age": 24, "department": "Software-Developer", "company": "TCS", "Salary": 85000},
{"name": "Aditya", "Age": 27, "department": "Senior-Developer", "company": "Infosys", "Salary": 145000},
{"name": "Rohan", "Age": 24, "department": "Backend-Developer", "company": "Wipro", "Salary": 95000},
{"name": "Arjun", "Age": None, "department": "Tech-Lead", "company": "Accenture", "Salary": 180000},
{"name": "Rahul", "Age": 26, "department": "Frontend-Developer", "company": "Cognizant", "Salary": 110000},
{"name": "Vikram", "Age": 31, "department": "Senior-Developer", "company": "Microsoft India", "Salary": 220000},
{"name": "Karan", "Age": 25, "department": "Full-Stack-Developer", "company": "Google India", "Salary": 200000},
{"name": "Siddharth", "Age": None, "department": "DevOps-Engineer", "company": "Amazon India", "Salary": 175000},
{"name": "Ankit", "Age": 22, "department": "Junior-Developer", "company": "Tech Mahindra", "Salary": 70000},
{"name":"shivam", "Age":21, "department":"Senior-Developer", "company":"MIT-ADT UNIVERSITY", "Salary":200000},
{"name": "Aarav", "Age": 24, "department": "Software-Developer", "company": "TCS", "Salary": 85000}
]
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")
print("Missing values:")
print(df.isnull().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nData types:" , df.dtypes)
print("REMOVING DUPLICATES DATA")
df=df.drop_duplicates()
print(df.duplicated().sum())
print("FILL THE MISSING NUMBER")
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df)
print(df.isnull().sum())
plt.plot(df["Age"], df["Salary"])

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

plt.show()
