#read book
def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
        return book_contents

#analyze book
from stats import count_words, count_chars, sort_on, sort_char


def main():
    file_path = "books/frankenstein.txt"
    book_contents = get_book_text(file_path)
    num_words = count_words(book_contents)
    char_count = count_chars(book_contents)
    sort_char_count = sort_char(char_count)
    return file_path, num_words, char_count, sort_char_count

def print_report(file_path, num_words, sort_char_count):
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {file_path}")
    
    print("--------- Word Count --------")
    print(f"Found {num_words} total words")

    print("------ Character Count ------")
    for char, count in sort_char_count.items():
        print(f"{char}: {count}")
    
    print("============ END ============")

file_path, num_words, char_count, sort_char_count = main()    
print_report(file_path, num_words, sort_char_count)