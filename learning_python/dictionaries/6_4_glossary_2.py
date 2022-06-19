glossary = {
    'string' : 'a series of characters inside quotes',
    'whitespace' : 'any nonprint character such as spaces or tabs',
    'integers' : 'all whole numbers',
    'floats' : 'any number with a decimal point', 
    'list' : 'a collection of items in a particular order',
    '.append()' : 'a modifier used to add an item to the end of a list',
    'insert()' : 'a method used to inser a new element at any position in a list',
    'del' : 'a statement used to remove an item and do not plan to use the item',
    'sort()' : 'a method used to change the order of a list permanantly',
    'sorted' : 'a function used to maintain the original order but sort the presented order'
}

for key, value in glossary.items():
    print(key + ": " + value)