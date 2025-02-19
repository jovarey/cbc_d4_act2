def longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

sentence = input("Enter a Sentence:")

print("Longest word:", longest_word(sentence))