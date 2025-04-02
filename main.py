def main():
    
    from stats import get_num_words
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = count_character_frequency(text)
    print_report(book_path, num_words, chars_dict)


        
def count_character_frequency(text):        
        freq = {}
        for c in text:
            lowered = c.lower()
            if lowered in freq:
                freq[lowered] += 1
            else:
                freq[lowered] = 1
        return(freq)  

def sort_on(dict):
    return dict["num"]  

def print_report(path, num_words, char_dict):
    print(f"--- Begin report of {path} ---")    
    print(f"{num_words} words found in the document\n")    

    chars_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": count}) 

    chars_list.sort(reverse=True, key=sort_on)

    for char_info in chars_list:
        print(f"The '{char_info['char']}' character was found {char_info['num']} times")        

def get_book_text(path):
    with open(path) as f:
        return f.read()   

main() 



    