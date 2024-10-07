import re

phoneNumberregex = re.compile(r'\+\d\d-\d{10}')
# re.compile Defines the type of string we want to look for

mo = phoneNumberregex.search('My Number is +91-9769218137.')
#search - Whatever string gets passed through search(), search function searches
# for the regex pattern passed into compile()
# RESULT of the search() is stored in mo and group() just groups up all the matches

print('Phone number found: ' + mo.group())
#The mo variable name is just a generic name to use for match objects.
#group - returns the chunk of string that matched the initial regex pattern

sample_array = re.compile(r'ab+(ab)+a')

# For a sample of 
# abababababababab
# abbbbbbbb
# aaaaaa bbbbbbbbbbb
# abbbababa, abababa, abbababa 
# abbbbababa 
# aababa
sample = sample_array.search("abbabbaba ")
print(sample.group())