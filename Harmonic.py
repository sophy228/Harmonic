
from Pitch import Pitch
from Tonality import Tonality
from Tonality import Scale
from Chord import Interval
from Chord import *
from Ukulele import *


ukulele = Ukulele()
ukulele.dump()
ukulele.dump_chord(MajorTraid(Pitch("D")))

if __name__ == '__main__':
    while(True):
        print("##################################")
        pitchname = input("请输入主调:")
        print("0 大调")
        print("1 小调")
        scale = int(input("请选择调式:"))
        if(scale == 0):
            tonality = Tonality(Pitch(pitchname),Scale.Major)
            tonality.dump_detail()
        elif(scale == 1):
            tonality = Tonality(Pitch(pitchname),Scale.Minor)
            tonality.dump_detail()
        
        