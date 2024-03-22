import random

print("Welcome to random password generator!")

randomchars = "ABCDEFGHIJKLMNOPQUSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890*&^%$#@!"

numberofpas = int(input("Please Enter The number of Password to be generated: "))

paslen = int(input("Please Enter the length of the password needed: "))

print("Here are your random passwords: ")

for x in range(numberofpas):
    pwd=""
    for chars in range(paslen):
        pwd = pwd + random.choice(randomchars)
    print(pwd)