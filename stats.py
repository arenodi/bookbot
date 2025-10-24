def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())

def get_num_char(text):

    char_dict = {}

    for word in text.split():
        characters = list(word)
        for char in characters:
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1

    return char_dict

def sort_on(char_dict):
    return char_dict["num"]

def get_sorted_dict(dictionary):
    
    dict_list = [{"char": key, "num": value} for key, value in dictionary.items()]
    dict_list.sort(key=sort_on, reverse=True)

    return dict_list
    

