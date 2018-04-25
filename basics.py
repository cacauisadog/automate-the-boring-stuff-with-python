# this file is used mainly for testing and learning the very basics of the
# language, hence why it's so weird.

import random, sys, pdb, pprint

### manipulating strings
# print('''
# Ale leleo leleo leleo
#          mas que calo ooo ooor

#     Atravessando o deserto do saara's

# o sol estava quente e queimou a nossa caraa''')

### dictionary
# all_guests = {
#               'Alice': {'apples': 5, 'pretzels': 12},
#               'Bob': {'ham sandwiches': 3, 'apples': 2},
#               'Carol': {'cups': 3, 'apple pies': 1}
#             }

# def total_brought(guests, item):ll_guests = {
#               'Alice': {'apples': 5, 'pretzels': 12},
#               'Bob': {'ham sandwiches': 3, 'apples': 2},
#               'Carol': {'cups': 3, 'apple pies': 1}
#             }

# def total_brought(guests, item):
#     num_brought = 0
#     for v in guests.values():
#         num_brought += v.get(item, 0)
#     return num_brought

# print('Number of things being brought:')
# print(' - Apples:             ' + str(total_brought(all_guests, 'apples')))
# print(' - Cups:               ' + str(total_brought(all_guests, 'cups')))
# print(' - Cakes:              ' + str(total_brought(all_guests, 'cakes')))
# print(' - Ham Sandwiches:     ' + str(total_brought(all_guests, 'ham sandwiches')))
# print(' - Apple Pies:         ' + str(total_brought(all_guests, 'apple pies')))
# message = "Come back to me, it's almost easy / Come back again, it's almost easy"
# count = {}

# for c in message:
#     count.setdefault(c, 0)
#     count[c] += 1

# print(count)
# print()

# message = "Rock with me, don't stop with me, baby come dance with me."
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# print(pprint.pformat(count))

# birthdays = {'Dani':'May 29', 'Caue':'????', 'Tetinho':'Jan 14'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print('%s is the birthday of %s!\n' % (birthdays[name], name))
#     else:
#         print('I do not have birthday information for %s. What is their birthday?' % name)
#         bday = input()
#         birthdays[name] = bday
#         print('DB updated.\n')


### lists

# messages = ['Certola',
#     'Obviamente',
#     'Se pá hein',
#     'Tente de novo',
#     'Foco, nego',
#     'Acho que não hein',
#     'Hmmmm melhor deixar pra lá',
#     'Duvido muito']

# print(messages[random.randint(0, len(messages)-1)])
# list = []
# for i in range(5):
#     print("Please type %i: " % i)
#     list += input()
# print(list)

# supplies = ['pen', 'is', 'click', 'wow']
# for i in range(len(supplies)):
#     print("We have %s at index %i" % (supplies[i], i))

# dani = ['linda', 'cheirosa', 'cremosa']
# print("O que a Dani é?")
# qualidade = input()
# if qualidade not in dani:
#     print("ERRADO! A Dani é %s, %s e %s" % (dani[0], dani[1], dani[2]))

# def teste(qualidade):
#     if qualidade in dani:
#         return dani.index(qualidade)
#     else:
#         return print("a dani não é %s! >=(" % qualidade)

# print(teste('linda'))
# print()
# print(teste('feia'))

### error handling
# def spam(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         print('Error. You tried to doom the universe.')

# print(spam(2))
# print(spam(0))
# print(spam(-2))

# print()
# def spam2(divide_by):
#     return 42 / divide_by

# try:
#     print(spam2(4))
#     print(spam2(0))
#     print(spam2(-4))
# except ZeroDivisionError:
#     print('Error. You monster')
### function scope
# def spam():
#     global eggs
#     eggs = "spam"

# eggs = 'global'
# print(eggs)
# spam()
# print(eggs)
# def get_answer(answer):
#     if answer == 1:
#         return 'Certainly'
#     elif answer == 2:
#         return 'Sure'
#     elif answer == 3:
#         return 'Probably yes'
#     elif answer == 4:
#         return 'I think so'
#     elif answer == 5:
#         return 'Maybe'
#     elif answer == 6:
#         return 'Maybe not'
#     elif answer == 7:
#         return "Doesn't look like it"
#     elif answer == 8:
#         return "Don't count on it"
#     elif answer == 9:
#         return 'Nope'
#     elif answer == 10:
#         return 'No fucking way.'

# answer = int(input())

# print(get_answer(answer))

# print('\nType a number: ')
# number = input()
# if number == '1':
#     print('Hello')
# elif number == '2':
#     print('Howdy.')
# else:
#     print('Greetings!')

# # This program says hello and asks for my name

# print('Hello world!')
# print('What is your name?')   # ask for their name
# my_name = input()
# print('It is good to meet you, ' + my_name)
# print('The length of your name is: ' + str(len(my_name)))
# print('What is your age?')  # ask for their age
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year!')

# # if block
# if my_name == 'Mary':
#     print('\nHello Mary')
#     print('Please enter your password: ')
#     password = input()
#     if password == 'swordfish':
#         print('Access granted')
#     elif password == 'bubba':
#         print('Try again: ')
#         password = input()
#         if password == 'swordfish':
#             print("That's it.")
#         else:
#             print("Get out, you bustah")
#     else:
#         print('Wrong password')

# # while block
# while True:
#     print('Who are you?')
#     my_name = input()
#     if my_name != 'Joe':
#         continue
#     print('Why hello there, John. What is the password my man?')
#     password = input()
#     if password == 'swordfish':
#         break
#     else:
#         print('No dice.')
# print('Come in nigga')

# # truthy and falsy values
# my_name = ''
# while not my_name:
#     print('Enter your name: ')
#     my_name = input()
# print('How many guests will you have?')
# num_of_guests = int(input())
# if num_of_guests:
#     print('Be sure to have enough room for everybody!')
    
# print('Done!')

# # for blocks
# print('My name is')
# for i in range(5):
#     print('Jimy Five Times (' + str(i) + ')')   #i in parenthesis

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# print(list(range(12,16)))

# for i in range(5):
#     print(random.randint(1, 10))

# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '. Goodbye!')
