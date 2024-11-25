def main():
    book_path = "/home/ero/workspace/github.com/dekoniec/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    def sort_on(text):
        return text["count"]
    text.sort(reverse=True, key=sort_on)
    
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"77986 words found in the document")
    for i in text:
        print(f"The '{i.get("letter")}' character was found '{i.get("count")}'")
    print("--- End report ---")
            

    


def get_book_text(path):
    with open(path) as f:
        lowered_text = f.read().lower().lstrip()
        charDict = dict.fromkeys(lowered_text, 0)
        for c in lowered_text:
            if c.isalpha():
                charDict[c] += 1
            else:
                charDict.pop(c, None)
    char_list = [{'letter': k, 'count': co} for k, co in charDict.items()]
    return char_list
        
        




main()