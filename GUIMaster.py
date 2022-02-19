import tkinter.messagebox
from tkinter import *
import University.globals as globals
from tkinter import ttk
import Programs.activity_choice as activity_choice

userrecognized=True

##########################################
#          Main Window creation          #
##########################################
main_win=Tk() #creating the main window and storing the window object in 'win'
main_win.title('Do It All Program') #setting title of the window
main_win.geometry('300x100') #setting the size of the window



def func():#function of the button
    tkinter.messagebox.showinfo(f"Greetings!", f"Hello! Welcome to Do It All Progarm.\nI'm your host, {globals.cname}")
    #tkinter.messagebox.showinfo(f"Greetings!",activity_choice.host_start(userrecognized))

#Button Widget
btn=Button(main_win,activeforeground="blue",bg="lime", text="Start Program", width=10,height=2,command=func)
btn.place(x=195,y=15)

#Entry Widget
Label(main_win, text='Name').grid(row=0) 
#Label(main_win, text='Email').grid(row=1) #Add Rows by increasing row count
ent1 = Entry(main_win) 
#ent2 = Entry(main_win) 
ent1.grid(row=0, column=1) 
#ent2.grid(row=1, column=1) 

main_win.mainloop() #running the loop that works as a trigger