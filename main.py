#functional code for bookbot
def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    path = 'books/frankenstein.txt'
    book_text = get_book_text(path)
    return(book_text)

#imports from stats.py
from stats import word_count
from stats import char_count
from stats import sort_char_dict

#the output
def report():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    book_data = main()
    print(f"Found {word_count(book_data)} total words.")
    print("---------- Character Count -------")
    for char in sort_char_dict(char_count(book_data)):
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ==============")

report()