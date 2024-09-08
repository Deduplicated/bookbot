def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    print(f"Book has {word_count} words")
    character_counting(text)
    # (character_counting(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    return len(text.split())

def character_counting(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    sorting_letters = sort_on(char_count)
    for char, count in sorting_letters.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    return
    

def sort_on(char_count):
    sorted_dict = dict(sorted(char_count.items(),key =lambda item: item[1], reverse=True))
    return sorted_dict
# I am sorting by the count and making it reversed (i.e biggest to smallest)
main()
