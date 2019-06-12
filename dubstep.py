def song_decoder(song):
    song = song.replace("WUB", " ")
    song = ' '.join(song.split())
    print(song)
    return song

song_decoder("AWUBWUBWUBBWUBWUBWUBC  ")