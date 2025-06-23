from stats import get_num_words,get_num_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    name = "/Users/darshkachhara/webflyx/bookbot/books/frankenstein.txt"    
    text = get_book_text(name)
    print(get_num_words(text))
    print(get_num_characters(text))

main()