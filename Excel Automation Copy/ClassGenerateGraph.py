<<<<<<< HEAD
from tkinter import simpledialog
import matplotlib.pyplot as plt
import pandas as pd


class ClassGenerateGraph:

    def __init__(self, all_files_list, status_label, master):
        self.all_files_list = all_files_list
        self.status_label = status_label
        self.master = master

    def generate_graph(self):
        if len(self.all_files_list) != 0:
            graph_dataframe = pd.read_excel(self.all_files_list[0])
            dialogue_box_x_axis = simpledialog.askstring("X axis", "Column to plot on x axis", parent=self.master)
            dialogue_box_y_axis = simpledialog.askstring("Y axis", "Column to plot on y axis", parent=self.master)
            values = graph_dataframe[[dialogue_box_x_axis, dialogue_box_y_axis]]
            axes = values.plot.bar(x=dialogue_box_x_axis, y=dialogue_box_y_axis, rot=0)
            plt.show()
        else:
            self.status_label.config(text="First of all select the files.")


=======
from tkinter import simpledialog
import matplotlib.pyplot as plt
import pandas as pd


class ClassGenerateGraph:

    def __init__(self, all_files_list, status_label, master):
        self.all_files_list = all_files_list
        self.status_label = status_label
        self.master = master

    def generate_graph(self):
        if len(self.all_files_list) != 0:
            graph_dataframe = pd.read_excel(self.all_files_list[0])
            dialogue_box_x_axis = simpledialog.askstring("X axis", "Column to plot on x axis", parent=self.master)
            dialogue_box_y_axis = simpledialog.askstring("Y axis", "Column to plot on y axis", parent=self.master)
            values = graph_dataframe[[dialogue_box_x_axis, dialogue_box_y_axis]]
            axes = values.plot.bar(x=dialogue_box_x_axis, y=dialogue_box_y_axis, rot=0)
            plt.show()
        else:
            self.status_label.config(text="First of all select the files.")


>>>>>>> 6a6f942a636bbab53b473e6523bff585b87e2a29
