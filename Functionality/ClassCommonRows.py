from tkinter import simpledialog
from functools import reduce
import pandas as pd
from pathlib import Path
from datetime import datetime


class ClassCommonRows:

    def __init__(self, all_files_list, status_label, master):
        self.all_files_list = all_files_list
        self.downloads_directory = str(Path.home() / "Downloads")
        self.status_label = status_label
        self.master = master
        self.cmn_rows_dataframe_list = []

    def get_common_rows(self):
        dialogue_box_ans = simpledialog.askstring("Column name",
                                                  "Enter the column name from which you want common rows.\n"
                                                  "Note : It must be present in all the selected files!!",
                                                  parent=self.master)
        print(self.cmn_rows_dataframe_list)
        if dialogue_box_ans is not None:
            for file in self.all_files_list:
                file_dataframe = pd.read_excel(file)
                # self.status_label.config(text="One of the file doesn't contained the column name you just entered.")
                self.cmn_rows_dataframe_list.append(file_dataframe)
            try:
                com_rows_final_dataframe = reduce(lambda left, right: pd.merge(left, right, on=dialogue_box_ans, how='inner'),self.cmn_rows_dataframe_list)
                current_time = datetime.now()
                current_time = current_time.strftime('%d-%m-%Y at %H.%M.%S')
                save_to = self.downloads_directory + "\Common rows " + current_time + ".xlsx"
                com_rows_final_dataframe.to_excel(save_to, index=True)
                self.status_label.config(text="File containing common rows generated in Downloads")

            except:
                 self.status_label.config(text="One of the file doesn't contained the column name you just entered.")

        else:
            self.status_label.config(text="Column name not entered")
