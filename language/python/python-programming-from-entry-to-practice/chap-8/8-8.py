# -*- coding: utf-8 -*-


def make_album(singer, album, count=1):
    if count > 1:
        return {'singer': singer, 'album': album, 'count': int(count)}
    else:
        return {'singer': singer, 'album': album}


while True:
    singer = input("\nPlease enter singer name: ")
    album = input("\nEnter the album name: ")
    count = input(
        "\nEnter the number of songs in the album(if you know) ") or 0
    print(make_album(singer, album, int(count)))
    msg = input("\nDo you want to keep going?(enter 'q' or 'quit' can break) ")
    if msg == 'q' or msg == 'quit':
        break
