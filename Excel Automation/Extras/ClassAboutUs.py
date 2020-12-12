import tkinter as tk
from tkinter import font
import webbrowser


class ClassAboutUs:
    def __init__(self, top):
        self.top = top
        self.top.title("About us")
        self.top.configure(bg="#ffffff")
        self.top.geometry("790x600")
        self.top.resizable(width=False, height=False)

        title_font = font.Font(family='Reem Kufi', size=40, weight='bold')
        text_font = font.Font(family="Rubik", size=11, weight="normal")
        developedby = font.Font(family="Garamond", size=13, weight='bold')

        developers = font.Font(family="Garamond", size=15, weight='bold')

        label = tk.Label(top, font=title_font, text="Excel Automation", fg="#00194C", bg="#ffffff")
        label.place(relx=0.22, rely=0.1)

        label = tk.Label(top, font=text_font,text="E  x  c  e  l     f  i  l  e     h  a  n  d  l  i  n  g     s  i  m  p  l  i  f  i  e  d", fg='#014067', bg='#ffffff')
        label.place(relx=0.22, rely=0.25)

        label = tk.Label(top, font=developedby, text="Developed by", fg='#000000', bg='#ffffff')
        label.place(relx=0.425, rely=0.5)

        label = tk.Label(top, font=developers, text="Rohit B. Deore", fg='#00194C', bg='#ffffff')
        label.place(relx=0.15, rely=0.6)

        github_photo = tk.PhotoImage(file="./Image Resources/github.png")
        rohit_github = tk.Label(top, image=github_photo, bg="#ffffff")
        rohit_github.image = github_photo
        rohit_github.place(relx=0.17, rely=0.649)
        rohit_github.bind("<Button-1>", lambda e: self.callback("https://github.com/deorerohit"))

        linkedin_photo = tk.PhotoImage(file="./Image Resources/linkedin.png")
        rohit_linkedin = tk.Label(top, image=linkedin_photo, bg="#ffffff")
        rohit_linkedin.image = linkedin_photo
        rohit_linkedin.place(relx=0.22, rely=0.653)
        rohit_linkedin.bind("<Button-1>", lambda e: self.callback("https://www.linkedin.com/in/rohit-deore-2b6a33193"))

        label = tk.Label(top, font=developers, text="Dhairyashil Potbhare", fg='#00194C', bg='#ffffff')
        label.place(relx=0.38, rely=0.6)

        github_photo = tk.PhotoImage(file="./Image Resources/github.png")
        rohit_github = tk.Label(top, image=github_photo, bg="#ffffff")
        rohit_github.image = github_photo
        rohit_github.place(relx=0.445, rely=0.649)
        rohit_github.bind("<Button-1>", lambda e: self.callback("https://github.com/deorerohit"))

        linkedin_photo = tk.PhotoImage(file="./Image Resources/linkedin.png")
        rohit_linkedin = tk.Label(top, image=linkedin_photo, bg="#ffffff")
        rohit_linkedin.image = linkedin_photo
        rohit_linkedin.place(relx=0.495, rely=0.653)
        rohit_linkedin.bind("<Button-1>", lambda e: self.callback("https://www.linkedin.com/in/rohit-deore-2b6a33193"))

        label = tk.Label(top, font=developers, text="Tejas Nagargoje", fg='#00194C', bg='#ffffff')
        label.place(relx=0.67, rely=0.6)

        github_photo = tk.PhotoImage(file="./Image Resources/github.png")
        rohit_github = tk.Label(top, image=github_photo, bg="#ffffff")
        rohit_github.image = github_photo
        rohit_github.place(relx=0.715, rely=0.649)
        rohit_github.bind("<Button-1>", lambda e: self.callback("https://github.com/deorerohit"))

        linkedin_photo = tk.PhotoImage(file="./Image Resources/linkedin.png")
        rohit_linkedin = tk.Label(top, image=linkedin_photo, bg="#ffffff")
        rohit_linkedin.image = linkedin_photo
        rohit_linkedin.place(relx=0.765, rely=0.653)
        rohit_linkedin.bind("<Button-1>", lambda e: self.callback("https://www.linkedin.com/in/rohit-deore-2b6a33193"))




        copyR = tk.Label(top, text="© 2020 Excel Automation", bg="#ffffff", justify="center")
        copyR.pack(side='bottom', fill="x")


    def callback(self, url):
        webbrowser.open_new(url)