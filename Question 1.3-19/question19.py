### Question 19
# count_words.py

import operations

def count_word_occurrences():
    file_path = 'paragraph.txt'
    word_count = {}
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower().strip('.,!?;"\'()[]{}')  # Normalize words to lowercase and remove punctuation
                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")
    
    # Sort the word count dictionary by word (alphabetically)
    sorted_word_count = dict(sorted(word_count.items()))
    
    for word, count in sorted_word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    count_word_occurrences()
