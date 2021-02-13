'''
    In this case study, we develop a program that computes the Flesch Index for a text file. 
    In 1949, Dr. Rudolf Flesch published The Art of Readable Writing,
    in which he proposed a measure of text readability known as the Flesch Index. 

    Write a program that computes the Flesch Index and grade level for text stored in a text file.

    Word - Any sequence of non-whitespace characters.
    Sentence - Any sequence of words ending in a period, question mark, exclamation point, colon, or semicolon.
    Syllable - Any word of three characters or less; or any vowel (a, e, i, o, u) or pair of consecutive vowels, 
            except for a final -es, -ed, or -e that is not -le.

    This program will perform the following tasks:
    1. Receive the filename from the user, open the file for input, and input the text.
    2. Count the sentences in the text.
    3. Count the words in the text.
    4. Count the syllables in the text.
    5. Compute the Flesch Index.
    6. Compute the Grade Level Equivalent.
    7. Print these two values with the appropriate labels, as well as the counts from tasks 2–4.

    Flesch’s formula to calculate the index F is the following:

    F = 206.835 - 1.015  × ( words / sentences) − 84.6 × (syllables / words)

    The Flesch-Kincaid Grade Level Formula is used to compute the Equivalent Grade Level G:

    G = 0.39 × ( words / sentences) + 11.8  ×  (syllables/words) − 15.59
'''

fileName = input("enter the filename : ")
inputfile = open(fileName)
text = inputfile.read()

sentences = text.count('.') + text.count('?') + text.count(':') + text.count(';') + text.count('!')

words = len(text.split())

syllables = 0
vowels = "aeiouAEIOU"

for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)

    for ending in ['es','ed','e']:
        if word.endswith(ending):
            syllables -= 1

    if word.endswith('le'):
        syllables += 1
    
    if len(word) <= 3:
        syllables += 1

index = 206.835 - 1.015  * ( words / sentences) - 84.6 * (syllables / words)

level = round(0.39 * ( words / sentences) + 11.8  *  (syllables / words) - 15.59)


print("The Flesch index is : %0.2f" % index)
print("The grade level is : ", level)
print("Sentences", sentences)
print("words", words)
print("syllables", syllables)