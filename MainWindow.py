import tkinter as tk
import tkinter.font as font
import pandas as pd
from functools import reduce
from pathlib import Path
from datetime import datetime
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog, Text, CENTER
import os

root = tk.Tk()
root.title("Excel Automation Software")
root.geometry("800x600")
root.configure(bg='#ffffff')
root.resizable(width=False, height=False)

myFont = font.Font(family='Poppins', size=9, weight='bold')

# Variables for combine
all_files_list = []
files_dataframe_list = []

# Variables for common columns
lst = list()
filesD = []

# Variables for common rows
cmn_rows_dataframe_list = []

# Downloads directory
downloads_directory = str(Path.home() / "Downloads")


# Function to call the proper function out of selected from drop down menu
def get_proper_function_name():
    if clicked.get() == "Combine All Files":
        combine_excel_files()
    elif clicked.get() == "Get common columns":
        get_common_columns()
    elif clicked.get() == "Get common rows":
        get_common_rows()
    elif clicked.get() == "Generate Graph":
        generate_graph()
    elif clicked.get() == "Statistics":
        generate_statistics()
    elif clicked.get() == "Attendence Report":
        attendence_report()


def change_color(val, not_used, dialogue_box_limit):
    for x in val:
        if x < dialogue_box_limit:
            return ['background-color: #FA5B5B']
        else:
            return ['background-color: transparent']


#    value = ['background-color: #FA5B5B' if x < 75 else 'background-color: #ffffff' for x in val]
#    print(value)
#    return value


def attendence_report():
    i = 1
    dialogue_box_limit = simpledialog.askfloat("Minimum Attendence",
                                               "Enter the minimum attendence required",
                                               parent=root)
    if dialogue_box_limit is not None:
        for file in all_files_list:
            attendence_dataframe = pd.read_excel(file)
            attendence_dataframe["Average"] = attendence_dataframe.mean(axis=1)  # used to calculate avg of row
            attendence_dataframe.loc["Overall"] = attendence_dataframe.mean()  # used to calculate avg of column
            attendence_dataframe = attendence_dataframe.style.apply(change_color, args=(2, dialogue_box_limit), axis=1,
                                                                    subset=[
                                                                        'Average'])  # used to format the background color
            current_time = datetime.now()
            current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
            downloads_path = str(Path.home() / "Downloads")
            saveTo = downloads_path + "\Attendence " + str(i) + " " + current_time + ".xlsx"
            attendence_dataframe.to_excel(saveTo, index=True)
            i += 1
            status_label.config(text="Attendence report generated in downloads")


def generate_statistics():
    i = 1
    for file in all_files_list:
        current_dataframe = pd.read_excel(file)
        dataframetocheck = current_dataframe.select_dtypes(include=np.number)
        if dataframetocheck.empty:
            msg = file + " does't contain any numeric column"
            status_label.config(text=msg)
            i += 1
        else:
            dataframe_towrite = pd.DataFrame()
            dataframe_towrite = dataframe_towrite.append(current_dataframe)
            current_dataframe = current_dataframe.select_dtypes(include=np.number)
            stats_dataframe = current_dataframe.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))
            dataframe_towrite = dataframe_towrite.append(stats_dataframe)
            current_time = datetime.now()
            current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
            save_to = downloads_directory + "\Stats of " + str(i) + " " + current_time + ".xlsx"
            dataframe_towrite.to_excel(save_to, index=True)
            i += 1


def generate_graph():
    if len(all_files_list) != 0:
        graph_dataframe = pd.read_excel(all_files_list[0])
        dialogue_box_x_axis = simpledialog.askstring("X axis", "Column to plot on x axis", parent=root)
        dialogue_box_y_axis = simpledialog.askstring("Y axis", "Column to plot on y axis", parent=root)
        values = graph_dataframe[[dialogue_box_x_axis, dialogue_box_y_axis]]
        axes = values.plot.bar(x=dialogue_box_x_axis, y=dialogue_box_y_axis, rot=0)
        plt.show()
    else:
        status_label.config(text="First of all select the files.")


def get_common_rows():
    dialogue_box_ans = simpledialog.askstring("Column name",
                                              "Enter the column name from which you want common rows.\n"
                                              "Note : It must be present in all the selected files!!",
                                              parent=root)
    if dialogue_box_ans is not None:
        for file in all_files_list:
            file_dataframe = pd.read_excel(file)
            cmn_rows_dataframe_list.append(file_dataframe)

        com_rows_final_dataframe = reduce(lambda left, right: pd.merge(left, right, on=dialogue_box_ans, how='inner'),
                                          cmn_rows_dataframe_list)
        current_time = datetime.now()
        current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
        save_to = downloads_directory + "\Common rows " + current_time + ".xlsx"
        com_rows_final_dataframe.to_excel(save_to, index=True)
    else:
        print("You don't have a first name?")


# Function to get the common columns
def get_common_columns():
    for file in all_files_list:
        k = pd.read_excel(file)
        filesD.append(k)
        lst.append(k.columns.ravel())
    com = list(set.intersection(*map(set, lst)))

    p = []
    # Reading common column from each .xlsx file
    for i in filesD:
        for j in com:
            df = pd.DataFrame(i[str(j)])
            p.append(df)

    dp = pd.concat(p, axis=1)
    current_time = datetime.now()
    current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
    save_to = downloads_directory + "\Common columns " + current_time + ".xlsx"
    dp.to_excel(save_to, index=True)


# Function to combine all the exce files
def combine_excel_files():
    for file in all_files_list:
        current_dataframe = pd.read_excel(file)
        files_dataframe_list.append(current_dataframe)

    output_dataframe = pd.concat(files_dataframe_list, axis=1)
    current_time = datetime.now()
    current_time = current_time.strftime('%d-%m-%Y %H~%M~%S')
    save_to = downloads_directory + "\Combine All " + current_time + ".xlsx"
    output_dataframe.to_excel(save_to, index=True)
    status_label.config(text="Successful!! file is saved in downloads")


def remove_file():
    all_files_list.pop()
    label_list = inside_frame.winfo_children()
    label_to_remove = label_list.pop()
    label_to_remove.destroy()


# Function to select the excel files
def add_excel_files():
    if len(all_files_list) != 0:
        status_label.config(text="Now you can select the operation to perform")

    filename = filedialog.askopenfilename(initialdir="D/", title="Select File",
                                          filetypes=(("Excel file", "*.xlsx"), ("All files", "*.*")))

    if len(filename) != 0:
        all_files_list.append(filename)
        label = tk.Label(inside_frame, font=myFont, text=all_files_list[-1], anchor='w')
        label.pack(fill='both')
    mycanvas.config(scrollregion=mycanvas.bbox('all'))


frame = tk.Frame(root, bg="#ede2ef", )
frame.place(relx='0.02', rely='0.05', relwidth='0.96', relheight='0.46')

mainFrame = tk.LabelFrame(frame, relief='sunken')
mainFrame.place(relwidth='0.98', relheight='0.78', relx='0.01', rely='0.035')

mycanvas = tk.Canvas(mainFrame)
mycanvas.pack(side=tk.LEFT)

yscrollbar = tk.Scrollbar(mainFrame, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=tk.RIGHT, fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

inside_frame = tk.Frame(mycanvas)
mycanvas.create_window((0, 0), window=inside_frame, anchor='nw')

# This is for the drop down menu
clicked = tk.StringVar(root)
clicked.set("Choose Option")
# options = [
#    "Combine All Files",
#    "Get common columns",
#    "Get common rows",
#    "Generate Graph",
#    "Statistics"
# ]
# dropDownMenu = tk.OptionMenu(root, clicked, *options)
# dropDownMenu.place(width=170, relx='0.02', rely='0.54')

operation_window = tk.LabelFrame(root, text="  Operations  ", bg="#ffffff", padx=10)
operation_window.place(relx='0.02', rely='0.53', relheight='0.17', relwidth='0.96')

cmn_all_rb = tk.Radiobutton(operation_window, font=myFont, text='Combine All', variable=clicked,
                            value="Combine All Files", bg="#ffffff")
cmn_all_rb.place(relx='0.02', rely='0.02')
cmn_col_rb = tk.Radiobutton(operation_window, font=myFont, text='Get Common Columns', variable=clicked,
                            value="Get common columns", bg="#ffffff")
cmn_col_rb.place(relx='0.4', rely='0.02')
cmn_row_rb = tk.Radiobutton(operation_window, font=myFont, text='Get Common Rows', variable=clicked,
                            value="Get common rows", bg="#ffffff")
cmn_row_rb.place(relx='0.8', rely='0.02')

cmn_graph_rb = tk.Radiobutton(operation_window, font=myFont, text='Generate Graph', variable=clicked,
                              value="Generate Graph", bg="#ffffff")
cmn_graph_rb.place(relx='0.02', rely='0.43')
cmn_stats_rb = tk.Radiobutton(operation_window, font=myFont, text="Statistics", variable=clicked, value="Statistics",
                              bg="#ffffff")
cmn_stats_rb.place(relx='0.4', rely='0.43')
attend_repo = tk.Radiobutton(operation_window, font=myFont, text="Attendence Report", variable=clicked,
                             value="Attendence Report", bg="#ffffff")
attend_repo.place(relx='0.8', rely='0.43')

# Button to start the selected process
startProcess = tk.Button(root, font=myFont, text="Start Process", padx=20, pady=5, fg='white', bg="#1F1B24",
                         command=get_proper_function_name)
startProcess.place(x=654, y=545)

addExcelFile = tk.Button(frame, font=myFont, text="Add File", padx=10, pady=5, fg="white", bg="#1F1B24",
                         command=add_excel_files)
addExcelFile.place(relx='0.75', rely='0.84')

removeFile = tk.Button(frame, font=myFont, text="Remove File", padx=10, pady=5, fg="white", bg='#FF0000',
                       command=remove_file)
removeFile.place(relx='0.86', rely='0.84')

status_window = tk.LabelFrame(root, text="   Status   ", bg="#ffffff", padx=10)
status_window.place(relx='0.02', rely='0.74', relheight='0.15', relwidth='0.96')

status_mainframe = tk.Frame(status_window, relief='sunken')
status_mainframe.place(rely='0.09', relheight='0.8', relwidth='0.998')

status_label = tk.Label(status_mainframe, text='Welcome!!  Add files to continue', padx=10, pady=5, font=myFont,
                        anchor='w')
status_label.pack(fill='both')

root.mainloop()
