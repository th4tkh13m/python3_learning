def song_playlist(songs, max_size = 0):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    lst_song = []
    if songs[0][2] <= max_size:
        lst_song = lst_song + [songs[0][0]]
        max_size = max_size - songs[0][2]
    new_songs = songs[1:]
    sorted_songs = sorted(new_songs, key = lambda x: x[2] )
    for song in sorted_songs:
        if song[2] <= max_size:
            lst_song = lst_song + [song[0]]
            max_size = max_size - song[2]
        else:
            break
    return lst_song

song_playlist([('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)], 12.2)
    
    