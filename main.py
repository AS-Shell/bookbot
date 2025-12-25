from stats import word_counter
from stats import count_characters
from stats import char_list
from stats import sort_list

def main():
    file = "books/frankenstein.txt"
    file_contents = get_book_text(file)
    words_count = word_counter(file_contents)
    characters_dic = count_characters(file_contents)
    character_list = char_list(characters_dic)


    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {file}...")
    print ("----------- Word Count ----------")
    print (f"Found {words_count} total words")
    print ("--------- Character Count -------")
    character_list.sort(reverse=True, key=sort_list)
    for item in character_list:
        k = item["char"]
        v = item["num"]
        print(f"{k}: {v}")
    print ("============= END ===============")


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


main()