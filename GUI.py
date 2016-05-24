'''
Created on Jul 30, 2014
@author: darius
'''
from tkinter import * ## use Tkinter for 2.7.*

class Fun :
    def __init__(self, master) :
        self.frame = Frame(master)
        self.frame.pack()
        self.createWidgets()
        self.drawing_space = Frame(master)
        self.drawing_space.pack()
        self.sketching_space = Canvas(self.drawing_space, width = 600, height = 600)
        self.sketching_space.pack()
        self.sketching_space.create_line(0,0,300,150)
        self.sketching_space.create_line(0,300,15,300)
        self.sketching_space.create_line(0,150,300,0, fill = "red", dash=(4,4))
        self.sketching_space.create_rectangle(50,25,250,125, fill = "blue")
        self.sketching_space.create_text(75, 75, text = "`Hello!!!", fill="pink",
                                         font=('Courier', 36, 'italic'))
    def createWidgets(self):
        self.button = Button(self.frame, text="QUIT", command=self.frame.quit)
        self.button.grid(row = 3, column = 0)
       
        self.my_text = StringVar()
        self.my_data = IntVar()
        
        self.slide = Scale(self.frame, from_ = 0, to = 200, orient = HORIZONTAL)
        self.slide.grid(row = 0, column = 0, columnspan = 4, sticky = W + E)
        
        self.info = Label(self.frame, textvariable = self.my_text)
        self.info.grid(row = 3, column = 0, columnspan = 4, sticky = W)
        
        self.slide_info = Label(self.frame, textvariable = self.my_data)
        self.slide_info.grid(row=3, column = 2, columnspan = 2)
        
        self.info = Label(self.frame, textvariable = self.my_text)
        self.info.grid(row = 3, column = 0, columnspan = 4, sticky = W)
        
        self.slide_info = Label(self.frame, textvariable = self.my_data)
        self.slide_info.grid(row=3, column = 2, columnspan = 2)
        
    def update_data(self):
        self.my_data.set(self.slide.get())

    def keyC(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyCsharp(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyD(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyDsharp(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyE(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyF(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyFsharp(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyG(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyGsharp(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyA(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyAsharp(self):
        print("IDK WHAT TO DOOOOO")
        
    def keyB(self):
        print("IDK WHAT TO DOOOOO")
        

root = Tk() # creates a tk root widget aka window
w = Fun(root)
root.mainloop()
#root.destroy() # optional





