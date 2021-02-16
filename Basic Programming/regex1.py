# Check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
def check_string(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(check_string("Vibhushit030699")) 
print(check_string("abc90!@#$%"))