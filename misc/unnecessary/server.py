#!/usr/local/bin/python
aaabbbabab = []

for i in range(256):
    c = chr(i)
    if c not in "ab:='{}":
        aaabbbabab.append(ord(c))

test = globals()

print("pyjails really shouldn't be guessy, but this one is.")
first_input = input(">>> ")

if any([ord(c) in aaabbbabab for c in first_input]):
    print("guess harder")
    exit()

try:
    eval(first_input, test)
except Exception as e:
    print(e)

print("i kinda feel bad, so i'll let you have another try.")
second_input = input(">>> ")

if any([c in aaabbbabab for c in second_input]):
    print("guess even harder")
    exit()

try:
    eval(second_input, test)
except:
    print("error, guess harder!")
