import pandas as pd
import matplotlib.pyplot as plt

# workbook='sampledata.xlsx'
workbook1='sampledata1.xlsx'

df=pd.read_excel(workbook1)
X_value=input('Enter column name for X axis \n ')
Y_value=input('Enter column name for Y axis \n ')

values=df[[X_value,Y_value]]
print(values)

axes= values.plot.bar(x=X_value,y=Y_value,rot=0)
plt.show()