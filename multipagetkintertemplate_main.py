import tkinter as tk
from tkinter import ttk

LARGE_FONT = ('Calibri', 35, 'bold underline')
BACKGROUND = '#222222'
MIDGROUND = '#434242'
FOREGROUND = '#F3EFE0'
ACCENT = '#22A39F'
BUTTONS = ''


class MultiPageTemplate(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing pages to an empty dictionary
        self.frames = {}

        # iterating through pages
        for F in (StartPage, Page2, Page3, Page4):
            frame = F(container, self)

            # initializing frame of that object from
            # StartPage, Page2, Page3 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.display_page(StartPage)

    def display_page(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame StartPage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BACKGROUND)
        # Initialize style
        s = ttk.Style()

        # configure label styles
        s.configure('label.TLabel', background=BACKGROUND, foreground='white')

        label = ttk.Label(self, text="Start Page", font=LARGE_FONT, style='label.TLabel')
        label.grid(row=0, column=2, columnspan=4, padx=10, pady=10)

        # creating buttons for page navigation and using lambda command to display page matched to button text
        button1 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.display_page(Page2))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 3",
                             command=lambda: controller.display_page(Page3))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Page 4",
                             command=lambda: controller.display_page(Page4))

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BACKGROUND)
        # Initialize style
        s = ttk.Style()

        # configure label styles
        s.configure('label.TLabel', background=BACKGROUND, foreground='white')

        label = ttk.Label(self, text="Page 2", font=LARGE_FONT, style='label.TLabel')
        label.grid(row=0, column=2, columnspan=4, padx=10, pady=10)

        # creating buttons for page navigation and using lambda command to display page matched to button text
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.display_page(StartPage))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 3",
                             command=lambda: controller.display_page(Page3))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Page 4",
                             command=lambda: controller.display_page(Page4))

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BACKGROUND)
        # Initialize style
        s = ttk.Style()

        # configure label styles
        s.configure('label.TLabel', background=BACKGROUND, foreground='white')

        label = ttk.Label(self, text="Page 3", font=LARGE_FONT, style='label.TLabel')
        label.grid(row=0, column=2, columnspan=4, padx=10, pady=10)

        # creating buttons for page navigation and using lambda command to display page matched to button text
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.display_page(StartPage))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.display_page(Page2))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Page 4",
                             command=lambda: controller.display_page(Page4))

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BACKGROUND)

        # Initialize style
        s = ttk.Style()

        # configure style for each frame
        s.configure('Frame1.TFrame', background='skyblue')
        s.configure('Frame2.TFrame', background='green')
        s.configure('Frame3.TFrame', background='blue')
        s.configure('Frame4.TFrame', background=ACCENT)

        # configure label styles
        s.configure('label.TLabel', background=BACKGROUND, foreground='white')

        label = ttk.Label(self, text="Page Four", font=LARGE_FONT, style='label.TLabel')
        label.grid(row=0, column=2, columnspan=4, padx=10, pady=10)

        # creating buttons for page navigation and using lambda command to display page matched to button text
        button1 = ttk.Button(self, text="StartPage", style=BUTTONS,
                             command=lambda: controller.display_page(StartPage))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.display_page(Page2))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Page 3",
                             command=lambda: controller.display_page(Page3))

        button3.grid(row=3, column=1, padx=10, pady=10)

        # creating a notebook within right side frame with multiple tabs styled separately
        mainframe = ttk.Notebook(self, width=50, height=200, style='Frame1.TFrame')
        mainframe.grid(row=1, column=2, columnspan=4, rowspan=5, sticky='nsew', padx=10, pady=10)

        tab1 = ttk.Frame(mainframe, style='Frame1.TFrame')
        mainframe.add(tab1, text="Tab1",)
        tab1_contents = ttk.Frame(tab1, width=300, height=190, style='Frame1.TFrame')
        tab1_contents.grid(row=0, column=0, pady=5, padx=5)

        tab2 = ttk.Frame(mainframe, style='Frame2.TFrame')
        mainframe.add(tab2, text="Tab2")

        tab3 = ttk.Frame(mainframe, style='Frame3.TFrame')
        mainframe.add(tab3, text="Tab3")

        tab4 = ttk.Frame(mainframe, style='Frame4.TFrame')
        mainframe.add(tab4, text="Tab4")


app = MultiPageTemplate()
app.mainloop()

# I Created this to streamline creation of multi-page applications,
# this has helped me greatly in my personal development especially with developing my undestanding of
# creating and manipulating tkinter objects, this has also aided in creating videogames
# with multiple screens such as start screens, game screens, high score pages etc.
# this code can be easily expanded to have more pages and can be used in conjunction with various other modules
# My personal favourite being the Turtle module for videogames
