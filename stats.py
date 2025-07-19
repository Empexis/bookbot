
def word_count(book_text):
    count = len(book_text.split())
    print(f"{count} words found in the document.")

def char_count(book_text):
    
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(f"Character counts: {char_dict}")