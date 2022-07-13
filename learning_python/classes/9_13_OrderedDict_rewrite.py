from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'a series of characters inside quotes'
glossary['whitespace'] = 'any nonprint character such as spaces or tabs'
glossary['integers'] = 'all whole numbers'
glossary['floats'] = 'any number with a decimal point' 
glossary['list'] = 'a collection of items in a particular order'
glossary['.append()'] = 'a modifier used to add an item to the end of a list'
glossary['insert()'] = 'a method used to inser a new element at any position in a list'
glossary['del'] = 'a statement used to remove an item and do not plan to use the item'
glossary['sort()'] = 'a method used to change the order of a list permanantly'
glossary['sorted'] = 'a function used to maintain the original order but sort the presented order'

for key, value in glossary.items():
    print(key + ": " + value)