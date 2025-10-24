import sys
from stats import get_book_text, get_num_words, get_num_char, get_sorted_dict

def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = arguments[1]

    print(
            "============ BOOKBOT ============",
            f"Analyzing book found at {filepath}...",
            sep="\n"
        )
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    print(
            "----------- Word Count ----------", 
            f"Found {num_words} total words",
            sep="\n"
            )

    char_dict = get_num_char(book_text)
    char_dict_list = get_sorted_dict(char_dict)

    print("--------- Character Count -------")
    
    for char in char_dict_list:
        
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")


main()

