# D:\Photos & VIdeos\Family Photos\DataForPandas.xlsx
# D:\Photos & VIdeos\Family Photos\Zanotexcel.xlsx

import pandas as pd
from functools import reduce
from pathlib import Path
from datetime import datetime

current_time = datetime.now()
current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')

downloads_path = str(Path.home() / "Downloads")
saveTo = downloads_path + "\Common rows " + current_time + ".xlsx"

print(saveTo)

dataframelist = []

left = pd.read_excel("D:\Photos & VIdeos\Family Photos\DataForPandas.xlsx")
end = pd.read_excel("D:\Photos & VIdeos\Family Photos\Book3.xlsx")
right = pd.read_excel("D:\Photos & VIdeos\Family Photos\Zanotexcel.xlsx")

dataframelist.append(left)
dataframelist.append(end)
dataframelist.append(right)
str = 'Name'

df_final = reduce(lambda left, right: pd.merge(left, right, suffixes=('_x', '_y'), on=str, how="inner"), dataframelist)

df_final.to_excel(saveTo, index=False)
