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
        ('안', 'a n'), 
        ('녕', 'ny eo ng'), 
        ('하', 'h a'), 
        ('세', 's e'), 
        ('요', 'y o')
    ]
    
    for l, _ in data:
        track.add(l)

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
    track.update(lyric='히')
    track.display()

    # update lyric with phone
    track >> 1
    track.update(lyric='헤', phone='h e')
    track.display()


if __name__ == '__main__':
    main()
    # test()
