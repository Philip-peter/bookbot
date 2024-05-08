def get_text():
    with open("/home/ppeter/workspace/github.com/philip-peter/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def number_of_words():
    texts = get_text()
    split_words = texts.split()
    count = 0
    for words in split_words:
        count += 1
    return count

def count_letters():
    letters_dict = {}
    fetch_text = get_text()
    split_fetched_text = fetch_text.split()

    for word in split_fetched_text:
        word = word.lower()
        for letter in word:
            if letter in letters_dict.keys() and letter.isalpha():
                letters_dict[letter] +=  1
            elif letter not in letters_dict.keys() and letter.isalpha():
                letters_dict[letter] = 1

    #sort dictionary
    sorted_list = dict(sorted(letters_dict.items(), reverse=True, key=lambda item:item[1]))

    for i in sorted_list:
        print(f"The {i} character was found {letters_dict[i]} times")

def main():
    text = get_text()
    #print(text)
    print()
    print("---Begin report of books/frankenstein.txt---")
    print("Total number of words is ", number_of_words())
    print()
    print(count_letters())
    print("---End of Report---")

if __name__ == "__main__":
    main()
