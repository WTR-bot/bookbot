def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    letter_counts = letter_count(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for letter, count in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{letter}' character was found {count} times")
    
    print("--- End report ---")

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