<<<<<<< HEAD
import pandas as pd

# Enter the no of Excel no
print('Enter no of file : ')
i = int(input())

# store the File Descriptor in list
lst = list()
for fd in range(0,i) :
    temp = input('Enter the File Path')
    k = pd.read_excel(str(temp))
    lst.append(k)
    
#Concate the file
dp = pd.concat(lst,axis=1)

#Export Dataframe to Excel file
dp.to_excel('D:\Java Program\Data.xlsx',index=True)


=======
import pandas as pd

# Enter the no of Excel no
print('Enter no of file : ')
i = int(input())

# store the File Descriptor in list
lst = list()
for fd in range(0,i) :
    temp = input('Enter the File Path')
    k = pd.read_excel(str(temp))
    lst.append(k)
    
#Concate the file
dp = pd.concat(lst,axis=1)

#Export Dataframe to Excel file
dp.to_excel('D:\Java Program\Data.xlsx',index=True)
>>>>>>> 78e95ed975954aaf3084adb9b0b7d0a2b721b2d8
