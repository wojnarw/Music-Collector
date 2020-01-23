from display import print_collection, print_options


def add_to_collection(collection, new_item):

    item_information = {
        "artist": new_item[0],
        "album": new_item[1],
        "release_year": new_item[2],
        "genre": new_item[3],
        "length": new_item[4]
    }

    item_index = len(collection.keys()) + 1
    collection.update({str(item_index): item_information})


def import_collection(collection, filename="text_albums_data.txt"):

    try:
        with open(filename) as collection_file:
            for line in collection_file:
                new_item = line.split(',')
                new_item[-1] = new_item[-1].rstrip('\n')
                add_to_collection(collection, new_item)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_collection(collection, filename="export_collection.csv"):

    export_items = ""

    for key in collection:
        export_items += (f"{collection[key]['artist']},"
                         f"{collection[key]['album']},"
                         f"{collection[key]['release_year']},"
                         f"{collection[key]['genre']},"
                         f"{collection[key]['length']} \n")

    try:
        with open(filename, "w") as collection_file:
            collection_file.write(export_items)
    except FileNotFoundError:
        print(f"You don't have permission creating file '/nopermission.csv'!")


def find_in_collection(
    category="",
    search_word="",
    input_question="\n\tPlease insert search term: "
):
    if not category:
        category = input("\n\tPlease insert category you want to search for"
                         + " (artist, album, year, genre, length): "
                         )
    if not search_word:
        search_word = input(input_question)

    if category == "release_year":
        year = search_word.split("-")

    search_results = {}
    count_results = 0

    for key in collection:
        compare_word = collection[str(key)][category]
        if compare_word.lower() == search_word.lower():
            search_results.update({key: collection[key]})

    count_results = len(search_results)
    title = f"Find by: {category.replace('_',' ').title()}, {search_word}"
    print_collection(search_results, title, count_results)


def additional_info():

    albums = len(collection)
    sort_oldest_album = sort_collection("release_year", "asc", "oldest")
    oldest_album = collection[sort_oldest_album[0]]['release_year']

    sort_youngest_album = sort_collection("release_year", "asc", "youngest")
    youngest_album = collection[sort_youngest_album[-1]]['release_year']

    genres = set()

    for key in range(1, albums):
        genres.add(collection[str(key)]['genre'])

    print(f"Release years: {oldest_album} - {youngest_album}")
    print(f"Genres: {genres}")
    print(f"Total length: {albums}")


def sort_collection(category, order, album_length):

    sorting_results = {}

    if order == "desc":
        reverse = True
    elif order == "asc":
        reverse = False

    if category == "release_year":
        sort_collection = sorted(collection, key=lambda x: int(
            collection[x]["release_year"]), reverse=reverse)
        if album_length == "oldest":
            sort_collection = [sort_collection[0]]
            category = "Oldest album"
        if album_length == "youngest":
            sort_collection = [sort_collection[-1]]
            category = "Youngest album"
    elif category == "length":
        sort_collection = sorted(collection, key=lambda x: int(
            collection[x]["length"].replace(':', '')), reverse=reverse)
        if album_length == "shortest":
            sort_collection = [sort_collection[0]]
            category = "Shortest album"
        if album_length == "longest":
            sort_collection = [sort_collection[-1]]
            category = "Longest album"
    else:
        sort_collection = sorted(collection, key=lambda x: str(
            collection[x][category].lower()), reverse=reverse)

    for key in sort_collection:
        sorting_results.update({key: collection[key]})

    title = f"Sorted by: {category.replace('_',' ').title()}"
    print_collection(sorting_results, title)
    return sort_collection


def generate_report():
    additional_info()
    find_in_collection()
    sort_collection("release_year", "asc", "oldest")
    sort_collection("release_year", "asc", "youngest")
    sort_collection("length", "asc", "shortest")
    sort_collection("length", "asc", "longest")


def get_input():
    # choice = input("\n\tChoose whatcha ya gonna do now: ")
    choice = "7"
    if choice == "1":
        print_collection(collection)
    elif choice == "2":
        find_in_collection("genre")
    elif choice == "3":
        find_in_collection(
            "release_year",
            "",
            "Please specify time range in years, example \"1998-2002\" "
        )
    elif choice == "4":
        sort_collection("length", "asc", "shortest")
        sort_collection("length", "asc", "longest")
    elif choice == "5":
        find_in_collection("artist")
    elif choice == "6":
        find_in_collection("album")
    elif choice == "7":
        generate_report()


if __name__ == "__main__":
    collection = {}
    import_collection(collection)
    # print_collection(collection)
    # test = collection["10"]["genre"]
    # print(test)
    # sort_collection("artist","desc")
    # sort_collection("album","asc")
    # sort_collection("release_year","asc","")
    # sort_collection("release_year","asc", "oldest")
    # sort_collection("release_year","asc", "youngest")
    # sort_collection("genre","desc")
    # sort_collection("length","asc","")

    # export_collection(collection)

    # sort_collection("length","asc","shortest")
    # sort_collection("length","asc","longest")
    # print_collection(collection)

    # find_in_collection()
    # find_in_collection("genre","pop")

    # print_options()
    get_input()
