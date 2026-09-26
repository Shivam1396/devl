import pandas as pd
data = [
{"name":"shivam", "Age":21, "department":"Senior-Developer", "company":"MIT-ADT UNIVERSITY", "Salary":200000},
{"name":"Aarav", "Age":24, "department":"Software-Developer", "company":"TCS", "Salary":85000},
{"name":"Aditya", "Age":27, "department":"Senior-Developer", "company":"Infosys", "Salary":145000},
{"name":"Rohan", "Age":23, "department":"Backend-Developer", "company":"Wipro", "Salary":95000},
{"name":"Arjun", "Age":29, "department":"Tech-Lead", "company":"Accenture", "Salary":180000},
{"name":"Rahul", "Age":26, "department":"Frontend-Developer", "company":"Cognizant", "Salary":110000},
{"name":"Vikram", "Age":31, "department":"Senior-Developer", "company":"Microsoft India", "Salary":220000},
{"name":"Karan", "Age":25, "department":"Full-Stack-Developer", "company":"Google India", "Salary":200000},
{"name":"Siddharth", "Age":28, "department":"DevOps-Engineer", "company":"Amazon India", "Salary":175000},
{"name":"Ankit", "Age":22, "department":"Junior-Developer", "company":"Tech Mahindra", "Salary":70000}
]
df = pd.DataFrame(data)
print("EXTRACTED DATA:")
print(df)
df["Annual Salary"] = df["Salary"] * 12
df["Salary in Lakhs"] = df["Salary"] / 100000
print("\nTRANSFORMED DATA:")
print(df)
df.to_csv("final_employee_data.csv", index=False)
print("\nETL PROCESS COMPLETED!")
print("Data saved to final_employee_data.csv")
