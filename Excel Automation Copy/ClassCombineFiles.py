import pandas as pd
from pathlib import Path
from datetime import datetime


class ClassCombineFiles:

    def __init__(self, all_files_list, status_label):
        self.downloads_directory = str(Path.home() / "Downloads")
        self.all_files_list = all_files_list
        self.status_label = status_label

    # Function to combine all the exce files
    def combine_excel_files(self):
        files_dataframe_list = []
        for file in self.all_files_list:
            current_dataframe = pd.read_excel(file)
            files_dataframe_list.append(current_dataframe)

        output_dataframe = pd.concat(files_dataframe_list, axis=0)

        current_time = datetime.now()
        current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
        save_to = self.downloads_directory + "\Combine All " + current_time + ".xlsx"
        output_dataframe.to_excel(save_to, index=True)
        self.status_label.config(text="Successful!! file is saved in downloads")


