from display import print_collection, print_options, additional_info


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
        print(f"\tFile {filename} saved.")
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

    search_results = {}  # Dictionary for find results
    count_results = 0  # Sum of results

    for key in collection:
        compare_word = collection[str(key)][category]
        if compare_word.lower() == search_word.lower():
            search_results.update({key: collection[key]})

    count_results = len(search_results)  # Sum of results
    # Title for table
    title = f"Find by: {category.replace('_',' ').title()}, {search_word}"
    # Printing table with result
    print_collection(search_results, title, count_results)
    return count_results


def sort_collection(category, order, album_length):

    sorting_results = {}  # Dic for sorting results

    # Set ASC or DESC order
    if order == "desc":
        reverse = True
    elif order == "asc":
        reverse = False

    # Sort by category
    if category == "release_year": #Sorting years by int
        sort_collection = sorted(collection, key=lambda x: int(
            collection[x]["release_year"]), reverse=reverse) #All elements of sorting results
        if album_length == "oldest":
            sort_collection = [sort_collection[0]] #First element of sorting results
            category = "Oldest album"
        if album_length == "youngest":
            sort_collection = [sort_collection[-1]] #Last element of sorting results
            category = "Youngest album"
    elif category == "length": #Sorting length by int
        sort_collection = sorted(collection, key=lambda x: int(
            collection[x]["length"].replace(':', '')), reverse=reverse) #All elements of sorting results
        if album_length == "shortest":
            sort_collection = [sort_collection[0]] #First element of sorting results
            category = "Shortest album"
        if album_length == "longest":
            sort_collection = [sort_collection[-1]] #Last element of sorting results
            category = "Longest album"
    else:  #Sorting artists, albums and genres by string
        sort_collection = sorted(collection, key=lambda x: str(
            collection[x][category].lower()), reverse=reverse) #All elements of sorting results

    # Writing results to dictionary
    for key in sort_collection:
        sorting_results.update({key: collection[key]})

    # Title for table
    title = f"Sorted by: {category.replace('_',' ').title()}"

    #Printing sorting results
    print_collection(sorting_results, title)


def generate_report():
    # Sorting by release year ASC and finding oldest and youngest album
    sort_years_release = sorted(collection, key=lambda x: int(
        collection[x]["release_year"]), reverse=False)
    oldest_album = collection[sort_years_release[0]]['release_year']  # First element od dic
    youngest_album = collection[sort_years_release[-1]]['release_year']  # Last element of dic

    # Summary of all albums
    albums = len(collection)

    # Making set of all genres and counting total for length of all albums
    genres_set = set()
    total_length = 0.00

    for key in range(1, albums):
        genres_set.add(collection[str(key)]['genre'])  # Add to genres set
        # Add to summary of length, converting to float
        total_length += float(collection[str(key)]['length'].replace(':', '.'))

    # Printing table with all aditionnal ifno
    additional_info(albums, oldest_album, youngest_album, str(
        genres_set)[1:-1], str(total_length).replace('.', ':'))

    # Printing how many albums have each genre
    for genre in genres_set:
        find_in_collection("genre", genre, "")

    # Printing oldest and youngest album
    sort_collection("release_year", "asc", "oldest")
    sort_collection("release_year", "asc", "youngest")

    # Printing shortest and longest album
    sort_collection("length", "asc", "shortest")
    sort_collection("length", "asc", "longest")


def get_input():
    choice = input("\n\tChoose whatcha ya gonna do now: ")

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
    elif choice == "8":
        export_collection(collection)


if __name__ == "__main__":
    collection = {}
    import_collection(collection)
    print_options()
    get_input()
