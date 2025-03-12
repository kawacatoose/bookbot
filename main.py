from stats import get_word_count
from stats import count_letters
from stats import sort_dict
import sys


def main():
    try:
        sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookpath = sys.argv[1]
    text = get_book_text(bookpath)
    word_count = get_word_count(text)
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count --------")
    letter_count = count_letters(text)
    sorted_list = sort_dict(letter_count)
    for key_pair in sorted_list:
        letter = key_pair["letter"]
        count = key_pair["count"]
        if letter.isalpha():
            print(f"{letter}: {count}")
    



def get_book_text(path):
    with open(path) as f:
        return f.read()
        

main()