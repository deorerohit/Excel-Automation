import pandas as pd

print('Enter no of file : ')
i = int(input())

# Creating list of col_names in given xlsx files
lst = list()
filesD = []

for fd in range(0, i):
    temp = input('Enter the File Path')
    k = pd.read_excel(str(temp))
    filesD.append(k)
    lst.append(k.columns.ravel())

# finding the common column
com = list(set.intersection(*map(set, lst)))

p = []
# Reading common column from each .xlsx file
for i in filesD:
    for j in com:
        df = pd.DataFrame(i[str(j)])
        print(df)
        p.append(df)

#Writing Common column of all files in new created .xlsx File column
dp = pd.concat(p, axis=1)
dp.to_excel('D:\\text.xlsx', index=False)
