from stats import get_word_count, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(file_contents)
    print(f"Found {word_count} total words")
    char_count = get_char_count(file_contents)
    print(char_count)

main()