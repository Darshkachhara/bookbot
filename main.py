from stats import get_num_words
from stats import get_num_characters
from stats import sort_num_characters,sort_key


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def report(name):
    text = get_book_text(name)
    print("="*12+"BOOKBOT"+"="*12)
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    dic = get_num_characters(text)
    arr = sort_num_characters(dic)
    print("--------- Character Count -------")
    for l in arr:
        if l['char'].isalpha():
            print(f"{l['char']}: {l['num']}")

    print("============= END ===============")

def main():
    name = "/Users/darshkachhara/webflyx/bookbot/books/frankenstein.txt"    
    # text = get_book_text(name)
    # print(get_num_words(text))
    # print(get_num_characters(text))
    report(name)

main()