# 5. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

list1 = [0,3,4,7,9]
list2 = [3,5,7,13]
list3 = [1,5,3]

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def all_primes(numbers):
    return all(isPrime(num) for num in numbers)

print(all_primes(list1))
print(all_primes(list2))
print(all_primes(list3))