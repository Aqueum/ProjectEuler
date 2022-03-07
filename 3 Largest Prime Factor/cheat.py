# from https://www.geeksforgeeks.org/find-largest-prime-factor-number/
import math
 
# A function to find largest prime factor
def maxPrimeFactors (n):
     
    # Initialize the maximum prime factor
    # variable with the lowest one
    maxPrime = -1
    print("-1 ", maxPrime)
     
    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        print("2 ", maxPrime)
        n >>= 1     # equivalent to n /= 2
         
    # n must be odd at this point
    while n % 3 == 0:
        maxPrime = 3
        print("3 ", maxPrime)
        n=n/3
     
    # now we have to iterate only for integers
    # who does not have prime factor 2 and 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            maxPrime = i
            print("i ", maxPrime)
            n = n / i
        while n % (i+2) == 0:
            maxPrime = i+2
            n = n / (i+2)
            print("i+2 ", maxPrime)
         
    # This condition is to handle the
    # case when n is a prime number
    # greater than 4
    if n > 4:
        maxPrime = n
        print("n>4 ", maxPrime)
     
    return int(maxPrime)
 
# Driver code to test above function
 
n = 13195
print(maxPrimeFactors(n))
