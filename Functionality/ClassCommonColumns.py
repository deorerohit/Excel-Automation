import pandas as pd
from pathlib import Path
from datetime import datetime


class ClassCommonColumns:


    def __init__(self, all_files_list, status_label):
        self.lst = list()
        self.filesD = []
        self.all_files_list = all_files_list
        self.downloads_directory = str(Path.home() / "Downloads")
        self.status_label = status_label

    # Function to get the common columns
    def get_common_columns(self):
        for file in self.all_files_list:
            k = pd.read_excel(file)
            self.filesD.append(k)
            self.lst.append(k.columns.ravel())
        com = list(set.intersection(*map(set, self.lst)))

        p = []
        # Reading common column from each .xlsx file
        for i in self.filesD:
            for j in com:
                df = pd.DataFrame(i[str(j)])
                p.append(df)

        dp = pd.concat(p, axis=1)
        current_time = datetime.now()
        current_time = current_time.strftime('%d-%m-%Y at %H.%M.%S')
        save_to = self.downloads_directory + "\Common columns " + current_time + ".xlsx"
        dp.to_excel(save_to, index=True)
        self.status_label.config(text="File containing common columns generated in Downloads")
