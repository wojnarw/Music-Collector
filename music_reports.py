import re, os
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


def import_collection(collection, filename):
    collection.clear()

    if not filename:
        filename = input("\tPlease enter filename you want to import, default is \"text_albums_data.txt\"\n\t")
        while not re.search("^[a-zA-Z0-9,]*[.][a-zA-Z0-9]{1,4}$", filename):
            filename = input("\tPlease enter correct filename, remember about file extension!\n\t")

    try:
        with open(filename) as collection_file:
            for line in collection_file:
                line = line.strip()
                new_item = line.split(',')
                add_to_collection(collection, new_item)
    except FileNotFoundError:
        input(f"\n\tFile '{filename}' not found!")


def export_collection(collection):

    filename = input("\tPlease enter filename you want to export, default is \"text_albums_data.txt\"\n\t")
    while not re.search("^[a-zA-Z0-9,]*[.][a-zA-Z0-9]{1,4}$", filename):
        filename = input("\tPlease enter correct filename, remember about file extension!\n\t")


    export_items = ""

    for key in collection:
        export_items += (f"{collection[key]['artist']},"
                         f"{collection[key]['album']},"
                         f"{collection[key]['release_year']},"
                         f"{collection[key]['genre']},"
                         f"{collection[key]['length']}\n")

    try:
        with open(filename, "w") as collection_file:
            collection_file.write(export_items)
        input(f"\n\tFile {filename} saved.")
        print_collection(collection, "", "", True)

    except FileNotFoundError:
        input(f"\n\tYou don't have permission creating file {filename}!")


def find_in_collection(
    category="",
    search_word="",
    input_question="\n\tPlease insert search term: ",
    clear_screen = "True"
):
    if not category:
        category = input("\n\tPlease insert category you want to search for"
                         + " (artist, album, year, genre, length): "
                         )
    if not search_word:
        search_word = input(input_question)

    years = []
    # Check if we are looking for a year or years range
    if category == "release_year":
        # REGEXP (^\d{3,4}-\d{3,4}$)|(^\d{3,4}$)
        # ^ starts with, $ ends with, | or, () group, {3,4} 3 or 4 repeats
        while not re.search("(^\d{3,4}-\d{3,4}$)|(^\d{3,4}$)", search_word):
            search_word = input(input_question)
        years = search_word.split("-")

        # if user entered reversed years order, switch variables
        if len(years) == 2 and int(years[0]) > int(years[1]):
            years[0], years[1] = years[1], years[0]

    search_results = {}  # Dictionary for find results
    count_results = 0  # Sum of results
    
    for key in collection:
        compare_word = collection[str(key)][category]

        # if user entered years range
        if len(years) == 2:
            if category == "release_year" and int(compare_word) >= int(years[0]) and int(compare_word) <= int(years[1]):
                search_results.update({key : collection[key]})
        # if user entered single year
        if category == "release_year" and int(compare_word) == int(years[0]) and len(years) == 1:
            search_results.update({key : collection[key]})
        # all other search phrases
        elif compare_word.lower() == search_word.lower():
            search_results.update({key : collection[key]})

    count_results = len(search_results)  # Sum of results
    # Title for table
    title = f"Find by: {category.replace('_',' ').title()}, {search_word}"
    # Printing table with result
    print_collection(search_results, title, count_results, clear_screen)
    return count_results


def sort_collection(category, order, album_length, clear_screen = False):

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
    print_collection(sorting_results, title, "", clear_screen)


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

    os.system('clear')
    # Printing how many albums have each genre
    for genre in genres_set:
        find_in_collection("genre", genre, "", False)

    # Printing oldest and youngest album
    sort_collection("release_year", "asc", "oldest")
    sort_collection("release_year", "asc", "youngest")

    # Printing shortest and longest album
    sort_collection("length", "asc", "shortest")
    sort_collection("length", "asc", "longest")


def add_album():

    new_entry = []
    # remove commas from inputs
    new_entry.append(input("\tPlease insert new artist name: ").replace(",",""))
    new_entry.append(input("\tPlease insert new album name: ").replace(",",""))

    # validate rest of inserted data
    new_release_year = input("\tPlease insert release year: ")
    while not re.search("^\d{3,4}$", new_release_year): # accept only 3 or 4 digits
        new_release_year = input("\tPlease insert full release year in digits only: ")
    new_entry.append(new_release_year)

    new_genre = input("\tPlease insert genre: ")
    while not new_genre.isalpha(): # accept only alphabet
        new_genre = input("\tPlease insert genre in letters only: ")
    new_entry.append(new_genre)

    new_length = input("\tPlease insert album length in format \"minutes:seconds\": ")
    while not re.search("^\d{1,4}:[0-5]\d$", new_length): # accept time format only
        new_length = input("\tPlease insert album length in format \"minutes:seconds\": ")
    new_entry.append(new_length)

    add_to_collection(collection, new_entry)
    input("\n\tADDED NEW ALBUM SUCCESFULLY! ")
    print_collection(collection, "", "", True)


def remove_album():
    print("\n\tREMOVING ALBUM")
    artist_name = input("\n\tPlease enter artist name: ")
    album_name = input("\tPlease enter album name: ")
    
    search_results = {}  # Dictionary for find results

    for key in collection:
        compare_word = collection[str(key)]["artist"]
        if compare_word.lower() == artist_name.lower():
            search_results.update({key : collection[key]})
    # if there were matches for artist
    if search_results:
        for key in search_results:
            compare_word = search_results[str(key)]["album"]
            if compare_word.lower() == album_name.lower():
                search_results.update({key : search_results[key]})
        print(search_results)
        del collection[next(iter(search_results))] 
    # if no results for given artist and album
    elif not search_results:
        print("\n\tThere were no matches. ")



def get_input():
    choice = input("\n\tChoose what do you want to do now: ")

    #ask for input again if it's not alphanumeric
    while not choice.isalnum():
        choice = input("\tPlease type a number from the list or \"exit\" to quit: ")

    if choice.lower() == "exit":
        return
    elif choice == "1":
        print_collection(collection, "", "", True)
    elif choice == "2":
        find_in_collection("genre")
    elif choice == "3":
        find_in_collection(
            "release_year",
            "",
            "\tPlease specify year or time range in years, example \"2010\" or \"1998-2002\": "
        )
    elif choice == "4":
        sort_collection("length", "asc", "shortest", True)
        sort_collection("length", "asc", "longest")
    elif choice == "5":
        find_in_collection("artist")
    elif choice == "6":
        find_in_collection("album")
    elif choice == "7":
        generate_report()
    elif choice == "8":
        add_album()
    elif choice == "9":
        remove_album()
    elif choice == "0":
        export_collection(collection)
    elif choice == "10":
        import_collection(collection, "")
        print_collection(collection, "", "", True)

    print_options()
    get_input()


if __name__ == "__main__":
    collection = {}
    import_collection(collection, "text_albums_data.txt")
    print_options(True)
    get_input()
