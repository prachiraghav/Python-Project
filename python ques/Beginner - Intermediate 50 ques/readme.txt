Beginner Level (1–25)
Focus: Syntax, data types, loops, conditionals, functions, strings, lists, and dictionaries.
1. Write a program to print "Hello, World!".
2. Take a number input from the user and print whether it’s even or odd.
3. Write a function to return the square of a number.
4. Take two numbers and print their sum, difference, product, and quotient.
5. Check if a number is positive, negative, or zero.
6. Write a function to check if a number is prime.
7. Print the first 10 natural numbers using a for loop.
8. Find the factorial of a number using a while loop.
9. Print the multiplication table of a given number.
10. Write a function to find the maximum of three numbers.
11. Reverse a string without using built-in methods.
12. Count the number of vowels in a string.
13. Write a function to check if a string is a palindrome.
14. Write a program to count how many times a word appears in a sentence.
15. Create a list of numbers and print only the even ones.
16. Write a function to calculate the sum of all numbers in a list.
17. Remove duplicates from a list.
'''
def is_palindrome(a):
    # Check if the string is the same reversed
    return a == a[::-1]
   
a = str(input()) 
if is_palindrome(a):
    print("is a palindrome")
else:
    priint("is not a palindrome")
    


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))


def words(s):
    words = s.split()
    cnt = len(words)
    return cnt
a = input()
print("count:", words(a))



def even(s):
    b = []
    for i in s:
       if i%2==0:
           b.append(i)
    return b


a = [1,2,3,4,5,6,7,8,9,10]

print("Even number  in list", even(a))


num = [1,5,9,85,67,19,1897,46519,111,23]
a  =0
for i in num:
    a = a+ i

print(a)

a = [1,1,2,2,2,3,5,1,8,2,2,7,4,1,2,]
unique = list(set(a))
print(unique)

18. Sort a list without using the built-in sort() function.
19. Create a dictionary and print its keys and values.
a = {'model': 1920, 'color': 'red','fruit':['apple','banana','cherry']}
a.update({'size':['s','m','l']})
b = a.keys()
c = list(a.values())
print(b)
print(c[3][1])

20. Add a new key-value pair to a dictionary.
21. Write a function that takes a list and returns a list of squares of all even numbers.
22. Create a list of 5 items and find the largest and smallest elements.
23. Convert Celsius to Fahrenheit using a function.
24. Write a function that accepts a string and returns the count of each character.
'''
a = {'model': 1920, 'color': 'red','fruit':['apple','banana','cherry']}
a.update({'size':['s','m','l']})
b = a.keys()
c = list(a.values())

print(b)
print(c[3][1])


a = list(map(int,input().split()))
b=[]
for i in a:
    if i%2==0:
        b.append(i**2)
print(b)

a = [2,5,3,6,8]
largest = a[0]
smallest = a[0]
for i in a: 
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print(largest)
print(smallest)

0°C × 9/5) + 32 

c = int(input())
def fer(a):
    return a * (9/5) +32

print(fer(c))

'''
'''

def sen(b):
    count = {}
    for char in b:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
sentence = str(input())
result = sen(sentence)
print(result)
'''
25. Write a program to simulate a simple calculator (add, subtract, multiply, divide).

Intermediate Level (26–50)
Focus: File handling, list comprehensions, exception handling, OOP, simple algorithms.

26. Read a file and count the number of lines.
27. Write to a file and then read the content.
28. Use list comprehension to generate squares of numbers 1 to 10.
29. Write a function to find all prime numbers in a given range.
30. Create a class Person with attributes name and age. Add a method to display them.
31. Create a class BankAccount with deposit and withdraw methods.
32. Write a function to count the frequency of words in a text file.
33. Create a simple password strength checker (length >= 8, contains digits and special characters).
34. Handle division by zero using exception handling.
35. Find the second largest number in a list.
36. Check whether a string is an anagram of another string.
37. Write a function to return the Fibonacci series up to n terms.
38. Find the sum of digits of a number using recursion.
39. Count the number of uppercase and lowercase letters in a string.
40. Merge two sorted lists into a single sorted list.
41. Write a program to remove punctuation from a string.
42. Flatten a nested list (e.g., [[1, 2], [3, 4]] → [1, 2, 3, 4]).
43. Write a program to check if a year is a leap year.
44. Convert a string to title case without using title() method.
45. Write a function to find the GCD of two numbers.
46. Implement a simple number guessing game.
47. Write a function to rotate a list by n positions.
48. Create a basic contact book using a dictionary.
49. Write a program to find the intersection of two lists.
50. Write a function to check if a list is sorted or not.

