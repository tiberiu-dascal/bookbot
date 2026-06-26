from stats import get_num_words, characters_count


def get_book_text(file_path):

    book_content: str = ""
    with open(file_path) as f:
        book_content = f.read()

    return book_content


def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    w_count = get_num_words(frankenstein_text)
    chars_counter = characters_count(frankenstein_text)
    print(f"Found {w_count} total words.")
    print(chars_counter)


main()
