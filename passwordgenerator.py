from ntpath import join
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letter_num = int(input("how many letters in your password"))
#symbol_num = int(input("how many symbols do u like"))
num_num = int(input("how many number do u like"))
password = []
for i in range (letter_num):
    password.append(random.choice(letters))

for i in range (num_num):
    password.append(str(random.choice(numbers)))


random.shuffle(password)
print(password)
print(''.join(password))