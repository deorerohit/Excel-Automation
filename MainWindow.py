import tkinter as tk
import pandas as pd
from tkinter import filedialog, Text, CENTER
import os

root = tk.Tk()
root.title("Excel Automation Software")
root.geometry("800x600")
root.resizable(width=False, height=False)

all_files_list = []
files_dataframe_list = []


def add_excel_files():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Excel file", "*.xlsx"), ("All files", "*.*")))
    all_files_list.append(filename)
    print(filename)
    label = tk.Label(frame, text=all_files_list[-1])
    label.pack()


def combine_excel_files():
    for file in all_files_list:
        current_dataframe = pd.read_excel(file)
        files_dataframe_list.append(current_dataframe)

    output_dataframe = pd.concat(files_dataframe_list, axis=0)
    output_dataframe.to_excel('D:\Data.xlsx', index=True)


canvas = tk.Canvas(root, height=600, width=800, bg="#1F1B24")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.98, relheight=0.4, relx=0.01, rely=0.1)


combineFiles = tk.Button(frame, text="Combine Files", padx=10, pady=5, fg="#1F1B24", command=combine_excel_files)
combineFiles.pack(side="bottom")


addExcelFile = tk.Button(frame, text="Add File", padx=10, pady=5, fg="#1F1B24", command=add_excel_files)
addExcelFile.pack(side="bottom")

root.mainloop()

print(all_files_list)
