import random
import json
import os

def get_recipe(book):
    book_title = book["title"]

    if len(book["recipes-pages-list"]) == 0:
        repice_page = random.randint(book["recipes-interval"]["first_page"],
                                     book["recipes-interval"]["last_page"]
                                    )

    else:
        repice_page = book["recipes-pages-list"][random.randint(0, len(book["recipes-pages-list"]))]

    return book_title, repice_page

def main ():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_dir, "books_list.json")

    with open(config_file_path, 'r') as f:
        config = json.load(f)

    books = config.get("books")
    i = random.randint(0, len(books)-1)

    print(get_recipe(books[i]))

if __name__ == "__main__":
    main()
