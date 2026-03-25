# Chapter 9. Reading a file and writing to a file


# open a file in the same directory
# fin is a common name for a file object used for input
# file object methods: readline: gets only one sequential line
file_name = "words.txt"
# strip is a string method to eliminate a new line character
# ln = fin.readline().strip()

def print_words_with_length_more_than_20(file):
    fin = open(file)

    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

print_words_with_length_more_than_20(file_name)