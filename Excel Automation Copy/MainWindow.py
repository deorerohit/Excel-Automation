from tkinter import filedialog
import tkinter as tk
import tkinter.font as font

from ClassAttendenceReport import ClassAttendenceReport
from ClassCombineFiles import ClassCombineFiles
from ClassCommonColumns import ClassCommonColumns
from ClassCommonRows import ClassCommonRows
from ClassGenerateGraph import ClassGenerateGraph


class MainWindow:

    all_files_list = []

    def __init__(self, master):
        myFont = font.Font(family='Poppins', size=9, weight='bold')

        self.frame = tk.Frame(master, bg="#ede2ef")
        self.frame.place(relx='0.02', rely='0.05', relwidth='0.96', relheight='0.46')
        main_frame = tk.LabelFrame(self.frame, relief='sunken')
        main_frame.place(relwidth='0.98', relheight='0.78', relx='0.01', rely='0.035')
        self.mycanvas = tk.Canvas(main_frame)
        self.mycanvas.pack(side=tk.LEFT)

        yscrollbar = tk.Scrollbar(main_frame, orient='vertical', command=self.mycanvas.yview)
        yscrollbar.pack(side=tk.RIGHT, fill='y')
        self.mycanvas.configure(yscrollcommand=yscrollbar.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))
        self.inside_frame = tk.Frame(self.mycanvas)
        self.mycanvas.create_window((0, 0), window=self.inside_frame, anchor='nw')

        # This window will show the current status
        status_window = tk.LabelFrame(master, text="   Status   ", bg="#ffffff", padx=10)
        status_window.place(relx='0.02', rely='0.74', relheight='0.15', relwidth='0.96')
        status_mainframe = tk.Frame(status_window, relief='sunken')
        status_mainframe.place(rely='0.09', relheight='0.8', relwidth='0.998')
        self.status_label = tk.Label(status_mainframe, text='Welcome!!  Add files to continue', padx=10, pady=5,anchor='w')
        self.status_label.pack(fill='both')

        operation_window = tk.LabelFrame(master, text="  Operations  ", bg="#ffffff", padx=10)
        operation_window.place(relx='0.02', rely='0.53', relheight='0.17', relwidth='0.96')

        self.clicked = tk.StringVar(master)
        self.clicked.set("Choose Option")

        self.cmn_all_rb = tk.Radiobutton(operation_window, font=myFont, text='Combine All', variable=self.clicked, value="Combine All Files", bg="#ffffff")
        self.cmn_all_rb.place(relx='0.02', rely='0.02')
        self.cmn_col_rb = tk.Radiobutton(operation_window, font=myFont, text='Get Common Columns', variable=self.clicked, value="Get common columns", bg="#ffffff")
        self.cmn_col_rb.place(relx='0.4', rely='0.02')
        self.cmn_row_rb = tk.Radiobutton(operation_window, font=myFont, text='Get Common Rows', variable=self.clicked, value="Get common rows", bg="#ffffff")
        self.cmn_row_rb.place(relx='0.8', rely='0.02')

        self.cmn_graph_rb = tk.Radiobutton(operation_window, font=myFont, text='Generate Graph', variable=self.clicked, value="Generate Graph", bg="#ffffff")
        self.cmn_graph_rb.place(relx='0.02', rely='0.43')
        self.cmn_stats_rb = tk.Radiobutton(operation_window, font=myFont, text="Statistics", variable=self.clicked, value="Statistics", bg="#ffffff")
        self.cmn_stats_rb.place(relx='0.4', rely='0.43')
        self.attend_repo = tk.Radiobutton(operation_window, font=myFont, text="Attendence Report", variable=self.clicked, value="Attendence Report", bg="#ffffff")
        self.attend_repo.place(relx='0.8', rely='0.43')

        # Button to add the excel file
        self.addExcelFile = tk.Button(self.frame, font=myFont, text="Add File", padx=10, pady=5, fg="white",bg="#1F1B24", command=self.add_excel_files)
        self.addExcelFile.place(relx='0.75', rely='0.84')

        # Button to remove selected file
        self.removeFile = tk.Button(self.frame, font=myFont, text="Remove File", padx=10, pady=5, fg="white",bg='#FF0000', command=self.remove_file)
        self.removeFile.place(relx='0.86', rely='0.84')

        # Button to start the selected process
        self.startProcess = tk.Button(master, font=myFont, text="Start Process", padx=20, pady=5, fg='white', bg="#1F1B24", command=self.get_proper_function_name)
        self.startProcess.place(relx=0.818, rely=0.923)


    def remove_file(self):
        self.all_files_list.pop()
        label_list = self.inside_frame.winfo_children()
        label_to_remove = label_list.pop()
        label_to_remove.destroy()

    # Function to select the excel files
    def add_excel_files(self):
        myfont = font.Font(family='Poppins', size=9, weight='bold')
        if len(self.all_files_list) != 0:
            self.status_label.config(text="Now you can select the operation to perform", font=myfont)

        filename = filedialog.askopenfilename(initialdir="D/", title="Select File",
                                              filetypes=(("Excel file", "*.xlsx"), ("All files", "*.*")))

        if len(filename) != 0:
            self.all_files_list.append(filename)
            label = tk.Label(self.inside_frame, font=myfont, text=self.all_files_list[-1], anchor='w')
            label.pack(fill='both')
        self.mycanvas.config(scrollregion=self.mycanvas.bbox('all'))

    def get_proper_function_name(self):
        if self.clicked.get() == "Combine All Files":
            combine_file = ClassCombineFiles(self.all_files_list, self.status_label)
            combine_file.combine_excel_files()
        elif self.clicked.get() == "Get common columns":
            common_column = ClassCommonColumns(self.all_files_list, self.status_label)
            common_column.get_common_columns()
        elif self.clicked.get() == "Get common rows":
            common_rows = ClassCommonRows(self.all_files_list, self.status_label, self.frame)
            common_rows.get_common_rows()
        elif self.clicked.get() == "Generate Graph":
            graph = ClassGenerateGraph(self.all_files_list, self.status_label, self.frame)
            graph.generate_graph()
        elif self.clicked.get() == "Statistics":
            pass
            # Function for statistics
        elif self.clicked.get() == "Attendence Report":
            attend_report = ClassAttendenceReport(self.all_files_list, self.status_label, self.frame)
            attend_report.attendence_report()


root = tk.Tk()
root.title("Excel Automation Software")
root.geometry("850x650")
root.configure(bg='#ffffff')
root.resizable(width=False, height=False)

obj1 = MainWindow(root)

root.mainloop()