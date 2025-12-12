def count_words(book_contents):
    all_words = book_contents.split()
    return len(all_words)

def count_chars(book_contents):
    char_counts = {}

    for c in book_contents:
        lowered = c.lower()
        if lowered in char_counts:
            char_counts[lowered] += 1
        else:
            char_counts[lowered] = 1
    return char_counts

def sort_dict(items):
    return items["num"]
