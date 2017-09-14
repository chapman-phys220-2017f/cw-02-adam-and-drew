
#Create a function to generate equally spaced coordinates.

#Using for loop 

def coord_for(n,a=0,b=1):
    coords_list = []
    a = float(a)
    b = float(b)
    h = (b-a)/n
    for i in range(n+1):
        coords_list.append((a+(i*h)))
    return coords_list

#Using While Loop

def coord_while(n,a,b):
    coords_list = []
    a = float(a)
    b = float(b)
    h = (b-a)/n
    while ((a+i) <= b):
        coords_list.append(a+i)
        i = i+h 
    return coords_list
    
#Using List Comprehension

def coord_comp(n,a=0,b=1):
    a = float(a)
    b = float(b)
    h = (b-a)/n
    coords_list = [a+i*h for i in range(n+1)]
    return coords_list

#Use Main Block (takes user input and call the three previously defined functions)
#Define n (integer number of intervals, a (starting point), and b (end point)


if _name_ == "_main_":
    n = input("Number of intervals (n): ")
    a = input("Starting at a: ")
    b = input("And ending at b: ")
    for_list = coord_for(n,a,b)
    while_list = coord_while(n,a,b)
    comp_list = coord_comp(n,a,b)
    print("With a for loop: ", for_list)
    print("with a while loop: ",)
    
    
    

