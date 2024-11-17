def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)

    print(f"--- Begin report of {path} ---")
    print(f'{count_words(text)} words found in the document')

    for char, count in count_chars(text).items():
        print(f'The {char} character: was found {count} times')

    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1

    return char_count

main()