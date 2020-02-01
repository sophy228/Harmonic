class Pitch(object):
    """description of class"""
    A4_frequncy = 440
    interval_table = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}
    signature_list = {'#':1,'b':-1}
    def __init__(self, pitchname = "A4"):
        self.__parse_name(pitchname)

    def __parse_name(self,pitchname):
        self.oct_index = 4
        self.key_signature = ''
        self.pitchname = pitchname
        self.basepitch = pitchname[0].upper()
        if(len(pitchname) > 1):
            if(pitchname[1] in Pitch.signature_list):
                self.key_signature = pitchname[1]
            else:
                self.oct_index = int(pitchname[1])
        if(len(pitchname) > 2):
            self.key_signature = pitchname[2]

    def to_freq(self):
        current_A_freq = self.A4_frequncy*(2**(self.oct_index - 4))
        interval_index = self.interval_table[self.basepitch]
        interval_index += self.signature_list.get(self.key_signature, 0)
        n = interval_index - self.interval_table['A']
        freq = current_A_freq *(2**(n/12))
        return freq

    def add_interval(self, number):
         interval_index = self.interval_table[self.basepitch]
         interval_index += self.signature_list.get(self.key_signature, 0)
         interval_index += number;
         new_interval_index = interval_index % 12
         new_basepitch = 'C'
         new_key_signature = ''
         for k,v in self.interval_table.items():
             if(new_interval_index < v):
                 break
             new_basepitch = k
         if(new_interval_index -  self.interval_table[new_basepitch] > 0):
             new_key_signature = '#'
         new_oct_index = self.oct_index + interval_index // 12
         new_pitchname = str.format("{}{}{}",new_basepitch,new_oct_index,new_key_signature)
         return Pitch(new_pitchname)
    
    def rename(self):
        if(self.key_signature in self.signature_list):
            names = list(self.interval_table.keys())
            index = 0
            for name in names:
                if (name == self.basepitch):
                    break;
                index += 1
            i = self.signature_list[self.key_signature]
            self.basepitch = names[index + i]
            if(self.interval_table[names[index + i]] - self.interval_table[names[index]] > 1):
                if(self.key_signature == '#'):
                    self.key_signature = 'b'
                else:
                    self.key_signature = '#'
            else:
                self.key_signature = ''
            self.pitchname = str.format("{}{}{}",self.basepitch,self.oct_index,self.key_signature)

    def __str__(self):
        return self.pitchname