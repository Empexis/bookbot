#imports
import sys
from stats import word_count
from stats import char_count
from stats import sort_char_dict

#functional code for bookbot
def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    return(path, book_text)

#the output
def report(path, book_text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words.")
    print("---------- Character Count -------")
    for char in sort_char_dict(char_count(book_text)):
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ==============")


path, book_text = main()
report(path, book_text)