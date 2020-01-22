# import display 
from display import print_collection, print_options

def add_to_collection(collection, new_item):
    
    item_information = {
         "artist" : new_item[0],
         "album" : new_item[1],
         "release_year" : new_item[2],
         "genre" : new_item[3],
         "length" : new_item[4]
    }

    item_index = len(collection.keys()) + 1
    collection.update({str(item_index) : item_information})

def import_collection(collection, filename="text_albums_data.txt"):

    try:
        with open(filename) as collection_file:
            for line in collection_file:
                new_item = line.split(',')
                new_item[-1] = new_item[-1].rstrip('\n')
                add_to_collection(collection,new_item)
    except:
        print(f"File '{filename}' not found!")

def export_collection(collection, filename="export_collection.csv"):

    export_items = ""

    for key in collection:
        export_items += (f'{key},' * collection.get(key))

    try:
        with open(filename, "w") as collection_file:
            collection_file.write(export_items.rstrip(','))
    except:
        print(f"You don't have permission creating file '/nopermission.csv'!")

def find_in_collection(category = "", search_word = "", input_question = "\n\tPlease insert search term: "):
    if not category:
        category = input("\n\tPlease insert category you want to search for (artist, album, year, genre, length): ")
    if not search_word:
        search_word = input(input_question)

    if category == "release_year":
        year = search_word.split("-")

    search_results = {}
    for key in collection:
        compare_word = collection[str(key)][category]
        if compare_word.lower() == search_word.lower():
            search_results.update({key : collection[key]})
        
    print_collection(search_results)

def get_input():
    choice = input("\n\tChoose whatcha ya gonna do now: ")

    if choice == "1":
        print_collection(collection)
    elif choice == "2":
        find_in_collection("genre")
    elif choice == "3":
        find_in_collection("release_year", "", "Please specify time range in years, example \"1998-2002\" ")
    elif choice == "4":
        pass
    elif choice == "5":
        find_in_collection("artist")
    elif choice == "6":
        find_in_collection("album")
    elif choice == "7":
        pass

    # def f(x):
    #     return {
    #         'a': 1,
    #         'b': 2
    #     }.get(x, 9)

def sort_collection(category, order):

    sorting_results = {}

    if category == "release_year":
        sort_collection = sorted(collection, key=lambda x: int(collection[x]["release_year"]), reverse=True)
    elif category == "length":
        sort_collection = sorted(collection, key=lambda x: int(collection[x]["length"].replace(':','')), reverse=True)
    else:
        sort_collection = sorted(collection, key=lambda x: str(collection[x][category].lower()), reverse=True)
    
    for key in sort_collection:
        sorting_results.update({key : collection[key]})
        
    print_collection(sorting_results) 

if __name__ == "__main__":
    collection = {}
    import_collection(collection)
    #test = collection["10"]["genre"]
    #print(test)
    sort_collection("artist","desc")
    sort_collection("album","desc")
    sort_collection("release_year","desc")
    sort_collection("genre","desc")
    sort_collection("length","desc")
    print_collection(collection)

    #find_in_collection()
    #find_in_collection("artist","Pink Floyd")
    
    print_options()
    get_input()
    #choice = input("\n\tChoose whatcha ya gonna do now")
