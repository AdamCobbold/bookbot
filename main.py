from stats import word_count
from stats import char_count

def get_book_text(path_file):
    with open(path_file) as f:
        file_txt = f.read()
    return file_txt


def main():
    frank_text = get_book_text("books/frankenstein.txt")
    wordcount = word_count(frank_text)
    print(f"{wordcount} words found in the document")
    print(char_count(frank_text))

main()