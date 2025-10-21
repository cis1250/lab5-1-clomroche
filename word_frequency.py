#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False
        
    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True
    
def get_sentence():
    user_sentence = input("Enter a sentence: ")
    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_input = input("Enter a sentence: ")
    return user_sentence

def calculate_frequencies(user_sentence):
    # Split the sentence into a clean list of lowercase words with no punctation
    words = user_sentence.strip('.').lower().split()
    # Create blank dictionary
    frequency = {}

    # Assign a value of zero to each unique word in the original sentence
    for word in words:
        if word not in frequency:
            frequency[word] = 0

    # For everytime a word appears in the original sentence, add a value to it
    for word in words:
        frequency[word] = frequency[word]+1
    return frequency

def print_frequencies(frequency):
    # Print out the dictionary
    print(frequency)
    
def main():
    user_sentence = get_sentence()
    word_frequencies = calculate_frequencies(user_sentence)
    print_frequencies(word_frequencies)
    
main()
