def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_num = get_words_num(text)
    char_nums = get_char_num(text) 
    print(f"There are {words_num} found in the text")
    print(char_nums)

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
    

    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()