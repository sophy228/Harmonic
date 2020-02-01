from enum import Enum


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
            pitch = pitch.add_interval(interval)
            if(self.scale == Scale.Minor):
                pitch.rename()
            pitchlist.append(pitch)
        return pitchlist



