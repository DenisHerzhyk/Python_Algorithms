def dict_our_list(string:str):
    new_dict = {}
    string = string.lower().split()

    for word in string:
        new_dict[word.lower()] = string.count(word)
    return new_dict

