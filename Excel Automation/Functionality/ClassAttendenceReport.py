from tkinter import simpledialog
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime


class ClassAttendenceReport:

    def __init__(self, all_files_list, status_label, master):
        self.all_files_list = all_files_list
        self.downloads_directory = str(Path.home() / "Downloads")
        self.status_label = status_label
        self.master = master
        self.dialogue_box_limit = 0.0

    def attendence_report(self):
        i = 1
        self.dialogue_box_limit = simpledialog.askfloat("Minimum Attendance",
                                                        "Enter the minimum attendance required",
                                                        parent=self.master)
        if self.dialogue_box_limit is not None:
            for file in self.all_files_list:
                attendence_dataframe = pd.read_excel(file)
                numeric_dataframe = attendence_dataframe.select_dtypes(include=np.number)  # used to get the numeric columns

                attendence_dataframe["Average"] = attendence_dataframe.mean(axis=1)  # used to calculate avg of row
                attendence_dataframe.loc["Overall"] = attendence_dataframe.mean()  # used to calculate avg of column

                numeric_dataframe = numeric_dataframe[numeric_dataframe < self.dialogue_box_limit].count(axis='columns')
                attendence_dataframe['Below '+str(self.dialogue_box_limit)] = numeric_dataframe

                attendence_dataframe = attendence_dataframe.style.apply(self.change_color,
                                                                        axis=1,
                                                                        subset=['Average'])  # used to format the background color
                current_time = datetime.now()
                current_time = current_time.strftime('%d-%m-%Y at %H.%M.%S')
                downloads_path = str(Path.home() / "Downloads")
                saveTo = downloads_path + "\Attendance " + str(i) + " " + current_time + ".xlsx"
                attendence_dataframe.to_excel(saveTo, index=True)
                i += 1
                msg = "Attendance report generated in downloads, "+"Minimum attendance = " + str(self.dialogue_box_limit)
                self.status_label.config(text=msg)

    def change_color(self, val):
        for x in val:
            if x < self.dialogue_box_limit:
                return ['background-color: #FA5B5B']
            else:
                return ['background-color: transparent']
