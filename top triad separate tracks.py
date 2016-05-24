#Import the library
from MidiFile3 import MIDIFile
import random
import numbers

'''gui stuff: length of piece, tempo, instrument, volume, keys, name'''

# Create the MIDIFile Object
MyMIDI = MIDIFile(2) ### the integer = the number of parallel tracks available

# Add track names and tempo. The first argument to addTrackName and
# addTempo is the time to write the event. This initialises the tracks.
tracks = (0, 1)
start_time = 0

MyMIDI.addTrackName(tracks[0],start_time,"Melody")


MyMIDI.addTempo(tracks[0],start_time, 120)
#MyMIDI.addTrackName(tracks[1],start_time,"Cello")
#MyMIDI.addTempo(tracks[1],start_time, 120)

# Each track can hold multiple channels, we'll use two for now
channels = (0,1,2,3)

# Add a note. addNote expects the following information:
#channel = some integer >= 0
#pitch = some integer >= 0 ... middle C = 60
#duration = 1 corresponds to a crotchet, aka a quarter note
#volume = 100
volume = 100 # may as well specify this here for now

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
        self.treble_loc += length # moving to next time to start a note

                
    def harmonize2(self, h, lengthbass, lengthA, lengthT):
        harmony_list = []
        for something in triad[str(h)]:
            print(triad[str(h)])
            harmony_list.append(something)
        self.add2bass(harmony_list[0], lengthbass)
        if self.treble_loc > 16:
            self.add2alto(harmony_list[2], lengthA)
        if self.treble_loc > 12:
            self.add2tenor(harmony_list[1], lengthT)
        

            
            
            
            
            
    def add2alto(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[1],pitch,self.treble_loc,length,volume)
        
    def add2tenor(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[2],pitch,self.treble_loc,length,volume)
        
    def add2bass(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[3],pitch,self.bass_loc,length,volume)
        self.bass_loc += length # moving to next time to start a note

        
'''    def harmonize(self, h, length): 
        channel = 0
        for something in triad[str(h)]:
            channel += 1
            MyMIDI.addNote(tracks[0],channels[],something,self.treble_loc,length,volume)'''
            
#        self.treble_loc += length # moving to next time to start a note
octave = dict([('C-1',48),('D-1',50),('E-1',52),('F-1',53),('G-1',55),('A-1',57),('B-1',59),('C0',60),('D0',62),('E0',64),('F0',65),('G0',67),('A0',69),('B0',71),('C1',72),('D1',74),('E1',76),('F1',77),('G1',79),('A1',81),('B1',83)]) #in dictionary format for easy understanding. can work in list form but note names wont be available.
melodychoice = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83]
melody_length = [0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 4.0]
A_length = [1.0, 2.0, 2.0]
T_length = [0.5, 0.5, 1.0, 1.0]
accom_length = [1.0, 1.0, 2.0, 2.0, 2.0, 2.0]
triad = dict([('48',(octave['C-1'], octave['E-1'], octave['G-1'])), ('50',(octave['D-1'], octave['F-1'], octave['A-1'])),
              ('52',(octave['E-1'], octave['G-1'], octave['B-1'])), ('53',(octave['F-1'], octave['A-1'], octave['C0'])),
              ('55',(octave['G-1'], octave['B-1'], octave['D0'])), ('57',(octave['A-1'], octave['C0'], octave['E0'])),
              ('59',(octave['B-1'], octave['D0'], octave['F0'])), ('60',(octave['C-1'], octave['C0'], octave['E0'], octave['G0'])),
              ('62',(octave['D-1'], octave['D0'], octave['F0'], octave['A0'])), ('64',(octave['E-1'], octave['E0'], octave['G0'], octave['B0'])), ('65',(octave['F-1'], octave['F0'], octave['A0'], octave['C1'])),
              ('67',(octave['G-1'],  octave['G0'], octave['B0'], octave['D1'])), ('69',(octave['A-1'], octave['A0'], octave['C1'], octave['E1'])),
              ('71',(octave['B-1'], octave['B0'], octave['D1'], octave['F1'])), ('72',(octave['C-1'], octave['C1'], octave['E1'], octave['G1'])),
              ('74',(octave['D-1'], octave['D1'], octave['F1'], octave['A1'])), ('76',(octave['E-1'], octave['E1'], octave['G1'], octave['B1'])),
              ('77',(octave['F-1'], octave['F1'], octave['A1'], octave['C1'])), ('79',(octave['G-1'], octave['G1'], octave['B1'], octave['D1'])), 
              ('81',(octave['A-1'], octave['A1'], octave['C1'], octave['E1'])), ('83',(octave['B-1'], octave['B1'], octave['D1'], octave['F1']))])

#print(triad['1'])



Composition = compose()
duration = 0
x = 0
y = int(len(melodychoice)-1)
#    melody_note = random.choice(list(melodychoice))

while duration < 40:
    i = random.randint(x, y)
    print("i is of value: " + str(i))
    Mnote_length = random.choice(list(melody_length))
    Bnote_length = random.choice(list(accom_length))
    Anote_length = random.choice(list(A_length))
    Tnote_length = random.choice(list(T_length))
    Composition.add2melody(melodychoice[i],Mnote_length)
    if Composition.treble_loc > 8:
        Composition.harmonize2(melodychoice[i], Bnote_length, Anote_length, Tnote_length)
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
    


    
    
    

    
    
binfile = open("outputtesttriadchannels4.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

'''print(octave[random.choice(list(octave.keys()))])
print(octave['G'])'''
