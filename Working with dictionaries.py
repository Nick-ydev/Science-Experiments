'''
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
#DICTIONARIES ARE NOT ORDERED, THEY CANNOT BE SLICED LIKE LISTS.
'''

'''
The keys(), values(), and items() Methods
?VALUE()
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
...     print(v)

red
42
RETURNS VALUES from key:value pair

?KEYS()
>>> for k in spam.keys():
...     print(k)

color
age
RETURNS ALL KEYS in output.

''''''
Use the multiple assignment trick in a for loop to assign the key and value to separate variables.
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
...     print('Key: ' + k + ' Value: ' + str(v))

Key: age Value: 42
Key: color Value: red


The get() & setdefault() method


>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black') 
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}

The first time setdefault() is called, the dictionary in spam changes to 
{'color': 'black', 'age': 5, 'name': 'Pooka'}. 
The method returns the value 'black' because this is now the value set for the key 'color'.
When spam.setdefault('color', 'white') is called next,
the value for that key is not changed to 'white',
because spam already has a key named 'color'.
'''
