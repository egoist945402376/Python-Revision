print("1024 * 768 =", 1024 * 768)

bob = {
    'name': 'Bob',
    'age': 20,
    'score':88
}

#fstring
print(f"I have a friend, his name is {bob['name']}, he is {bob['age']} years old, and his score is {bob['score']}")

#format method
print("I have a friend, his name is {0}, he is {1} years old, and his score is {2}".format(bob['name'], bob['age'], bob['score']))

a = 3.1415926
print(f"{a:2f}")
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)