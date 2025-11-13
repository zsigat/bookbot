def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):
    word_list = book.split()
    return len(word_list)

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(file_contents)
    print(f"Found {word_count} total words")

main()