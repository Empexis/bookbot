
def word_count(book_text):
    count = len(book_text.split())
    return count

def char_count(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_char_dict(char_dict):
    listed_chars = list(char_dict.items())
    def sort_on(item):
        return item[1]
    listed_chars.sort(reverse=True, key=sort_on)
    new_list = [{"char": key, "num": value} for key, value in listed_chars]
    return new_list