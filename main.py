from stats import word_count
from stats import char_count
from stats import sort_count
import sys

def get_book_text(path_file):
    with open(path_file) as f:
        file_txt = f.read()
    return file_txt


def main():
    input = sys.argv
    if len(input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = (input[1])
        text = get_book_text(book)
        wordcount = word_count(text)
        chara = char_count(text)
        sorted = sort_count(chara)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for i in sorted:
            if i[0].isalpha():
                print(f"{i[0]}: {i[1]}")
        print("============= END ===============")

main()