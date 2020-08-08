#A python program to automate files in your system.
#This program will automatically  arrange files according to date
import glob
import os

print("Which extension would you like to arrange : ")
print("1. .py       2.  .txt       3. .js")
questions = int(input("Enter the number : "))

if questions == 1:
    files = glob.glob("*.py")
    files.sort(key=os.path.getmtime)
    print("\n".join(files))

elif    questions == 2:
    files = glob.glob("*.txt")
    files.sort(key=os.path.getmtime)
    print("\n".join(files))

elif    questions == 3:
    files = glob.glob("*.js")
    files.sort(key=os.path.getmtime)
    print("\n".join(files))

else:
    print("Enter a valid number")