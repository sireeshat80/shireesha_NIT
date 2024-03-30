from MulTabExcept import *
from MulTable import table
try:
    num=input("Enter a Number For Generating A Mul Table:")
    table(num)#function call
except ValueError:
    print("Dont Enter Alnums,strs and symbols for Numbers")
except ZeroError:
    print("Dont Enter Zero For Mul Table")
except NegNumError:
    print("Dont Enter Negative Numbers For Multiplication Table")
except:
    print("oops some thing went wrong")
finally:
    print("I am from finally block")