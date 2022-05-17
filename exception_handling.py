# python version 3.10.4
# encoding : UTF-8

# Practice program for exception handling

#Function that divides 5 by number entered
def div_by_5(num):
    try:
        result=5/num
    except ZeroDivisionError:
        print("Do not div by zero, pass another value")
        result=1
    return result

print(div_by_5(0))
print("This program successfully completed")
