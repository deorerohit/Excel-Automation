import pandas as pd

print('Enter no of file : ')
i = int(input())

# Creating list of col_names in given xlsx files
lst_column_names = list()
filesD = []

for fd in range(0, i):
    temp = input('Enter the File Path')
    k = pd.read_excel(str(temp))
    filesD.append(k)
    lst_column_names.append(k.columns.ravel())

# finding the common column
com_column = list(set.intersection(*map(set, lst_column_names)))

df_com_column = []
# Reading common column from each .xlsx file
for i in filesD:
    for j in com_column:
        temp_df = pd.DataFrame(i[str(j)])
        print(temp_df)
        df_com_column.append(temp_df)

# Writing Common column of all files in new created .xlsx File column
dp = pd.concat(df_com_column, axis=1)
dp.to_excel('D:\\text.xlsx', index=False)

