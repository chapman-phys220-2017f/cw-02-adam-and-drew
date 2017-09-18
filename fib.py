#!/usr/bin/env python

def fib(n):
    fibArray = [1,1]                                    ### Could define this in the elif for n>2
    if (n == 1):
        return [1]
    elif (n == 2):
        return [1,1]
    elif (n > 2):
        for i in range(2,n):
            fibArray.append(fibArray[i-2]+fibArray[i-1])
        return fibArray
    else:
        print("error")                                  ### Danger! Be careful to return consistent types. Better to throw an exception in the case of an input error.
        
def fib_generator():
    a = 1
    b = 1
    while True:
        yield a
        a=b
        b=a+b
        
        

if __name__ == "__main__":
    n = input("Please choose a value for n: ")         ### Never use input(). Use command-line arguments here.
    print(fib(n))
    print("Time for the fib generator!")
    gen = fib_generator()
    generated_list = [next(gen) for _ in range(n)]
    print(generated_list)
    
