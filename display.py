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

report_top = """
\t█████████████████████████████████████████████████████████████████████████████████████████████
\t█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒
\t█▒                                                                                          █▒
\t█▒ MUSIC COLLECTOR                                                                          █▒
\t█▒                                                                                          █▒
\t█▒ FULL REPORT                                                                              █▒
\t█▒                                                                                          █▒"""

reaport_bottom = """\
\t█▒                                                                                          █▒
\t█████████████████████████████████████████████████████████████████████████████████████████████▒
\t ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

program_top = """
\t█████████████████████████████████████████████████████████████████████████████████████████████
\t█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒
\t█▒                                                                                          █▒
\t█▒ MUSIC COLLECTOR                                                                          █▒
\t█▒                                                                                          █▒"""

program_bottom = """\
\t█▒                                                                                          █▒
\t█████████████████████████████████████████████████████████████████████████████████████████████▒
\t ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""

#check how many spaces we need to make columns straight
def fill (check_for_length, total_length, filler):
    space = ""
    for i in range(len(check_for_length), total_length):
        space += filler
    return space


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
    print("\n")


def print_options():
    print(program_top)
    print(program_bottom)
    print("\n")    
    print("\t1 - View all albums")
    print("\t2 - Find all albums by genre")
    print("\t3 - Find all albums from given time range")
    print("\t4 - Find shortest/longest album")
    print("\t5 - Find all albums created by given artist")
    print("\t6 - Find album by album name")
    print("\t7 - Full report")
    print("\t8 - Save to file")


def additional_info(albums, odlest_album, youngest_album, genres, total_length):
    print(report_top)
    print(reaport_bottom)
    print("\n")
    print(f"\tAlbums: {albums}")
    print(f"\tRelease years: {odlest_album}-{youngest_album}")
    print(f"\tGenres: {genres}")
    print(f"\tTotal length: {total_length}")
    print("\n")
