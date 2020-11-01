import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

dataframelist = []

current_time = datetime.now()
current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')

downloads_path = str(Path.home() / "Downloads")
saveTo = downloads_path + "\Stats " + current_time + ".xlsx"

left = pd.read_excel("D:\Photos & VIdeos\Family Photos\DataForPandas.xlsx")
right = pd.read_excel("D:\Photos & VIdeos\Family Photos\Zanotexcel.xlsx")
end = pd.read_excel("D:\Photos & VIdeos\Family Photos\Book3.xlsx")

finaldf = pd.DataFrame()
finaldf = finaldf.append(left)
left = left.select_dtypes(include=np.number)
stats = left.describe()
finaldf = finaldf.append(stats)
# finaldf.to_excel(saveTo, index=True)
dataframelist.append(left)

right = right.select_dtypes(include=np.number)
dataframelist.append(right)

endfinal = pd.DataFrame()
endfinal = endfinal.append(end)
end = end.select_dtypes(include=np.number)
endstats = end.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
print(endstats)
endfinal = endfinal.append(endstats)
endfinal.to_excel(saveTo, index=True)

dataframelist.append(end)

# for data in dataframelist:
#    print(data)
#    print("\n******************************************\n")
