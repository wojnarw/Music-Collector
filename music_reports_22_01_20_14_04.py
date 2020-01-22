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

def find_in_collection(category = "", search_word = ""):
    if not category:
        category = input("\n\tPlease insert category you want to search for (artist, album, year, genre, length): ")
    if not search_word:
        search_word = input("\n\tPlease insert search term: ")

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
        pass
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

# git pull - zwroci blad
# git stash (kopiuje do schowka wszystkie zmiany)
# git pull origin master
# git stash pop
# konfllikty i ich rozwiazanie
# mamy wspolny kod i ta sama wersje na galezi master
# git pull
# git checkout -b sort_collection_by_name
# git checkout -b find_in_collection

def sort_collection(category, order):

    sorting_results = {}

    if order == "desc":
        reverse = True
    elif order == "asc":
        reverse = False

    if category == "release_year":
        sort_collection = sorted(collection, key=lambda x: int(collection[x]["release_year"]), reverse=reverse)
    elif category == "length":
        sort_collection = sorted(collection, key=lambda x: int(collection[x]["length"].replace(':','')), reverse=reverse)
    else:
        sort_collection = sorted(collection, key=lambda x: str(collection[x][category].lower()), reverse=reverse)
    
    for key in sort_collection:
        sorting_results.update({key : collection[key]})
        
    print_collection(sorting_results) 

if __name__ == "__main__":
    collection = {}
    import_collection(collection)
    #test = collection["10"]["genre"]
    #print(test)
    sort_collection("artist","desc")
    sort_collection("album","asc")
    sort_collection("release_year","asc")
    sort_collection("genre","desc")
    sort_collection("length","asc")
    print_collection(collection)

    #find_in_collection()
    #find_in_collection("artist","Pink Floyd")
    
    print_options()
    get_input()
    #choice = input("\n\tChoose whatcha ya gonna do now")
