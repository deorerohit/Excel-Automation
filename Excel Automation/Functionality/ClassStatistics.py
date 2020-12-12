import pandas as pd
from pathlib import Path
from datetime import datetime
import numpy as np


class ClassStatistics:
    def __init__(self, all_files_list, status_label):
        self.all_files_list = all_files_list
        self.downloads_directory = str(Path.home() / "Downloads")
        self.status_label = status_label

    def generate_statistics(self):
        i = 1
        for file in self.all_files_list:
            current_dataframe = pd.read_excel(file)
            dataframetocheck = current_dataframe.select_dtypes(include=np.number)
            if dataframetocheck.empty:
                msg = file + " does't contain any numeric column\nStatistics of other file may have generated"
                self.status_label.config(text=msg)
                i += 1
            else:
                dataframe_towrite = pd.DataFrame()
                dataframe_towrite = dataframe_towrite.append(current_dataframe)
                current_dataframe = current_dataframe.select_dtypes(include=np.number)
                stats_dataframe = current_dataframe.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
                dataframe_towrite = dataframe_towrite.append(stats_dataframe)
                current_time = datetime.now()
                current_time = current_time.strftime('%d-%m-%Y at %H.%M.%S')
                save_to = self.downloads_directory + "\Stats of " + str(i) + " " + current_time + ".xlsx"
                dataframe_towrite.to_excel(save_to, index=True)
                self.status_label.config(text="File(s) containing statistics generated")
                i += 1
