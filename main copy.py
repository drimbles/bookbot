def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    #print(file_contents)
 def get_word_count(file_contents):
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    print(f"Found {word_count} total words")



main()

