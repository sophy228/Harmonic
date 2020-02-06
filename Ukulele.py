from Pitch import Pitch
from Chord import *

class String(object):
    def __init__(self, rootPitch:Pitch, fretnumber, invterval=1):
        pitch = self.rootpitch = rootPitch
        self.pitches=[rootPitch]
        for index in range(1,fretnumber + 1):
            pitch = pitch.add_interval(invterval)
            self.pitches.append(pitch)
        self.fretnumber = fretnumber
    
    def __iter__(self):
        return iter(self.pitches)
    
    def __next__(self):
        return next(self.pitches)

    def __getitem__(self,i): 
        return self.pitches[i]

    def find_chord_positions(self, chord:Chord):
        index = 0
        positions = {}
        chordpitches = chord.get_pitches()
        chordnames = []
        for p in chordpitches:
            name = str(p)
            chordnames.append(name)
        for p in self.pitches:
            if (str(p) in chordnames):
                positions[str(p)] = index
                chordnames.remove(str(p))
            index += 1
        return positions


class Ukulele(object):
    """description of class"""
    def __init__(self, pitch4=Pitch("G"), pitch3=Pitch("C"), 
                 pitch2=Pitch("E"), pitch1=Pitch("A")):
       self.strings = {}
       self.strings[1] = String(pitch1, 19)
       self.strings[2] = String(pitch2, 19)
       self.strings[3] = String(pitch3, 19)
       self.strings[4] = String(pitch4, 19)

    def dump(self):
        print("Ukulele:")
        print("{:^10s}{:^10d}{:^10d}{:^10d}{:^10d}".format('Fret',4,3,2,1))
        for i in range(self.strings[1].fretnumber):
            print("{:^10d}".format(i),end='')
            for j in [4,3,2,1]:
                print("{:^10s}".format(str(self.strings[j][i])),end='')
            print("")

    def dump_chord(self,  chord:Chord):
        strings = [4,3,2,1]
        chordpitches = chord.get_pitches()
        chordnames = []
        chordnamesbak = []
        for p in chordpitches:
            name = str(p)
            chordnames.append(name)
            chordnamesbak.append(name)
        
        sumtable = {}
        for index in range(1,5):
            table = self.strings[index].find_chord_positions(chord)
            for k,v in table.items():
                sumtable[(k,index)] = v
        sumlist = list(sumtable.items())
        sumlist.sort(key=lambda x:x[1])

        finalist = []
        for element in sumlist:
            pitchname = element[0][0]
            stringindex = element[0][1]
            position = element[1]
            if((stringindex in strings)):
               if (pitchname in chordnames):
                    finalist.append((pitchname,stringindex, position))
                    chordnames.remove(pitchname)
                    strings.remove(stringindex)
               elif( (len(strings) == 1) and (pitchname in chordnamesbak)):
                   finalist.append((pitchname,stringindex, position))
                   strings.remove(stringindex)
                   break

        print("Ukulele:", chord)
        print("{:^10s}{:^10d}{:^10d}{:^10d}{:^10d}".format('Fret',4,3,2,1))
        for i in range(self.strings[1].fretnumber): 
            print("{:^10d}".format(i),end='')
            for j in [4,3,2,1]:
                if( i != 0 and (str(self.strings[j][i]), j, i) in finalist):
                    print("{:^10s}".format(str(self.strings[j][i])+'●'),end='')
                else:
                    print("{:^10s}".format(str(self.strings[j][i])),end='')
            if(i == 0):
                print("\n================================================")
            else:
                print("")
        print(finalist)






