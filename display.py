ascii_top = """
\t█████████████████████████████████████████████████████████████████████████████████████████████
\t█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒
\t█▒                                                                                          █▒
\t█▒ ARTIST NAME             ALBUM NAME                    YEAR    GENRE               LENGTH █▒
\t█▒                                                                                          █▒"""

ascii_bottom = """\
\t█▒                                                                                          █▒
\t█████████████████████████████████████████████████████████████████████████████████████████████▒
\t ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

#check how many spaces we need to make columns straight
def fill (check_for_length, total_length, filler):
    space = ""
    for i in range(len(check_for_length), total_length):
        space += filler
    return space

# dict_names = {'d1' : {'name':'bob', 'place':'lawn', 'animal':'man'},
#               'd2' : {'name':'spot', 'place':'bed', 'animal':'dog'}}



def print_collection(collection, title="", count_results=""):
    print(f"\n\t {title}")
    if count_results != "":
        print(f"\t Results: {count_results}")

    print(ascii_top)
    for key, entry in collection.items():
        artist = entry.get("artist")[0:23]
        album = entry.get("album")[0:29]
        year = entry.get("release_year")[0:7]
        genre = entry.get("genre")[0:19]
        album_length = entry.get("length")[0:6]     
        space1 = fill(artist, 24, " ")
        space2 = fill(album, 30, " ")
        space3 = fill(year, 8, " ")
        space4 = fill(genre, 20, " ")
        space5 = fill(album_length, 6, " ")

        print(f"\t█▒ {artist}{space1}{album}{space2}{year}{space3}{genre}{space4}{space5}{album_length} █▒")
    print(ascii_bottom)

def print_options():
    print("""Music Collector \n\n\
  ok    1 - As a user I want to view all imported albums
  ok    2 - As a user I want to find all albums by genre
        3 - As a user I want to find all albums from given time range
  ok    4 - As a user I want to find shortest/longest album
  ok    5 - As a user I want to find all albums created by given artist
  ok    6 - As a user I want to find album by album name
        7 - As a user I want to get full report in form of set of given statistics (longest album, 
            shortest album, oldest album, youngest album, all albums count + additional info, how many albums are given the genres)
        ELSE - exit""")

if __name__ == "__main__":
    collection = {
    "klucz": 
        {
        "artist" : "Pink Floyd",
        "album" : "The Dark Side Of The MoonMoonMoonMoonMoonMoonMoonMoon",
        "release_year" : "1973",
        "genre" : "progressive rock",
        "length" : "43:00"
        },
    "klucz2":
        {
        "artist" : "Britney SpearsSpearsSpearsSpearsSpearsSpears",
        "album" : "Baby One More Time",
        "release_year" : "199919991999",
        "genre" : "poppoppoppoppoppoppoppop",
        "length" : "123:20:20:20:20:20:20:20:20"
        }
    }

    print_collection(collection)
