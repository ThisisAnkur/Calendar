import calendar
from tkinter import *


def show_to_calender():
    gui = Tk()
    gui.config(background='black')
    gui.title('Calender of the Year')
    gui.geometry('550x600')
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calendar_Year = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calendar_Year.grid(row =6, column =1, padx =20)
    gui.mainloop()

if __name__ == "__main__":
    new_gui = Tk()
    new_gui.config(background='black')
    new_gui.title('calendar')
    new_gui.geometry('250x250')
    cal = Label(new_gui, text="Calender",bg='grey',font=("times", 28, "bold"))
    year = Label(new_gui, text="Enter year", bg='dark grey')
    year_field = Entry(new_gui)
    button = Button(new_gui, text='Show Calender',fg='Grey',bg='Blue',command=show_to_calender)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    
    # Exit.grid(row=6, column=1)
    new_gui.mainloop()