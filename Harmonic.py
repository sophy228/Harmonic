
from Pitch import Pitch
from Tonality import Tonality
from Tonality import Scale

ptich = Pitch("E#")
ptich.rename()
print(ptich.pitchname)
print("#########################################")
tonality = Tonality(Pitch("D"), Scale.Major)
pitch_list = tonality.get_pitchset()
for p in pitch_list:
    print(p.pitchname,end=' ')
print('')
tonality = Tonality(Pitch("C"), Scale.Minor)
pitch_list = tonality.get_pitchset()
for p in pitch_list:
    print(p.pitchname,end=' ')
print('')