import tkinter as tk
from tkinter import *
import pandas as pd
from tkinter import filedialog, Text, CENTER
import os

root = tk.Tk()
root.title("Excel Automation Software")
root.geometry("800x600")
root.configure(bg='#1F1B24')
root.resizable(width=False, height=False)

# Variables for combine
all_files_list = []
files_dataframe_list = []

# Variables for common columns
lst = list()
filesD = []


# Function to call the proper function out of selected from drop down menu
def get_proper_function_name():
    print(clicked.get())
    if clicked.get() == "Combine All Files":
        combine_excel_files()
    elif clicked.get() == "Get common columns":
        get_common_columns()




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
    dp.to_excel('D:\Common Columns.xlsx', index=False)




# Function to combine all the exce files
def combine_excel_files():
    for file in all_files_list:
        current_dataframe = pd.read_excel(file)
        files_dataframe_list.append(current_dataframe)

    output_dataframe = pd.concat(files_dataframe_list, axis=0)
    output_dataframe.to_excel('D:\Combine All.xlsx', index=True)




# Function to select the excel files
def add_excel_files():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Excel file", "*.xlsx"), ("All files", "*.*")))
    all_files_list.append(filename)
    print(filename)
    label = tk.Label(frame, text=all_files_list[-1], anchor='w')
    label.pack(fill='both')



# canvas = tk.Canvas(root, height=600, width=800, bg="#1F1B24")
# canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.98, relheight=0.4, relx=0.01, rely=0.1)

# This is for the drop down menu
clicked = tk.StringVar(root)
clicked.set("Choose Options")
options = [
    "Combine All Files",
    "Get common columns",
    "Get common rows",
    "Generate Graph"
]
dropDownMenu = tk.OptionMenu(root, clicked, *options)
dropDownMenu.place(width=200, x=9, y=315)



# Button to start the selected process
startProcess = tk.Button(root, text="Start Process", padx=10, pady=5, fg="#1F1B24", command=get_proper_function_name)
startProcess.place(x=650, y=550)



addExcelFile = tk.Button(frame, text="Add File", padx=10, pady=5, fg="white", bg="#1F1B24", command=add_excel_files)
addExcelFile.place(x=580, y=200)

removeFile = tk.Button(frame, text="Remove File", padx=10, pady=5, fg="white", bg='#FF0000')
removeFile.place(x=680, y=200)

root.mainloop()
