# lst = [str(i) for i in range(1000,3001)]
# lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i),lst ))   # using lambda to define function inside filter function
# print(",".join(lst))


# string = input("Enter the sentense")
# upper = 0
# lower = 0
# for x in string:
#     if x.isupper() == True:
#         upper += 1
#     if x.islower() == True:
#         lower += 1
#
# print("UPPER CASE: ", upper)
# print("LOWER CASE: ", lower)

import  re

s = input("Enter passwords: ").split(',')
lst = []

for i in s:
    cnt = 0
    cnt+=(6<=len(i) and len(i)<=12)
    cnt+=bool(re.search("[a-z]",i))      # here re module includes a function re.search() which returns the object information
    cnt+=bool(re.search("[A-Z]",i))      # of where the pattern string i is matched with any of the [a-z]/[A-z]/[0=9]/[@#$] characters
    cnt+=bool(re.search("[0-9]",i))      # if not a single match found then returns NONE which converts to False in boolean
    cnt+=bool(re.search("[@#$]",i))      # expression otherwise True if found any.
    if cnt == 5:
        lst.append(i)

print("These are the real pass:", ",".join(lst))