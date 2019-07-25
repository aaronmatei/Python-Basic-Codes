# TASK 1:
# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes",
# otherwise print "No".
# Hint: Use input () to get the persons input

#
# string = input("Enter String: ")
# if string == "yes":
#     print("Yes")
# elif string == "YES":
#     print("Yes")
# elif string == "Yes":
#     print("Yes")
# else:
#     print("No")

# TASK 2:
# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max () function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.


# def largest (lst):
#     if (a > b) and (a > c):
#         return '{}: is the largest'.format(a)
#     elif (b>a)and(b>c):
#         return '{}: is the largest'.format(b)
#     elif (a==b)and(b==c):
#         return 'The three numbers are equal'
#     else:
#         return '{}: is the largest'.format(c)
#
# print(largest(48,48,46))

# Task3
# def list_numbers(list):
#     new_list=[]
#     if len(list)==1:
#         return list
#     else:
#         new_list.append(list[0])
#         new_list.append(list[-1])
#         return new_list
#
# print(list_numbers([3]))



# TASK 4:
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# number = int(input("Enter the number: "))
# if number%2==0:
#     print("The number is even")
#     if number%4==0:
#         print("The number is even and also multiple of 4")
# else:
#     print("The number is odd")

# Task5

tp =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_half = []
second_half = []
for item in range(0,int(len(tp)/2)):
    first_half.append(tp[item])
for item in range(int(len(tp)/2),int(len(tp))):
    second_half.append(tp[item])

print(first_half)
print(second_half)








