#read book
def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
        return book_contents

#analyze book
from stats import count_words, count_chars, sort_dict

def main():
    file_path = "books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    num_words = count_words(book_contents)
    char_count = count_chars(book_contents)
    print(f"Found {num_words} total words")
    char_count.sort(reverse = True, key = sort_dict)
main()