import csv
import os

f = open("hello.txt", "w")
f.write("Hello, this is a new file and Im testing stuffs!")
f.close()
f = open("hello.txt", "r")
print(f.read())
f.readline()
f.close()

os.remove("hello.txt")
