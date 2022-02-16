'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.


Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

v = [odd , even]

'''


def sumsquare(l):
    v = [0,0]
    if len(l)!=0:
        for i in l:
            if i%2==0:
                v[1]+= i*i
            else:
                v[0]+= i*i
                
    return v
                
                



print (sumsquare([-1,-2,3,7]))
