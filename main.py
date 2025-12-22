def main():
    path_to_file = "/home/alex/workspace/github.com/boot.dev/bookbot/books/frankenstein.txt"
    print(get_book_text(path_to_file))

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    print(file_contents)

main()