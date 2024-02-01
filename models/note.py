from typing import List


class Note:
    def __init__(self, lyric='la', pitch='C', phone='la'):
        self._id = id(self)
        self._lyric = lyric
        self._pitch = pitch
        self._phone = phone
        self._prev = None
        self._next = None

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
    
    def valid(self, lyric, phone):
        pass
    
    def update(self):
        # prev + cur + next 3개를 넣고, 한번에 g2p 검사를 시행한다.
        if not self.valid(self.lyric, self.phone):
            self.phone = self.phone # G2P
            self.update(self.prev)
            self.update(self.next)
        
