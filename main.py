from stats import word_counter

def main():
    file = "/home/alex/workspace/github.com/boot.dev/bookbot/books/frankenstein.txt"
    file_contents = get_book_text(file)
    words_count = word_counter(file_contents)
    print(f"Found {words_count} total words")

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


main()