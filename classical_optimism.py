'''
Created on Aug 2, 2014
modified from the single-note-example form midiutil
@author: darius
'''
############################################################################
# A sample program to create a multi-track MIDI file, add notes,
# and write to disk.
############################################################################

#Import the library
from MidiFile3 import MIDIFile
import testgui

# Create the MIDIFile Object
MyMIDI = MIDIFile(2) ### the integer = the number of parallel tracks available

# Add track names and tempo. The first argument to addTrackName and
# addTempo is the time to write the event. This initialises the tracks.
tracks = (0, 1)
start_time = 0

MyMIDI.addTrackName(tracks[0],start_time,"Piano")
MyMIDI.addTempo(tracks[0],start_time, 120)
#MyMIDI.addTrackName(tracks[1],start_time,"Cello")
#MyMIDI.addTempo(tracks[1],start_time, 120)

# Each track can hold multiple channels, we'll use two for now
channels = (0,1)

# Add a note. addNote expects the following information:
#channel = some integer >= 0
#pitch = some integer >= 0 ... middle C = 60
#duration = 1 corresponds to a crotchet, aka a quarter note
#volume = 100
volume = Window.volume_data # may as well specify this here for now

# Now add the note.
# MyMIDI.addNote(track,channel,pitch,note_start_time,duration,volume)
class compose:
    def __init__(self):
        self.treble_loc = start_time
        self.bass_loc = start_time
#        self.octave = dict([('C',60),('D',62),('E',64),('F',65),
#                            ('G',67),('A',69),('B',71),
#                            ('C#',61),('D#',63),('F#',66),('G#',68),('A#',70),
#                            ('Db',61),('Eb',63),('Gb',66),('Ab',68),('Bb',70)])

    def add2treble(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[0],pitch,self.treble_loc,length,volume)
        self.treble_loc += length # moving to next time to start a note
    def add2bass(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[1],pitch,self.bass_loc,length,volume)
        self.bass_loc += length # moving to next time to start a note

composition = compose()
composition.add2treble(64, 1)
composition.add2treble(62, 1)
composition.add2treble(60, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)

print(str(volume))

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

