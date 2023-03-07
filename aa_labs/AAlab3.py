import math
import time
import numpy as np
import matplotlib.pyplot as plt
from time import process_time
import random


def sieve1(n):
    c= [True]*(n+1)
    c[0]=c[1]=False
    i=2
    j=1
    while (i<=n):
        if c[i]:
            j=2*i
            while(j<=n):
                c[j]=False
                j+=i
        i+=1

def sieve2(n):
    c=[True]*(n+1)
    c[0]=c[1]=False
    i=2
    while(i<=n):
        j=2*i
        while(j<=n):
            c[j]=False
            j+=i
        i+=1
 


def sieve3(n):
    c=[True]*(n+1)
    c[0]=c[1]=False
    i=2
    while(i<=n):
        if(c[i]==True):
            j=i+1
            while(j<=n):
                if(j % i ==0):
                    c[j]=False
                j+=1
        i+=1



def sieve4(n):
    c=[True]*(n+1)
    i=2
    while(i<=n):
        j=2
        while(j<i):
            if(i % j ==0):
                c[i]=False
            j+=1
        i+=1




def sieve5(n):
    c=[True]*(n+1)
    c[0]=c[1]=False
    i=2
    while(i<=n):
        j=2
        while(j<=math.sqrt(i)):
            if(i%j==0):
                c[i]=False
            j+=1
        i+=1




algs = [
    {
        "name": "First method",
        "alg": lambda n: sieve1(n)
    },
     {
        "name": "Second method",
        "alg": lambda n: sieve2(n)
    },
     {
        "name": "Third method",
        "alg": lambda n: sieve3(n)
    },
     {
        "name": "Fourth method",
        "alg": lambda n: sieve4(n)
    },
     {
        "name": "Fifth method",
        "alg": lambda n: sieve5(n)
    }]

elements = np.array([i*100 for i in range(1, 10)])

plt.xlabel('Input Array of length n')
plt.ylabel('Time Complexity')


for alg in algs:
    times = list()
    start_all = process_time()
    a=100
    for i in range(1, 10):
        start = process_time()
        alg["alg"](a)
        end = process_time()
        a +=100
        times.append(end - start)

        print(alg["name"], " computed ", a-100, "Elements in", end - start, "s")
    end_all = process_time()
    print(alg["name"], "computed", end_all - start_all, "s")

    plt.plot(elements, times, label = alg["name"])

plt.grid()
plt.legend()
plt.show()

