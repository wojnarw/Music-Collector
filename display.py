ascii_top = """
\t████████████████████████████████████████████████████████████████████████████████████████████
\t█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒
\t█▒                                                                                         █▒
\t█▒ ARTIST NAME             ALBUM NAME                    YEAR    GENRE              LENGTH █▒
\t█▒                                                                                         █▒"""

ascii_bottom = """\
\t█▒                                                                                         █▒
\t████████████████████████████████████████████████████████████████████████████████████████████▒
\t ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

#check how many spaces we need to make columns straight
def fill (check_for_length, total_length, filler):
    space = ""
    for i in range(len(check_for_length), total_length):
        space += filler
    return space

# dict_names = {'d1' : {'name':'bob', 'place':'lawn', 'animal':'man'},
#               'd2' : {'name':'spot', 'place':'bed', 'animal':'dog'}}



def print_collection(collection):
    print(ascii_top)
    for key, entry in collection.items():
        artist = entry.get("artist")
        album = entry.get("album")
        year = entry.get("release_year")
        genre = entry.get("genre")
        album_length = entry.get("length")
        
        space1 = fill(artist, 24, " ")
        space2 = fill(album, 30, " ")
        space3 = fill(year, 8, " ")
        space4 = fill(genre, 20, " ")
        space5 = fill(album_length, 10, " ")

        print(f"\t█▒ {artist}{space1}{album}{space2}{year}{space3}{genre}{space4}{album_length} █▒")
    print(ascii_bottom)


if __name__ == "__main__":
    collection = {
    "klucz": 
        {
        "artist" : "Pink Floyd",
        "album" : "The Dark Side Of The Moon",
        "release_year" : "1973",
        "genre" : "progressive rock",
        "length" : "43:00"
        },
    "klucz2":
        {
        "artist" : "Britney Spears",
        "album" : "Baby One More Time",
        "release_year" : "1999",
        "genre" : "pop",
        "length" : "42:20"
        }
    }

    print_collection(collection)
