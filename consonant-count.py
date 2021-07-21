'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''

# NON-RECURSIVE SOLVE
def consonant_count(s):
    count = 0
    vowels =  ["a","e","i","o","u"]

    for i in s:
        if i.lower() not in vowels:
            count += 1

    answer = f"The word '{s}' contains {count} consonant"

    if count > 1: answer += "s" 

    return answer + "."

# RECURSIVE SOLVE
def consonant_count(s, count = 0):
    vowels =  ["a","e","i","o","u"]

    if len(s) == 0: 
        return count

    if s[0] not in vowels:
        count += 1

    return consonant_count(s[1:], count)



print(consonant_count("snakes"))