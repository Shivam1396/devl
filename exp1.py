import pandas as pd

df=pd.read_csv("data/data/MOCK_DATA.csv")
# in below line we just update the code
# the syntax as followed df.loc[index , "key"]="value"
df.loc[0 , "first_name"]="shiv"
df.loc[2 , "gender"]="male"
new_row = pd.DataFrame([{
    "id": 108,
    "first_name": "Aditi",
    "last_name": "Sharma", uhyggtf
    "email": "aditi@example.com",
    "gender": "Female",
    "DOB": "1/1/2000",
    "salary": 45
}])

df = pd.concat([df, new_row])
print(df)
# df.loc[row_label, column_label]

l=df.head(2)
# the above line gives you 5 data only default
#  but if you want any iother no of data just give the value inside that
print(l)
print(df.shape)
# here the above code represented
#  the no of rows and column first one is for row and second one is for column
df.to_csv("new.csv") 

# df.to_csv("new.csv" index=False) 
# the index="False" this confirms that u don't need the index
# # the above line just create new csv file with the following data
