from enum import Enum
from Chord import *
from Pitch import Pitch

class Scale(Enum):
    Major = 0
    Minor = 1

class Tonality(object):
    """description of class"""
    def __init__(self, rootpitch, scale):
        self.root_pitch = rootpitch
        self.scale = scale
        if(self.scale == Scale.Major):
            self.scale_interval = [2,2,1,2,2,2,1]
        else:
            self.scale_interval = [2,1,2,2,1,2,2]

    def get_pitchset(self):
        pitchlist = []
        pitch = self.root_pitch
        pitchlist.append(pitch)
        for interval in self.scale_interval:
            if(interval == 2):
                pitch = pitch.forward_interval(Interval.M2)
            else:
                pitch = pitch.forward_interval(Interval.m2)
            pitchlist.append(pitch)
        return pitchlist

    def get_chords_table(self):
        pitchlist = self.get_pitchset()
        chordstable = {}
        index = 1
        if(self.scale == Scale.Major):
            for pitch in pitchlist:
                if(index == 7):
                    chordstable[index] = DiminishedTraid(pitch)
                    break
                elif (index == 2 or index == 3 or index == 6):
                    chordstable[index] = MinorTraid(pitch)
                else:
                    chordstable[index] = MajorTraid(pitch)
                index += 1
        elif(self.scale == Scale.Minor):
            for pitch in pitchlist:
                if(index == 7):
                    break;
                if(index == 2):
                    chordstable[index] = DiminishedTraid(pitch)
                elif (index == 1 or index == 4 or index == 5):
                    chordstable[index] = MinorTraid(pitch)
                else:
                    chordstable[index] = MajorTraid(pitch)
                index += 1

        return chordstable

    def dump_detail(self):
        Majorchordsteps = ["I", "ii","iii", "IV", "V", "vi", "vii"]
        Minorchordsteps = ["i", "ii","III", "iv", "v", "VI", "VII"]
        if(self.scale == Scale.Major):
            scale = "Major"
            chordsteps = Majorchordsteps
        else:
            scale = "Minor"
            chordsteps = Minorchordsteps
        print(str.format("{}\t{}", self.root_pitch, scale))
        pitch_list = self.get_pitchset()
        for p in pitch_list:
            print(p,end='\t')
        print("\nChords:")
        chords_table = self.get_chords_table()
        
        for k, v in chords_table.items():
            pitches = v.get_pitches()
            print(str.format("{:^5s}({})",chordsteps[k-1],str(v)),end='\t')
            for pitch in pitches:
                print(pitch, end='\t')
            print("")










