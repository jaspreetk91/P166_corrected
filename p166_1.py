from tkinter import *
from tkinter import Entry
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()
root.title("C166")
root.geometry('600x600')

canvas = Canvas(root,width=600,height=500,bg='white',highlightbackground='blue')
canvas.pack()

label = Label(root,text='choose color')
label.place(relx=0.2,rely=0.8,anchor=CENTER)

fillcolor = ['red','orange','yellow','green','blue','purple','brown','grey','black']

dropdown = ttk.Combobox(state='readonly',values=fillcolor,width=10)
dropdown.place(relx=0.35,rely=0.8,anchor=CENTER)



startx = Label(root,text='startx')
startx.place(relx=0.4,rely=0.8,anchor=CENTER)

coordinates_values = [10,50,100,200,300,400,500,600,800,900]

dropdown2 = ttk.Combobox(state='readonly',values=coordinates_values,width=10)
dropdown2.place(relx=0.45,rely=0.8,anchor=CENTER)


starty = Label(root,text='starty')
starty.place(relx=0.5,rely=0.8,anchor=CENTER)

coordinates_values = [10,50,100,200,300,400,500,600,800,900]

dropdown3 = ttk.Combobox(state='readonly',values=coordinates_values,width=10)
dropdown3.place(relx=0.55,rely=0.8,anchor=CENTER)


endx = Label(root,text='startx')
endx.place(relx=0.6,rely=0.8,anchor=CENTER)

coordinates_values = [10,50,100,200,300,400,500,600,800,900]

dropdown4 = ttk.Combobox(state='readonly',values=coordinates_values,width=10)
dropdown4.place(relx=0.65,rely=0.8,anchor=CENTER)


endy = Label(root,text='startx')
endy.place(relx=0.7,rely=0.8,anchor=CENTER)

coordinates_values = [10,50,100,200,300,400,500,600,800,900]

dropdown5 = ttk.Combobox(state='readonly',values=coordinates_values,width=10)
dropdown5.place(relx=0.75,rely=0.8,anchor=CENTER)

mainloop()