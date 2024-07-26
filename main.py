def main():
    book = "books/frankenstein.txt"
    text = book_words(book)
    word_count = book_count(text)
    letter_dict = letter_count(text)
    report(letter_dict)

def book_count(book):
    words = book.split()
    return len(words)

def letter_count(book):
    l_count = {}

    words = book.split()
    for word in words:
        word = word.lower()
        for i in word:
            if i not in l_count:
                l_count[i] = 1
            else:
                l_count[i] += 1
    return l_count

def book_words(file):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def sort_on(dict):
    return dict["num"]

def report(book_dict):
    sorted_list = []

    for ch in book_dict:
        sorted_list.append({"char": ch, "num": book_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    print(sorted_list)

main()