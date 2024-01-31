from typing import List

from .note import Note


class Track:
    def __init__(self, name, singer):
        self.name = name
        self.singer = singer
        self.notes: List[Note] = []
        self.pointer: Note = None
        # self.cursor = Cursor()

    def __iadd__(self, other):
        if not isinstance(other, Note):
            raise ValueError

        if any(self.notes):
            self.notes[-1] >> other
            self.notes.append(other)
        else:
            self.notes.append(other)
            self.pointer = other

        return self

    def __lshift__(self, number):
        for _ in range(number):
            if self.pointer.prev is not None:
                self.pointer = self.pointer.prev
            else:
                raise IndexError

    def __rshift__(self, number):
        for _ in range(number):
            if self.pointer.next is not None:
                self.pointer = self.pointer.next
            else:
                raise IndexError

    def lyrics(self):
        return [note.lyric for note in self.notes]

    def phones(self):
        return [note.phone for note in self.notes]

    def update(self, /, lyric='', *, phone=''):
        if lyric:
            if phone:
                self.pointer[lyric] = phone
            else:
                self.pointer[lyric]
        else:
            raise ValueError

    def display(self):
        print('=' * 30)
        head = []
        for note in self.notes:
            if note == self.pointer:
                head.append('V')
            else:
                head.append(' ')
        print('\t', end='')
        print('\t|\t'.join(head))
        print('\t', end='')
        print('\t|\t'.join(self.lyrics()))
        print('\t', end='')
        print('\t|\t'.join(self.phones()))
        print('='*30)
