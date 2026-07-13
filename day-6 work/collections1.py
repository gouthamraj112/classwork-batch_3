#used to count the occurrence of each element

'''
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
'''

from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter)
