from models import (
    Track, 
    Note
)


def main():
    print('Create new Track')
    name = input('input you track\'s name: ')
    track = Track(name, 'None')
    _ = track
    while True:
        track.display()
        cmd = input('$ ')
        eval(cmd)

def test():
    # make track
    track = Track('Track 0', 'Nonamed')

    # add notes
    data = [
        ('an', 'a n'), 
        ('nyeong', 'ny eo ng'), 
        ('ha', 'h a'), 
        ('se', 's e'), 
        ('yo', 'y o')
    ]
    
    for l, p in data:
        note = Note()
        note[l] = p
        track += note

    # display
    track.display()

    # move pointer
    track >> 2
    track.display()
    track << 1
    track.display()

    # check pointed note
    print(track.pointer.lyric)
    print(track.pointer.phone)

    # update lyric
    track.update(lyric='hi')
    track.display()

    # update lyric with phone
    track >> 1
    track.update(lyric='he', phone='h e')
    track.display()


if __name__ == '__main__':
    main()
