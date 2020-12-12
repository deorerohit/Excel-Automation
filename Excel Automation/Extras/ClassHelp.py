import tkinter as tk
from tkinter import font


class ClassHelp:
    def __init__(self, top):
        self.top = top
        self.top.title("Want Help?")
        self.top.configure(bg="#ffffff")
        self.top.geometry("790x600")
        self.top.resizable(width=False, height=False)
        title_font = font.Font(family='Rubik', size=12, weight='bold')
        text_font = font.Font(family="Rubik", size=10, weight="normal")

        combine_all_frame = tk.Frame(self.top, bg="#ede2ef", padx=8, pady=8)
        combine_all_frame.pack(padx=20, pady=10, fill="x")
        label1 = tk.Label(combine_all_frame, font=title_font, text="Combine All", fg="#000000", bg="#ede2ef", anchor='w')
        label1.pack(fill='x')
        label2 = tk.Label(combine_all_frame, font=text_font, text="If you select this opttion it will combine all the selected files into one file and the output file will be saved in downloads", fg="#000000",  bg="#ede2ef", anchor='w')
        label2.pack(fill='x')


        common_column = tk.Frame(self.top, bg="#ede2ef", padx=8, pady=8)
        common_column.pack(padx=20, pady=10, fill="x")
        label1 = tk.Label(common_column, font=title_font, text="Get common columns", fg="#000000", bg="#ede2ef",  anchor='w')
        label1.pack(fill='x')
        label2 = tk.Label(common_column, font=text_font, text="This functionality helps you to get the common columns from all the selected files. All the columns will be added \nto a single file which will be saved in downloads",fg="#000000", bg="#ede2ef", anchor='w', justify=tk.LEFT)
        label2.pack(fill='x')

        common_rows = tk.Frame(self.top, bg="#ede2ef", padx=8, pady=8)
        common_rows.pack(padx=20, pady=10, fill="x")
        label1 = tk.Label(common_rows, font=title_font, text="Get common rows", fg="#000000", bg="#ede2ef",  anchor='w')
        label1.pack(fill='x')
        label2 = tk.Label(common_rows, font=text_font, text="First of all you need to enter the column name in which you want to look for common rows, then it will give you a \nsingle file containing the common entries from that column with all other column", fg="#000000", bg="#ede2ef", anchor='w',  justify=tk.LEFT)
        label2.pack(fill='x')

        generate_graph = tk.Frame(self.top, bg="#ede2ef", padx=8, pady=8)
        generate_graph.pack(padx=20, pady=10, fill="x")
        label1 = tk.Label(generate_graph, font=title_font, text="Generate graph", fg="#000000", bg="#ede2ef", anchor='w')
        label1.pack(fill='x')
        label2 = tk.Label(generate_graph, font=text_font, text="Select a file then select the columns to plot on x axis and y axis respectively and then click 'OK', it will show you a graph \nwith proper coordinates",  fg="#000000", bg="#ede2ef", anchor='w', justify=tk.LEFT)
        label2.pack(fill='x')

        statistics = tk.Frame(self.top, bg="#ede2ef", padx=8, pady=8)
        statistics.pack(padx=20, pady=10, fill="x")
        label1 = tk.Label(statistics, font=title_font, text="Statistics", fg="#000000", bg="#ede2ef", anchor='w')
        label1.pack(fill='x')
        label2 = tk.Label(statistics, font=text_font, text="Selecting this option will generate a file containing maximum, minimum, average, etc from each numeric column",  fg="#000000", bg="#ede2ef", anchor='w', justify=tk.LEFT)
        label2.pack(fill='x')

        attendence = tk.Frame(self.top, bg="#ede2ef", padx=8, pady=8)
        attendence.pack(padx=20, pady=10, fill="x")
        label1 = tk.Label(attendence, font=title_font, text="Attendence report", fg="#000000", bg="#ede2ef", anchor='w')
        label1.pack(fill='x')
        label2 = tk.Label(attendence, font=text_font, text="It will generate a file containing the average attendence of each student and also the number of subjects in which \nhis/her attendence is below minimum required attendence also the one who doesn't meet the criteria will be marked red",  fg="#000000", bg="#ede2ef", anchor='w', justify=tk.LEFT)
        label2.pack(fill='x')


