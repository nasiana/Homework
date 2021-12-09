"""
Create required phrase.
----------------------
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate the required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.
NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.
FOR EXAMPLE:
    characters = "cbacba"
    phrase = "aabbccc"
    In this case you CANNOT create required phrase, because you are 1 character short!
IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.
    You can always generate an empty string.
"""

'''
How Python's FIND works:
Python's find method returns an integer.
This integer is essentially the index of the beginning of the substring if the substring exists, otherwise -1 is returned.
'''

def generate_phrase(characters, phrase):
    # left basicially no time to do this lol so rewrite this in xmas holidays but a more efficient method which is less computationally expensive
    unique_char = ''.join(set(characters))
    unique_phrase = ''.join(set(phrase))
    if len(unique_char) < len(unique_phrase):
        return False
    else:
        if characters.find(phrase) != -1:
            return True
        return False

'''
How Python's IN operator works:
The in operator returns True when the substring exists in the string.
Otherwise, it returns false.
'''

def generate_phrase_2(characters, phrase):
    unique_char = ''.join(set(characters))
    unique_phrase = ''.join(set(phrase))
    if len(unique_char) < len(unique_phrase):
        return False
    else:
        if phrase in characters:
            return True
        return False


# characters = "cbacba"
# phrase = "aabbccc"
# print(generate_phrase(characters, phrase))
# print(generate_phrase_2(characters, phrase))

# characters = "nasianahmed"
# phrase = "nasian"
# print(generate_phrase(characters, phrase))
# print(generate_phrase_2(characters, phrase))