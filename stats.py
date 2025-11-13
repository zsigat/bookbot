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

def sort_on(items):
    return items["num"]

def sort_dict(char_count):
    sorted_dict = []
    for char in char_count:
        sorted_dict.append(
            {
                "char":char,
                "num":char_count[char]
            }
        )
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict