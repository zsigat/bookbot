import sys
from stats import get_word_count, get_char_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = args[1] #"books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    word_count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    sorted_dict = sort_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for elem in sorted_dict:
        if elem["char"].isalpha():
            print(f"{elem['char']}: {elem['num']}")
        else:
            continue
    print("============= END ===============")

main()