def get_num_words(text):
    word_list = text.split()
    return f"{len(word_list)} words found in the document"
def get_num_characters(text):
    text = text.lower()
    ans = dict()
    for char in text:
        if char in ans:
            ans[char]+=1
        else:
            ans[char]=1
    return ans