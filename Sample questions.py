#Question1
# i=int(input("enter number:"))
# fac=1
# if i<0:
#     print("negative factorial doesn't exist")
# elif i==0:
#     print("facorial of 0 is 1")
# else:
#     for i in range(1,i+1):
#         fac*=i
#     print("Factorial of ",i,"is",fac)0



#Question2
# num=int(input("enter number:"))
# total=0
# for i in range(0,num+1):
#     if i%2==0:
#         print(i)
#         total+=i
# print("Sum of even number:",total)


#Question 3
# str=input("enter string:")

# if str==str[::-1]:
#     print(str,'is palindrome')
# else:
#     print(str,'is not palindrome')


#Question 4
# def checkPrime(num):
#     if num < 2:
#         return 0
#     else:
#         x = num // 2
#         for j in range(2, x + 1):
#             if num % j == 0:
#                 return 0

#     return 1


# a=1 
# b=100
# for i in range(a, b + 1):
#     if checkPrime(i):
#         print(i, end=" ")

#Question5
# class Calculator:
#     def __init__(self):
#         self.result=0

#     def add(self,num):
#         self.result += num

#     def subtract(self,num):
#         self.result -= num

#     def multiply(self,num):
#         self.result *= num

#     def divide(self,num):
#         if num !=0:
#             self.result/=num
#         else:
#             print("Error:diviion by zero is not allowed.")

#     def calculator(self,nums):
#         for num in nums:
#             if num >0:
#                 self.add(num)
#             elif num<0:
#                 self.subtract(abs(num))

#     def get_result(self):
#         return self.result
#     c= calculator()

# numbers=[5,-2,3,0,4]
# Calculator.calculator(numbers)
# Calculator.multiply(2)
# Calculator.divide(3)

# final_result=Calculator.get_result()
# print("Final Result:",final_result)


#Question6
# words=['cat','Algorithms','supervised','Mother','Tanzeem']
# specified_length=5
# def filter_words(words_list,length):
#     new_list=[]
#     for word in words_list:
#         if len(word)>length:
#             new_list.append(word)
#     return new_list

# longer_words=filter_words(words,specified_length)
# print(longer_words)


#Question12
# number=[1,2,3,4,5,9,10,29,15,30]

# min=number[0]
# max=number[0]

# for i in range(len(number)):
#     if number[i]>max:
#         max=number[i]
#     elif number[i]<min:
#         min=number[i]

# print("Minimum number:",min)
# print("Maximum number:",max)

#Question17
# celsius= int(input("enter temp in celsius:"))

# farenheit= (celsius*(9/5))+32

# print("the converted value is ",farenheit)