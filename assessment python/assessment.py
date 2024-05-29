
#print hello world
print("HELLO WORLD!")


#print sum
a=int(input("enter a number"))
b=int(input("enter a number"))
c=a+b
print(c)
print("the sum of the two numbers are:",c)


#largest value
n1=int(input("enter a number1:"))
n2=int(input("enter a number2:"))
n3=int(input("enter a number3:"))
print ("check the largest value in those numbers")
if n1>n2:
    print("the largest value is",n1)
elif n2>n3:
    print("the largest value is",n2)
elif n3>n1:
    print("the largest value is",n3)
    
    
#even or odd
 n=int(input("enter any number"))
 print("to check the number if it is even or odd")
 if n%2==0:
  print("even")
 else:
  print("odd")
  

 #calculate the factorial
   import math
   def factorial(n):
     return(math.factorial(n))
   num=8
   print(factorial(num))
   

#reverse the string
str="data science"
print(str[: :-1])


#palindrome or not
def isPalindrome(s):
	return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
    
    
#count no. of vowels in string
string = "hello krithi!"
vowels = "aeiouAEIOU"
count = sum(string.count(vowel) for vowel in vowels)
print(count)



#sum of all elements in array
 
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list: ", total)


# Python code to remove duplicate elements
def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


#sort the elemets in a ascending order
alphabets = ['a','e','d','c','b'] 
alphabets.sort() 
print(alphabets) 

random_numbers = [2,5,6,1,8,3] 
random_numbers.sort() 
print(random_numbers)


# Python program to find largest number

list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
list2 = list(set(list1))
list2.sort()
print("Second largest element is:", list2[-2])


# Program to display the Fibonacci sequence 

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
