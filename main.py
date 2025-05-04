import sys

from stats import count_words, get_characters_counts, get_sorted_list_of_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")

    book_content = get_book_text(book_path)

    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")

    print(count_words(book_content))

    print("--------- Character Count -------")

    stats = get_characters_counts(book_content)
    sorted_stat_list = get_sorted_list_of_characters(stats)

    for stat in sorted_stat_list:
        if stat['char'].isalpha():
            print(f"{stat['char']}: {stat['num']}")

    print("============= END ===============")

main()