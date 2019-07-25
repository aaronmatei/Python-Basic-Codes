# def total_marks(a,b,c,d,e):
#     total = (a+b+c+d+e)
#     return total
#
# def avg_marks(total):
#     avgm = total/5
#     return avgm
# def findGrade(avgm):
#     if avgm > 80:
#         return 'A'
#     elif (avgm >= 70) and (avgm < 80):
#         return 'B'
#     elif (avgm >= 60) and (avgm < 70):
#         return 'C'
#     elif (avgm >= 50) and (avgm < 60):
#         return 'D'
#     else:
#         return 'E'
#
# total=total_marks(35,56,55,63,64)
# average = avg_marks(total)
# grade = findGrade(average)
#
# print("Total Marks is : {} , Average is : {} , and Grade is : {} ".format(total,average,grade))

#
# def EvenGenerator(n):
# #     i=0
# #     while i<=n:
# #         if i%5==0 and i%7==0:
# #             yield i
# #         i+=1
# #
# # n=int(input("enter n: "))
# # values = []
# # for i in EvenGenerator(n):
# #     values.append(str(i))
# #
# # print (",".join(values))

# def generator(number):
#     for i in range(number+1):
#         if i%35 == 0:
#             yield i
#
# number = int(input("Enter number: "))
# values = [str(i) for i in generator(number)]
# print(",".join(values))
#
# data = [2,4,5,6]
# for i in data:
#     assert i%2 == 0, "{} is not an even number".format(i)
# import random
# rand_num = random.uniform(10,100)
# print("{:.8f}".format(rand_num))
import random
resp = [i for i in range(10,151) if i % 35 == 0 ]
print(random.choice(resp))

# str = random.sample(range(10,151),5)
# print(str)