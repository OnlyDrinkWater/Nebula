#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    c= 0 
    a = sorted(a)
    b = sorted(b)
    for x in range(0,len(a)):
        c= c + (a[x]*b[x])
    return c

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
