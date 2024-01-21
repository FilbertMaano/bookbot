def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_dict = get_chars_dict(book_text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for char in sorted(chars_dict):
        if char.isalpha():
            num = chars_dict[char]
            print(f"The {char} character was found {num} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        char = char.lower()
        chars[char] = chars.get(char, 0) + 1

    return chars

if __name__ == "__main__":
    main()