def song_decoder(song):
    song = song.replace("WUB", " ")
    song = " ".join(song.split())
    return song
print(song_decoder("AWUBWUBBWUBC"))
