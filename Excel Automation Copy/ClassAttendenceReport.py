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
        self.dialogue_box_limit = simpledialog.askfloat("Minimum Attendence",
                                                        "Enter the minimum attendence required",
                                                        parent=self.master)
        if self.dialogue_box_limit is not None:
            for file in self.all_files_list:
                attendence_dataframe = pd.read_excel(file)


                attendence_dataframe["Average"] = attendence_dataframe.mean(axis=1)  # used to calculate avg of row

                current_time = datetime.now()
                current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
                downloads_path = str(Path.home() / "Downloads")
                saveTo = downloads_path + "\Attendence " + str(i) + " " + current_time + ".xlsx"
                attendence_dataframe.to_excel(saveTo, index=True)
                i += 1
                self.status_label.config(text="Attendence report generated in downloads")


