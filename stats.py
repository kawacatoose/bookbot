def get_word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    lowercase_text = text.lower()
    for letter in lowercase_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    list = []    
    for letter in dict:
        list.append({"letter": letter, "count": dict[letter]})
    list.sort(reverse=True, key=sort_on)
    return list
    