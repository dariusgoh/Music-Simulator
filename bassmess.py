#Import the library
from MidiFile3 import MIDIFile
import random
import numbers

from tkinter import *

properties_list = []

class Window :
    def __init__(self, master) :
        self.frame = Frame(master)
        self.frame.pack()
        self.initUI()
        self.slideButtons()

            
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
        
        self.volume_info = Label(self.frame, textvariable = self.volume_data)
        self.volume_info.grid(row=3, column = 2, columnspan = 2)
        
        self.length = Label(self.frame, text = "Adjust the length of the piece to your liking, click OK when done")
        self.length.grid(row = 8, column = 0, sticky = N)
    
        self.length_slide = Scale(self.frame, from_ = 0, to = 300, orient = HORIZONTAL)
        self.length_slide.grid(row = 9, column = 0, columnspan = 7, sticky = W + E)
        
        self.length_confirm = Button(self.frame, text="OK", command=self.update_length_data)
        self.length_confirm.grid(row =9, column = 8, sticky = W)
        
        self.slide_info = Label(self.frame, textvariable = self.tempo_data)
        self.slide_info.grid(row=3, column = 2, columnspan = 2)
            
    def update_tempo_data(self):
        tempo = (self.tempo_slide.get())
        properties_list.append(tempo)
    
    def update_volume_data(self):
        volume = (self.volume_slide.get())
        properties_list.append(volume)
        

    def update_length_data(self):
        duration = (self.length_slide.get())
        properties_list.append(duration)
        print(properties_list)
        
      
def main():  
    root = Tk()
    root.geometry("750x400+350+300")
    app = Window(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  



'''gui stuff: length of piece, tempo, instrument, volume, keys, name'''

# Create the MIDIFile Object
MyMIDI = MIDIFile(2) ### the integer = the number of parallel tracks available

# Add track names and tempo. The first argument to addTrackName and
# addTempo is the time to write the event. This initialises the tracks.
tracks = (0, 1)
start_time = 0

MyMIDI.addTrackName(tracks[0],start_time,"Melody")


MyMIDI.addTempo(tracks[0],start_time, properties_list[0])
#MyMIDI.addTrackName(tracks[1],start_time,"Cello")
#MyMIDI.addTempo(tracks[1],start_time, 120)

# Each track can hold multiple channels, we'll use two for now
channels = (0,1,2,3)

# Add a note. addNote expects the following information:
#channel = some integer >= 0
#pitch = some integer >= 0 ... middle C = 60
#duration = 1 corresponds to a crotchet, aka a quarter note
#volume = 100
volume = properties_list[1] # may as well specify this here for now

class compose:
    def __init__(self): #add randomization method if have time, and key will be C major and "sorry but only c maj will be available others will be ava in next version
        self.treble_loc = start_time
        self.bass_loc = start_time
        '''self.channels = channels
        self.key = key
        self.tempo = tempo
        self.volume = volume
        self.instrument = instrument'''
        
    def add2melody(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[0],pitch,self.treble_loc,length,volume)

                
    def harmonize2(self, h, length):
        harmony_list = []
        for something in triad[str(h)]:
            print(triad[str(h)])
            harmony_list.append(something)
        self.add2bass(harmony_list[0], length)
        if self.treble_loc > 16:
            self.add2alto(harmony_list[2], length)
        if self.treble_loc > 12:
            self.add2tenor(harmony_list[1], length)
        
            
    def add2alto(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[1],pitch,self.treble_loc,length,volume)
        
    def add2tenor(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[2],pitch,self.treble_loc,length,volume)
        
    def add2bass(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[3],pitch,self.treble_loc,length,volume)

        
'''    def harmonize(self, h, length): 
        channel = 0
        for something in triad[str(h)]:
            channel += 1
            MyMIDI.addNote(tracks[0],channels[],something,self.treble_loc,length,volume)'''
            
#        self.treble_loc += length # moving to next time to start a note
octave = dict([('C-1',48),('D-1',50),('E-1',52),('F-1',53),('G-1',55),('A-1',57),('B-1',59),('C0',60),('D0',62),('E0',64),('F0',65),('G0',67),('A0',69),('B0',71),('C1',72),('D1',74),('E1',76),('F1',77),('G1',79),('A1',81),('B1',83)]) #in dictionary format for easy understanding. can work in list form but note names wont be available.
melodychoice = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83]
melody_length1 = [2.0, 2.0, 2.0, 4.0]
melody_length2 = [0.5, 0.5, 1.0, 1.0, 1.0]
melody_length3 = [0.5, 0.50, 0.5, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0]
melody_length4 = [1.0, 1.0, 1.0, 2.0, 2.0]
A_length = [1.0, 2.0, 2.0]
T_length = [1.0, 2.0, 2.0]
accom_length = [1.0, 2.0, 2.0]
triad = dict([('48',(octave['C-1'], octave['E-1'], octave['G-1'])), ('50',(octave['D-1'], octave['F-1'], octave['A-1'])),
              ('52',(octave['E-1'], octave['G-1'], octave['B-1'])), ('53',(octave['F-1'], octave['A-1'], octave['C0'])),
              ('55',(octave['G-1'], octave['B-1'], octave['D0'])), ('57',(octave['A-1'], octave['C0'], octave['E0'])),
              ('59',(octave['B-1'], octave['D0'], octave['F0'])), ('60',(octave['C-1'], octave['C0'], octave['E1'], octave['G0'])),
              ('62',(octave['F-1'], octave['D0'], octave['F1'], octave['A0'])), ('64',(octave['G-1'], octave['E0'], octave['G1'], octave['B0'])), ('65',(octave['F-1'], octave['F0'], octave['A0'], octave['C1'])),
              ('67',(octave['B-1'],  octave['G0'], octave['B1'], octave['D1'])), ('69',(octave['C-1'], octave['A0'], octave['C0'], octave['E1'])),
              ('71',(octave['D-1'], octave['B0'], octave['D0'], octave['F1'])), ('72',(octave['E-1'], octave['C0'], octave['E1'], octave['G1'])),
              ('74',(octave['F-1'], octave['D0'], octave['F1'], octave['A1'])), ('76',(octave['G-1'], octave['E1'], octave['G0'], octave['B1'])),
              ('77',(octave['C-1'], octave['F1'], octave['A1'], octave['C1'])), ('79',(octave['G-1'], octave['G1'], octave['B1'], octave['D1'])), 
              ('81',(octave['E-1'], octave['A1'], octave['C1'], octave['E1'])), ('83',(octave['D-1'], octave['B1'], octave['D1'], octave['F1']))])

#print(triad['1'])



Composition = compose()
duration = 0
x = 0
y = int(len(melodychoice)-1)

while duration < properties_list[2]:
    while Composition.treble_loc < properties_list[2]/4:
        i = random.randint(x, y)
        print("i is of value: " + str(i))
        Mnote_length = random.choice(list(melody_length1))
        Bnote_length = random.choice(list(accom_length))
        Anote_length = random.choice(list(A_length))
        Tnote_length = random.choice(list(T_length))
        Composition.add2melody(melodychoice[i],Mnote_length)
        if Composition.treble_loc > 4:
            Composition.harmonize2(melodychoice[i], Mnote_length)
        Composition.treble_loc += Mnote_length # moving to next time to start a note     
        print(Composition.treble_loc)                   
        if i < 5:
            x = i - i #you will get 0 in stead of a negative number
            y = i + 5 #range of anything in step of 5
        elif i > 8: #because if it is greater than 15, then the new y value will be greater than 20
            x = i - 5
            y = (int(len(melodychoice)-1) - i) + i #ultimately gives you 20 in the end instead of being greater than 20
        else:
            x = i - 5
            y = i + 5   
        print('( ' + str(x) + ',' + str(y) + ' )') 
        duration += Mnote_length
        print(duration)
    while properties_list[2]/4 <= Composition.treble_loc < properties_list[2]/2:
        i = random.randint(x, y)
        print("i is of value: " + str(i))
        Mnote_length = random.choice(list(melody_length2))
        Bnote_length = random.choice(list(accom_length))
        Anote_length = random.choice(list(A_length))
        Tnote_length = random.choice(list(T_length))
        Composition.add2melody(melodychoice[i],Mnote_length)
        if Composition.treble_loc > 4:
            Composition.harmonize2(melodychoice[i], Mnote_length)
        Composition.treble_loc += Mnote_length # moving to next time to start a note     
        print(Composition.treble_loc)                   
        if i < 5:
            x = i - i #you will get 0 in stead of a negative number
            y = i + 5 #range of anything in step of 5
        elif i > 8: #because if it is greater than 15, then the new y value will be greater than 20
            x = i - 5
            y = (int(len(melodychoice)-1) - i) + i #ultimately gives you 20 in the end instead of being greater than 20
        else:
            x = i - 5
            y = i + 5   
        print('( ' + str(x) + ',' + str(y) + ' )') 
        duration += Mnote_length
        print(duration)
    while properties_list[2]/2 <= Composition.treble_loc < 3*properties_list[2]/4:
        i = random.randint(x, y)
        print("i is of value: " + str(i))
        Mnote_length = random.choice(list(melody_length3))
        Bnote_length = random.choice(list(accom_length))
        Anote_length = random.choice(list(A_length))
        Tnote_length = random.choice(list(T_length))
        Composition.add2melody(melodychoice[i],Mnote_length)
        if Composition.treble_loc > 4:
            Composition.harmonize2(melodychoice[i], Mnote_length)
        Composition.treble_loc += Mnote_length # moving to next time to start a note     
        print(Composition.treble_loc)                   
        if i < 5:
            x = i - i #you will get 0 in stead of a negative number
            y = i + 5 #range of anything in step of 5
        elif i > 8: #because if it is greater than 15, then the new y value will be greater than 20
            x = i - 5
            y = (int(len(melodychoice)-1) - i) + i #ultimately gives you 20 in the end instead of being greater than 20
        else:
            x = i - 5
            y = i + 5   
        print('( ' + str(x) + ',' + str(y) + ' )') 
        duration += Mnote_length
        print(duration)
    while 3*properties_list[2]/4 <= Composition.treble_loc < (properties_list[2]):
        i = random.randint(x, y)
        print("i is of value: " + str(i))
        Mnote_length = random.choice(list(melody_length4))
        Bnote_length = random.choice(list(accom_length))
        Anote_length = random.choice(list(A_length))
        Tnote_length = random.choice(list(T_length))
        Composition.add2melody(melodychoice[i],Mnote_length)
        if Composition.treble_loc > 4:
            Composition.harmonize2(melodychoice[i], Mnote_length)
        Composition.treble_loc += Mnote_length # moving to next time to start a note     
        print(Composition.treble_loc)                   
        if i < 5:
            x = i - i #you will get 0 in stead of a negative number
            y = i + 5 #range of anything in step of 5
        elif i > 8: #because if it is greater than 15, then the new y value will be greater than 20
            x = i - 5
            y = (int(len(melodychoice)-1) - i) + i #ultimately gives you 20 in the end instead of being greater than 20
        else:
            x = i - 5
            y = i + 5   
        print('( ' + str(x) + ',' + str(y) + ' )') 
        duration += Mnote_length
        print(duration)
    Composition.add2melody(67, 2)
    Composition.treble_loc += 2.0
    Composition.add2melody(60, 0.5)
    Composition.harmonize2(60, 0.5)
    Composition.treble_loc += 0.5
    Composition.add2melody(60, 6.0)
    Composition.harmonize2(60, 6.0)
    Composition.treble_loc += 6.0
    

print("volume is " + str(volume))
binfile = open("TEST.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

'''print(octave[random.choice(list(octave.keys()))])
print(octave['G'])'''
