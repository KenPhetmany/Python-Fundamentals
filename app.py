numbers = [1, 2, 3, 4, 5]

## squares = list(map(lambda number: number*2, numbers))

## squares = [number**2 for number in numbers]

# print(squares)

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

# highest_mountains = list(filter(lambda mountain: mountain[1] > 8600, mountains))

# highest_mountains = [mountain for mountain in mountains if mountain[1] > 8600]

# print(highest_mountains)
'''
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

person['age'] = 40
print(person.items())
'''
'''
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

# new_stocks = {}

# for symbol, price in stocks.items():
#    new_stocks[symbol] = price*1.02

# new_stocks = {symbol: price*1.02 for (symbol, price) in stocks.items()}

exxy_stocks = {symbol: price for (
    symbol, price) in stocks.items() if price > 200}
print(exxy_stocks)
'''

'''
tags = {'Django', 'Pandas', 'Numpy'}

# lowercase_tags = set()
# for tag in tags:
#    lowercase_tags.add(tag.lower())

lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)

'''
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s_union = s1.union(s2)

print(s_union)
