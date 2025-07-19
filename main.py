#

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    path = 'books/frankenstein.txt'
    book_text = get_book_text(path)
    return(book_text)

from stats import word_count
from stats import char_count

main()
word_count(main())
char_count(main())