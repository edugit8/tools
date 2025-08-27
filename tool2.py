import os

with open("file.txt","a",encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines :
        print(line)