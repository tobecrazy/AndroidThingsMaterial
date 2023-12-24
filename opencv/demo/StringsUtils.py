#!/usr/bin/python3

source = "dog cat CAT Mi Go"
words = {}
array1 = source.split(" ")
for i in range(0, len(array1) - 2):
    if array1[i].lower() == array1[i + 1].lower():
        print(array1[i] + " " + array1[i + 1])
        words[array1[i]] = 1
print(len(words))
