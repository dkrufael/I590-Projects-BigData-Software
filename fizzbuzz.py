#!python
"""this is the first python assignment 
"""
# this function takes an integer argument and prints the result result of the function
def fizzbuzz(n):
    # accepting the returned intiger
   
    for i in range(1,n+1):
        if i%2 ==0:
           if i%3 ==0:
              print "fizzbuzz"
           else:
              print "fizz"
        else:
             if i%3 ==0:
                print "buzz"
             else:
                print i
    return
# this prompts the user for an input
n = int(input("Enter a number: "))
fizzbuzz(n)


