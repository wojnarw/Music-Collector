# import display 
from display import print_collection

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

    # try:
        with open(filename) as collection_file:
            for line in collection_file:
                new_item = line.split(',')
                new_item[-1] = new_item[-1].rstrip('\n')
                add_to_collection(collection,new_item)
    # except:
    #     print(f"File '{filename}' not found!")

def export_collection(collection, filename="export_collection.csv"):

    export_items = ""

    for key in collection:
        export_items += (f'{key},' * collection.get(key))

    try:
        with open(filename, "w") as collection_file:
            collection_file.write(export_items.rstrip(','))
    except:
        print(f"You don't have permission creating file '/nopermission.csv'!")

if __name__ == "__main__":
    collection = {}
    import_collection(collection)
    # print(collection)
    print_collection(collection)

