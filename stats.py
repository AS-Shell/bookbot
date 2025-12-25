def word_counter(file_contents):
    words = file_contents.split()
    counter = 0
    for word in words:
        counter +=1
    return counter

def count_characters(file_contents):
    lower_string = file_contents.lower()
    char = {}

    for string in lower_string:
        if string in char:
            char[string] += 1
        else : 
            char[string] = 1 
    return char

def char_list(characters_dic):
    list = []
    for key, value in characters_dic.items():
        if key.isalpha(): 
            list.append (
                {
                    "char" : key,
                    "num"  : value
                }
            )
    return list

def sort_list(character_list):
    return character_list["num"]