from typing import List
from utils import G2P

class Note:
    def __init__(self, lyric, pitch='', prev=None, next=None):
        self._id = id(self)
        self._lyric = lyric
        self._pitch = pitch
        self._phone = ''
        self._prev = prev
        self._next = next
        self._g2p = G2P()
        
        self.update()

    def __rshift__(self, other):
        if not isinstance(other, Note):
            raise ValueError

        other._prev = self
        self._next = other

    def __getitem__(self, lyric):
        self.lyric = lyric

    def __setitem__(self, lyric, phone):
        self.lyric = lyric
        self.phone = phone

    def __eq__(self, other):
        if not isinstance(other, Note):
            raise ValueError

        return self._id == other._id

    @property
    def lyric(self):
        return self._lyric

    @lyric.setter
    def lyric(self, value):
        self._lyric = value
        self.update()

    @property
    def pitch(self):
        return self._pitch

    @pitch.setter
    def pitch(self, value):
        self._pitch = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def prev(self):
        return self._prev

    @property
    def next(self):
        return self._next
    
    def get_nodes(self):
        flag = [True,] # for find current note
        nodes = [self.lyric, ]
        if self.prev is not None:
            nodes.insert(0, self.prev.lyric)
            flag.insert(0, False)

        if self.next is not None:
            nodes.append(self.next.lyric)
            flag.append(False)
            
        return {
            'nodes': nodes, 
            'index': flag.index(True),
            'has_prev': self.prev is not None,
            'has_next': self.next is not None
        }
    
    def valid(self):
        if self.phone == '':
            return False
        
        data = self.get_nodes()
            
        predict = self._g2p.gen(data['nodes'])
        return self.phone == predict[data['index']]
    
    def update(self):
        # prev + cur + next 3개를 넣고, 한번에 g2p 검사를 시행한다.
        if not self.valid():
            data = self.get_nodes()
            phonemes = self._g2p.gen(data['nodes'])
            self.phone = phonemes[data['index']]
            
            if data['has_prev']:
                self.prev.phone = phonemes[data['index']-1]
                # self.prev.update()
                
            if data['has_next']:
                self.next.phone = phonemes[data['index']+1]
                # self.next.update()
        
