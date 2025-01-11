def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(text)
    print(f"{num_words} words found in the document")
    print(letter_count(text))

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def letter_count(text):
    text = text.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    counts = {}
    for letter in letters:
        counts[letter] = text.count(letter)
    return counts
    
main()