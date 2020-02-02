from aenum import Enum, NoAlias
from aenum import NamedConstant

class Interval(Enum):
    _settings_ = NoAlias
    P1 = 0
    d2 = 0
    A1 = 1
    m2 = 1
    M2 = 2
    d3 = 2
    A2 = 3
    m3 = 3
    M3 = 4
    d4 = 4
    A3 = 5
    P4 = 5
    A4 = 6
    Tritone = 6
    d5 = 6
    P5 = 7
    d6 = 7
    A5 = 8
    m6 = 8
    M6 = 9
    d7 = 9
    A6 = 10
    m7 = 10
    M7 = 11
    d8 = 11
    A7 = 12
    P8 = 12

    @classmethod
    def get_intervals_byharmoic(cls):
        Harmonic_Table = {Interval.P1:1, Interval.m2:240, Interval.M2:72, 
                    Interval.m3:30, Interval.M3:20, Interval.P4:12,
                    Interval.Tritone:70, Interval.P5:6, Interval.m6:40,
                    Interval.M6:15, Interval.m7:45, Interval.M7:120,
                    Interval.P8:2}
        ls = list(Harmonic_Table.items())
        ls.sort(key=lambda x:x[1])
        return ls


class Chord(object):
    """description of class"""
    def __init__(self, rootpitch,*intverals):
        self.rootpitch = rootpitch
        self.intverals = list(intverals)
        self.notenumber = len(self.intverals)
        self.chordpitches = [self.rootpitch]

        for interval in self.intverals:
            self.chordpitches.append(self.rootpitch.forward_interval(interval))

    def get_pitches(self):
        return self.chordpitches



class MajorTraid(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.M3,Interval.P5)
    def __str__(self):
        return str.format("{}", self.rootpitch)

class MinorTraid(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.m3,Interval.P5)
    def __str__(self):
        return str.format("{}m", self.rootpitch)

class AugmentedTraid(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.M3,Interval.A5)
    def __str__(self):
        return str.format("{}+", self.rootpitch)

class DiminishedTraid(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.m3,Interval.d5)
    def __str__(self):
        return str.format("{}dim", self.rootpitch)

class DiminishedSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.m3,Interval.d5,Interval.d7)
    def __str__(self):
        return str.format("{}dim7", self.rootpitch)

class HalfdiminishedSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.m3,Interval.d5,Interval.m7)
    def __str__(self):
        return str.format("{}ø7", self.rootpitch)

class MinorSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.m3,Interval.P5,Interval.m7)
    def __str__(self):
        return str.format("{}m7", self.rootpitch)

class MinorMajorSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.m3,Interval.P5,Interval.M7)
    def __str__(self):
        return str.format("{}mM7", self.rootpitch)

class DominantSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.M3,Interval.P5,Interval.m7)
    def __str__(self):
        return str.format("{}7", self.rootpitch)

class MajorSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.M3,Interval.P5,Interval.M7)
    def __str__(self):
        return str.format("{}M7", self.rootpitch)

class AugmentedSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.M3,Interval.A5,Interval.m7)
    def __str__(self):
        return str.format("{}+7", self.rootpitch)

class AugmentedMajorSeventh(Chord):
    def __init__(self, rootpitch):
        Chord.__init__(self, rootpitch, Interval.M3,Interval.A5,Interval.M7)
    def __str__(self):
        return str.format("{}+M7", self.rootpitch)








