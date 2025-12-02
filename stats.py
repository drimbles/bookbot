def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    formatted_text = text.lower()
    char_count = {}
    for char in formatted_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_num(char_count):
    return char_count["num"]
def sort_chars(char_count):
    char_count_list=[]
    for k,v in char_count.items():
        char_count_list.append({"char": k, "num": v})
    char_count_list.sort(key=char_num, reverse=True)
    return char_count_list



