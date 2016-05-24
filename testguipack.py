'''
created August 3rd 2014
by darius
'''
from tkinter import * 

class Window :
    def __init__(self, master) :
        self.frame = Frame(master)
        self.frame.pack()
        self.initUI()
        self.navButtons()
        self.keyButtons()
        
        
    def initUI(self):
        self.title = Label(self.frame, text = "Power of Compostition at your fingertips!!")
        self.title.grid(row = 0, column = 0)
        
        self.button = Button(self.frame, text="QUIT", command=self.frame.quit)
        self.button.pack(row = 10, column = 0, sticky = E)
        
    def navButtons(self):    
        self.tempo = Label(self.frame, text = "Adjust the tempo to your liking")
        self.t.grid(row = 3, column = 0)
        
        self.slide = Scale(self.frame, from_ = 0, to = 200, orient = HORIZONTAL)
        self.slide.grid(row = 4, column = 0, columnspan = 7, sticky = W + E)
        
        self.volume = Label(self.frame, text = "Adjust the volume to your liking")
        self.volume.grid(row = 5, column = 0)
        
        self.slide = Scale(self.frame, from_ = 0, to = 200, orient = HORIZONTAL)
        self.slide.grid(row = 6, column = 0, columnspan = 7, sticky = W + E)
        
    def update_data(self):
        self.my_data.set( self.slide.get() )
        
    def keyButtons(self):
        self.keyC = Button(self.frame, text="C", command=keysig.keyC)
        self.keyC.grid(row = 7, column = 0)
        
        self.keyCsharp = Button(self.frame, text="C#/Db", command=keysig.keyCsharp)
        self.keyCsharp.grid(row = 7, column = 1)
        
        self.keyE = Button(self.frame, text="D", command=keysig.keyE)
        self.keyE.grid(row = 7, column = 2)
        
        self.keyDsharp = Button(self.frame, text="D#/Eb", command=keysig.keyDsharp)
        self.keyDsharp.grid(row = 7, column = 3)
        
        self.keyE = Button(self.frame, text="E", command=keysig.keyE)
        self.keyE.grid(row = 7, column = 4)
        
        self.keyF = Button(self.frame, text="F", command=keysig.keyF)
        self.keyF.grid(row = 7, column = 5)
        
        self.keyFsharp = Button(self.frame, text="F#/Gb", command=keysig.keyFsharp)
        self.keyFsharp.grid(row = 8, column = 0)
        
        self.keyG = Button(self.frame, text="G", command=keysig.keyG)
        self.keyG.grid(row = 8, column = 1)
        
        self.keyGsharp = Button(self.frame, text="G#/Ab", command=keysig.keyGsharp)
        self.keyGsharp.grid(row = 8, column = 2)
        
        self.keyA = Button(self.frame, text="A", command=keysig.keyA)
        self.keyA.grid(row = 8, column = 3)
        
        self.keyAsharp = Button(self.frame, text="A#/Bb", command=keysig.keyAsharp)
        self.keyAsharp.grid(row = 8, column = 4)
        
        self.keyB = Button(self.frame, text="B", command=keysig.keyB)
        self.keyB.grid(row = 8, column = 5)
        
class keysig:
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
        
def main():  
    root = Tk()
    root.geometry("500x250+350+300")
    app = Window(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  





