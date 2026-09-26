import pandas as pd
data1=[{"name":"shivam" , "Age":21 , "department":"Senior-Developer" , "company":"MIT-ADT UNIVERSITY" , "Salary":200000},
{"name": "Aarav", "Age": 24, "department": "Software-Developer", "company": "TCS", "Salary": 85000},
{"name": "Aditya", "Age": 27, "department": "Senior-Developer", "company": "Infosys", "Salary": 145000},
{"name": "Rohan", "Age": 23, "department": "Backend-Developer", "company": "Wipro", "Salary": 95000},
{"name": "Arjun", "Age": 29, "department": "Tech-Lead", "company": "Accenture", "Salary": 180000},
{"name": "Rahul", "Age": 26, "department": "Frontend-Developer", "company": "Cognizant", "Salary": 110000},
{"name": "Vikram", "Age": 31, "department": "Senior-Developer", "company": "Microsoft India", "Salary": 220000},
{"name": "Karan", "Age": 25, "department": "Full-Stack-Developer", "company": "Google India", "Salary": 200000},
{"name": "Siddharth", "Age": 28, "department": "DevOps-Engineer", "company": "Amazon India", "Salary": 175000},
{"name": "Ankit", "Age": 22, "department": "Junior-Developer", "company": "Tech Mahindra", "Salary": 70000}]
data2=[
{"name": "Neha", "Age": 24, "department": "Data-Analyst", "company": "HCL", "Salary": 90000},
{"name": "Priya", "Age": 26, "department": "Software-Developer", "company": "Infosys", "Salary": 125000},
{"name": "Riya", "Age": 29, "department": "Senior-Developer", "company": "TCS", "Salary": 160000},
{"name": "Sneha", "Age": 23, "department": "Frontend-Developer", "company": "Wipro", "Salary": 85000},
{"name": "Nikhil", "Age": 30, "department": "Tech-Lead", "company": "Accenture", "Salary": 190000},
{"name": "Akash", "Age": 25, "department": "Backend-Developer", "company": "Cognizant", "Salary": 115000},
{"name": "Manish", "Age": 32, "department": "DevOps-Engineer", "company": "Amazon India", "Salary": 210000},
{"name": "Pooja", "Age": 27, "department": "Full-Stack-Developer", "company": "Google India", "Salary": 195000},
{"name": "Nihar", "Age": 28, "department": "Data-Engineer", "company": "Microsoft India", "Salary": 180000},
{"name": "Meera", "Age": 22, "department": "Junior-Developer", "company": "Tech Mahindra", "Salary": 75000}]
data3=[
{"name": "Amit", "Age": 25, "department": "Software-Developer", "company": "HCL", "Salary": 100000},
{"name": "Kavya", "Age": 27, "department": "Data-Analyst", "company": "TCS", "Salary": 120000},
{"name": "Varun", "Age": 30, "department": "Senior-Developer", "company": "Infosys", "Salary": 155000},
{"name": "Isha", "Age": 24, "department": "Frontend-Developer", "company": "Wipro", "Salary": 90000},
{"name": "Saurabh", "Age": 33, "department": "Tech-Lead", "company": "Accenture", "Salary": 205000},
{"name": "Divya", "Age": 26, "department": "Backend-Developer", "company": "Cognizant", "Salary": 110000},
{"name": "Rohit", "Age": 31, "department": "DevOps-Engineer", "company": "Amazon India", "Salary": 185000},
{"name": "Tanvi", "Age": 28, "department": "Full-Stack-Developer", "company": "Google India", "Salary": 210000},
{"name": "Deepak", "Age": 29, "department": "Data-Engineer", "company": "Microsoft India", "Salary": 175000},
{"name": "Simran", "Age": 23, "department": "Junior-Developer", "company": "Tech Mahindra", "Salary": 72000}]
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df = pd.concat([df1, df2, df3], ignore_index=True)
df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")
print(df)
