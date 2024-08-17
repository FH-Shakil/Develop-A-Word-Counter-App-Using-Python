def count_words(text):
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

def count_words_from_input():
    text = input("Enter some text: ")
    word_count = count_words(text)
    
    for word, count in word_count.items():
        print(f"{word}: {count}")

def count_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            word_count = count_words(text)
            
            for word, count in word_count.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")


if __name__ == "__main__":
    count_words_from_input()
    file_path = 'input.txt' 
    count_words_from_file(file_path)
