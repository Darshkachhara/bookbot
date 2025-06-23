def get_num_words(text):
    word_list = text.split()
    return f"Found {len(word_list)} total words"
def get_num_characters(text):
    text = text.lower()
    ans = dict()
    for char in text:
        if char in ans:
            ans[char]+=1
        else:
            ans[char]=1
    return ans
def sort_key(items):
    return items["num"]
def sort_num_characters(dic):
    lis = [{"char":key, "num":value} for key,value in dic.items()]
    return sorted(lis,reverse = True, key = sort_key)
