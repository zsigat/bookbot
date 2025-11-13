def get_word_count(book):
    word_list = book.split()
    return len(word_list)

def get_char_count(book):
    char_count = {}
    for char in book:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    return char_count
        