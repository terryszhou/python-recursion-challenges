'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"

input: reverse("computer")
output: "computer"
'''
# # NON-RECURSIVE SOLUTION
def reverse_string(s):
    return s[::-1]

# RECURSIVE SOLUTION
def reverse_string(s):

    if len(s) == 0:
        return ""

    return s[-1] + reverse_string(s[:-1])

print(reverse_string("computer"))