# def squaring(nums):

#     # squares = []
#     for number in nums:
#         yield (number*number)

squared = [x*x for x in [4,6,3,2]]  #this is comprehension list
# print(squared)

# squared1 = (x*x for x in [1,5,4,6,3,2]) #this is a generator
# print(list(squared1))
#
# print(next(squared))

for num in squared:
    print(num)

nums = [2,3,4,5,6,7,8]
for num in nums:
    print(num)

print("------------------------")

iterate_list = iter(nums)

while True:
    try:
        item = next(iterate_list)
        print(item)
    except StopIteration:
        break

# date_today = datetime.datetime.today()