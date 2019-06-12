def song_decoder(song):
    song = song.replace("WUB", " ")
    song = song.lstrip()
    song = song.rstrip()
    print(song)
    return song

song_decoder("AWUBWUBWUBBWUBWUBWUBC  ")