def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = get_words_num(text)
    char_nums = get_char_num(text)
    listed_char_dict = sort_char_dict(char_nums)
    # print(f"There are {words_num} found in the text")
    # print(char_nums)
    print(f"--- Being report of {book_path} ---")
    print(f"There are {words_num} found in the text")
    for entry in listed_char_dict:
        print(f"{entry['char']}: {entry['num']}")


def get_words_num(text):
    words = text.split()
    return len(words)


def get_char_num(text):
    char_dict = {}        
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict
    
def sort_char_dict(char_dict):
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    char_list.sort(reverse = True, key = lambda x: x["num"])
    return char_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()