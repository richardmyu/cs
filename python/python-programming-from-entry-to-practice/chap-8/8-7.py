# -*- coding: utf-8 -*-


def make_album(singer, album, count=1):
    if count > 1:
        return {'singer': singer, 'album': album, 'count': int(count)}
    else:
        return {'singer': singer, 'album': album}


print(make_album('jack', 'fun'))
print(make_album('bob', 'bananan', 12))
print(make_album('meimei', 'rain', 5))
