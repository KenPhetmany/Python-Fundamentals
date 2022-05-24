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

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

person['age'] = 40
print(person.items())
