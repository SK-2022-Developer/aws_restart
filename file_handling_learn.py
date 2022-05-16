# python version 3.10.4
# encoding : UTF-8

# This is my first program to learn file handling

# Reading and printing data from file

fileName=input("Enter the file name to open: ")

try:
    file1=open(fileName,"r")
except FileNotFoundError:
    print("The file name entered is incorrect, try again \n")
    fileName=input("Re-enter the file name to open: ")
    file1=open(fileName,"r")

print(file1.read())
file1.close()

"""
# Writing data into text file
writeMsg="\n"+input("Enter the message to write into the file: ")
file2=open("write_test.txt","a")
file2.write(writeMsg)
file2.close()
"""



