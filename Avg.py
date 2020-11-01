import pandas as pd

dp = pd.read_excel("D:\\Attendance.xlsx")

df = dp.mean(axis=1)


a = pd.concat([dp, df], axis=1)

a.to_excel('D:\\Attendance.xlsx', index=False)
