import pandas as pd
from pathlib import Path
import numpy as np
from datetime import datetime

df = pd.read_excel("D:\Photos & VIdeos\Family Photos\TE A&B Attendence Report.xlsx")

numeric_dataframe = df.select_dtypes(include=np.number)

# print(df)
# print(numeric_dataframe)

df['Average'] = df.mean(axis=1)
df.loc['mean'] = df.mean()


numeric_dataframe = numeric_dataframe[numeric_dataframe < 75].count(axis='columns')
df['Below 75 '] = numeric_dataframe
print(df)







def change_colour(val):
    return ['background-color: #FA5B5B' if x < 75 else 'background-color: #ffffff' for x in val]


df = df.style.apply(change_colour, axis=1, subset=['Average'])
current_time = datetime.now()
current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
downloads_path = str(Path.home() / "Downloads")
saveTo = downloads_path + "\Attendence temp " + current_time + ".xlsx"
df.to_excel(saveTo, index=True)
