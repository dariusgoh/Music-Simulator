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
        self.slideButtons()
        self.volume = self.volume_data

            
    def initUI(self):
        self.title = Label(self.frame, text = "Power of Composition at your fingertips!!")
        self.title.grid(row = 0, column = 0)
        
        self.button = Button(self.frame, text="QUIT", command=self.frame.quit)
        self.button.grid(row = 10, column = 0, sticky = E)
        
    def slideButtons(self):
        self.tempo_data = IntVar()
        self.volume_data = IntVar()
        self.volume_display = self.volume_data
        
        self.tempo = Label(self.frame, text = "Adjust the tempo to your liking, click OK when done")
        self.tempo.grid(row = 3, column = 0, sticky = S)
        
        self.tempo_slide = Scale(self.frame, from_ = 0, to = 300, orient = HORIZONTAL)
        self.tempo_slide.grid(row = 4, column = 0, columnspan = 7, sticky = W + E)
        
        self.tempo_confirm = Button(self.frame, text="OK", command=self.update_tempo_data)
        self.tempo_confirm.grid(row = 4, column = 8, sticky = W)
        
        self.tempo_info = Label(self.frame, textvariable = self.tempo_data)
        self.tempo_info.grid(row=4, column = 9, columnspan = 2)
        
        self.volume = Label(self.frame, text = "Adjust the volume to your liking, click OK when done")
        self.volume.grid(row = 5, column = 0)
        
        self.volume_slide = Scale(self.frame, from_ = 0, to = 100, orient = HORIZONTAL)
        self.volume_slide.grid(row = 6, column = 0, columnspan = 7, sticky = W + E)
        
        self.volume_confirm = Button(self.frame, text="OK", command=self.update_volume_data)
        self.volume_confirm.grid(row =6, column = 8, sticky = W)
        
        self.slide_info = Label(self.frame, textvariable = self.tempo_data)
        self.slide_info.grid(row=3, column = 2, columnspan = 2)
        
        self.length = Label(self.frame, text = "Adjust the length of the piece to your liking, click OK when done")
        self.length.grid(row = 8, column = 0, sticky = N)
    
        self.length_slide = Scale(self.frame, from_ = 0, to = 300, orient = HORIZONTAL)
        self.length_slide.grid(row = 9, column = 0, columnspan = 7, sticky = W + E)
        
        self.length_confirm = Button(self.frame, text="OK", command=self.update_length_data)
        self.length_confirm.grid(row =9, column = 8, sticky = W)
        
        self.slide_info = Label(self.frame, textvariable = self.tempo_data)
        self.slide_info.grid(row=3, column = 2, columnspan = 2)
            
    def update_tempo_data(self):
        self.tempo_data.set(self.tempo_slide.get())
    
    def update_volume_data(self):
        y = (self.volume_slide.get())
        print(y)


    def update_length_data(self):
        self.length_data.set(self.length_slide.get())
        
      
def main():  
    root = Tk()
    root.geometry("750x400+350+300")
    app = Window(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  

