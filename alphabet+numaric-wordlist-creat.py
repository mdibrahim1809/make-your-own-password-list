from string import *
from itertools import product
import sys , subprocess

value = ascii_letters + digits

x = input("enter the shortest length of your password :")
x = int(x)
y = input("enter the higest length of your password :")
y = int(y)

for i in range(x,y+1):
    for j in product(value,repeat = i):
        word = "".join(j)
        p = open("password.txt","a")
        p.write(word)
        p.write("\n")
        subprocess.run("clear" , shell = True)
        print("your wordlist creation is processing...")
