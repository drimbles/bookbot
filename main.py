import sys
#print(sys.argv)
arg_num = len(sys.argv)
#print(arg_num)
if arg_num != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import get_num_words, get_num_chars, sort_chars
def main():
    book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_num_chars(text)
    print(f"Found {num_words} total words")
    sorted_chars = sort_chars(char_counts)
    for item in sorted_chars:
        char = item["char"]
        num = item ["num"]
        if char.isalpha():
            print(f"{char}: {num}")
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

